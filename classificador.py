import csv
import json
import re
import nltk
import sys
import collections

from pymongo import MongoClient

# from nltk.classify import apply_features

CATEGORY_GROUP = {
	'apoio' : ['PRO','CONTRA','INDEFINIDO'],
	'enquadramento' : ['DEMOCRACIA',
					   'ECONOMIA',
					   'MINORIAS',
					   'CORRUPCAO',
					   'INTERNACIONAL',
					   'IDEOLOGIA',
					   'COTIDIANO',
					   'MIDIA',
					   'HISTORIA',
					   'MOBILIZACAO',
					   'OUTROS',
					   'OFENSAS']
}



# 1.1. Hard coded no codigo
# def load_preclassified_corpora():
	# return {
	# 	'pro' : ["pirando legal na batatinha: 'o golpe é homofóbico e racista'. - paaaaaaaaaaaaara tudo que eu quero… ",
	# 			 "golpe é eu não estar te chupando agora!",
	# 			 "@stf_oficial fracassa perante a sociedade brasileira. #somostodosgolpistas "],
	# 	'contra' : ["um homem no ônibus nos perguntou se o motivo de estarmos de preto era o golpe. n saímos c essa intenção, mas n é que encaixa perfeitamente..",
	# 				"@o_antagonista golpe é isso, ferir a constituição.",
	# 				"impitma sem crime é golpe "],
	# 	'indeciso' : []
	# }


# 1.2. Carregado a partir do CSV
def load_preclassified_corpora(filename,classification):

	categories = CATEGORY_GROUP[classification]

	classified_corpora = collections.defaultdict(list) # um dict como outro qualquer, que atribuiu 
													   # uma lista vazia automaticamente a novas chaves
													   # criadas, evitando fazer d['k'] = {} 
													   # So isso :-)

	with open(filename, newline='') as csvfile:
		
		# 1.2.1. Como acessar os campos do CSV

		# 1.2.1.1 Ler CSV como Array e acessar os campos atraves de indices: row[0], row[1]...
		# reader = csv.reader(csvfile, delimiter=',', quotechar='"')

		# 1.2.1.2. Ler como Dict e acessar os campos atraves de chaves: row['nome'], row['endereco']...
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

		for row in reader:
			# 1.2.1.1 
			# print(row[4],row[5],row[6],row[7])

			# 1.2.1.2.
			# print(row['TEXTO'],row['PRO'],row['CONTRA'],row['INDEFINIDO'],bag_of_words(row['TEXTO']))

			# 'categories' eh utilizado para se definir qual classificacao 
			# se deseja fazer. No nosso caso, temos duas possibilidades:
			# quanto ao 'apoio' do tweet ao impeachment e quanto
			# ao 'enquadramento' do tweet em uma taxonomia de termos
			# por nos definida.
			for category in categories:
				if row[category] is not None and len(row[category]) and int(row[category]):
					label = category

				# O for acima eh a mesma coisa que a sequencia de ifs abaixo, 
				# para o caso da classificacao por 'apoio':
				#
				# if int(row['PRO']):
				# 	label = 'PRO'
				# elif int(row['CONTRA']):
				# 	label = 'CONTRA'
				# elif int(row('INDEFINIDO']):
				# 	label = 'INDEFINIDO' 
			
			
			classified_corpora[label].append(row['TEXTO'])


		if classification == 'apoio':
			print('%s|%i|%i|%i||' % (filename,
									len(classified_corpora['PRO']),
									len(classified_corpora['CONTRA']),
									len(classified_corpora['INDEFINIDO'])))
		elif classification == 'enquadramento':
			print('%s|%i|%i|%i|%i|%i|%i|%i|%i|%i|%i|%i|%i|' % (filename,
															len(classified_corpora['DEMOCRACIA']),
															len(classified_corpora['ECONOMIA']),
															len(classified_corpora['MINORIAS']),
															len(classified_corpora['CORRUPCAO']),
															len(classified_corpora['INTERNACIONAL']),
															len(classified_corpora['IDEOLOGIA']),
															len(classified_corpora['COTIDIANO']),
															len(classified_corpora['MIDIA']),
															len(classified_corpora['HISTORIA']),
															len(classified_corpora['MOBILIZACAO']),
															len(classified_corpora['OFENSAS']),
															len(classified_corpora['OUTROS'])))


	return classified_corpora

# 1.3. Lido diretamente a partir do Google Spreadsheet
# TODO (ver gsheet.py)

####################
# 1. Funcao geradora de features

# 1.1. Features muito muito simples
# def impeachment_features(sentence):
# 	if 'golpe' in sentence:
# 		return {'golpe' : True}
# 	else:
# 		return {'golpe' : False}


# 1.2. Estrategia de features com bag of words.
# sentence= um homem no ônibus nos perguntou se o motivo de estarmos de preto era o golpe.
# words= ['um', 'homem', 'no', 'ônibus', 'nos', 'perguntou', 'se', 'o', 'motivo', 'de', 'estarmos', 'de', 'preto', 'era', 'o', 'golpe']
# bagofwords= {'se': True, 'motivo': True, 'era': True, 'de': True, 'o': True, 'golpe': True, 'um': True, 'nos': True, 'ônibus': True, 'homem': True, 'estarmos': True, 'no': True, 'perguntou': True, 'preto': True}
def bag_of_words(sentence):
	# Tira a pontuacao e quebra em array de palavras
	words = re.sub('[\.,!?…:\n]','',sentence).split(" ")
	return dict([(word, True) for word in words])
	# TODO1 Remover stopwords
	# TODO2 Incluir bigramas

# 1. Exemplo
# [({:},),({:},)]
# features_treinamento = [({'golpe':True},'contra'),
# 	

# Transforma {	'pos' : ['texto1','texto2',...], 
#				'neg' : ['texto',...]}
#
# em 		 {	'pos' : [{'plot':True, ':':True, 'teen':True ...}, {}, {}...], 
#				'neg' : [{},{},...] }
def get_features(corpora):
	features = collections.defaultdict(list)

	# Pra cada categoria .e pos, contra e indefinido
	for category in corpora.keys(): 

		print(' %s: %d' % (category,len(corpora[category])))

		# Pra cada texto da atual categoria
		for corpus in corpora[category]:
			features[category].append(bag_of_words(corpus))

	return features  


# Funcao auxiliar
# Reparte as features classificadas em dois grupos: 
# um para treinamento (75%) e outro para testes (25%).
# Em ambos, quantidades identicas de features de cada
# uma das categorias.
def split_features(lfeats, split):
	train_feats = []
	test_feats = []

	for label, feats in lfeats.items():
		# label=contra 		len(feats)=655 (492+163)
		# label=pro 		len(feats)=133
		# label=indefinido  len(feats)=195
		cutoff = int(len(feats) * split)

		# os primeiros 75% de features do label, vao para treinamento
		train_feats.extend([(feat, label) for feat in feats[:cutoff]])
		# os 25% restantes, para teste
		test_feats.extend([(feat, label) for feat in feats[cutoff:]])
	
	print('training_features=',len(train_feats))
	print('test_features=',len(test_feats))

	return train_feats, test_feats





def adhoc_classification_tests(classifier):
	texto = 'RT @JFMargarida: Juiz de Fora mantém a sua tradição democrática. Praça das estação contra o golpe #GolpeAquiNaoPassa https://t.co/LfIOsDaIVj'
	print('[%s] %s' % (classifier.classify(bag_of_words(texto)), texto))
	texto = 'Rio de Janeiro\n\nMST tranca a Dutra\n\nNa luta contra o golpe, a memória do massacre de Eldorado dos Carajás -20 anos https://t.co/26rk7OADEJ'
	print('[%s] %s' % (classifier.classify(bag_of_words(texto)), texto))
	texto = 'Ñ permitiremos q corruptos governem, não daremos paz nem um dia ,perseguiremos o Temer até na hora d colocar botox! https://t.co/LsgWDbnosM'
	print('[%s] %s' % (classifier.classify(bag_of_words(texto)), texto))

	texto = 'RT @JFMargarida: Juiz de Fora mantém a sua tradição democrática. Praça das estação contra o golpe #GolpeAquiNaoPassa https://t.co/LfIOsDaIVj'
	probs = classifier.prob_classify(bag_of_words(texto))
	probs = [ (label,probs.prob(label)) for label in probs.samples() ]
	print('[%s] %s' % (probs, texto))
	texto = 'Rio de Janeiro\n\nMST tranca a Dutra\n\nNa luta contra o golpe, a memória do massacre de Eldorado dos Carajás -20 anos https://t.co/26rk7OADEJ'
	probs = classifier.prob_classify(bag_of_words(texto))
	probs = [ (label,probs.prob(label)) for label in probs.samples() ]
	print('[%s] %s' % (probs, texto))
	texto = 'Ñ permitiremos q corruptos governem, não daremos paz nem um dia ,perseguiremos o Temer até na hora d colocar botox! https://t.co/LsgWDbnosM'
	probs = classifier.prob_classify(bag_of_words(texto))
	probs = [ (label,probs.prob(label)) for label in probs.samples() ]
	print('[%s] %s' % (probs, texto))

# def classify_text(classifier):
	# i = 0
	# Classificar tweets
	# json_file = open('RT_democracia_golpe_Abr2016.txt','r')
	# json_file = open('RT_democracia_golpe_Ago2016.txt','r')
	# for line in json_file:

	# 	i += 1

	# 	if line[0] == '{':
	# 		# print('line=',line)

	# 		obj = json.loads(line)
	# 		# print('obj=',obj)

	# 		id = obj['id']
	# 		# texot = obj['']

	# 		if "retweeted_status" in obj:
	# 			id_retweetado = obj['retweeted_status']['id']
	# 			texto_retweetado = obj['retweeted_status']['text'] 
	# 			#.replace('"',"'").replace("\n"," - ")
	# 			#texto = re.sub(":(\w)", "\:\\1", texto)
	# 			# texto = re.sub("http.*?( |$)","",texto)
	# 			# if "golp" in texto.lower():
	# 						# if detect(texto) == 'pt':
	# 			# texto.encode('utf-8').decode('utf-8').encode('cp1252','ignore').decode('cp1252'))

	# 			# print('%s,%s,%s' % (id, id_retweetado, texto_retweetado))
	# 			print('%d,%s,%s' % (i,texto_retweetado, classifier.classify(impeachment_features(texto_retweetado))))

def classify_text(classifier):
	print('Iniciando classificao dos textos do banco')

	# acessar o mongo
	print('Conectando ao Mongo...')
	client = MongoClient()
	db = client.impeachment

	# Remove documentos da classificacao anterior
	print('Removendo documentos da classificacao anterior...')
	db.tweets_classificados.delete_many({})

	# Busca apenas textos dos tweets
	print('Buscando texto dos tweets retweetados...')
	texts = db.tweets.aggregate([ 
				{'$match': { 'retweeted_status.text' : { '$regex' : 'golp', '$options' : 'i' } } }, 
				{'$project': { '_id':0, 'text' : "$retweeted_status.text"} } ])
	print("XX tweets encontrados")

	i = 0
	# Classifica cada um dos textos e salva o resultado de volta no banco
	for doc in texts:
		text = doc['text']

		i += 1
		print('Classificando tweet %i (%s)' % (i,text))

		probs = classifier.prob_classify(bag_of_words(text))
		texto_classificado = {
			'texto': text,
			'classeMaisProvavel': probs.max(),
			'probabilidades' : {
				'pro': probs.prob('pro'),
				'contra': probs.prob('contra'),
				'indefinido': probs.prob('indefinido'),
			}
		}
		
		id_texto_classificado = db.tweets_classificados.insert_one(texto_classificado)
		print("  Resultado da classificacao salvo no banco com id",id_texto_classificado)


if __name__ == '__main__':

	# PASSO 1. Carregar os dados pre-classificados

	filename = 'datasets/20161116/AmostraABRIL-AriadneeMarisaREDUZIDA.utf8.csv' # 60%, Enquadramento: 16.43
	# filename = 'datasets/20161115/textos-preclassificados-abril-e-agosto-20161117.csv'	# 48%, Enquadramento: 17.69%
	# filename = 'datasets/20161115/AmostraAGOSTOREVIS1411.utf8.csv' # 50%, Enquadramento: 17.26%
	# filename = 'datasets/20161115/AmostraABRIL-AriadneeMarisaREVIS2.utf8.csv' # 66%, Enquadramento: 14.69%
	# filename = 'datasets/AmostraAGOSTO - AMOSTRAAGO10003110-2.csv' # Apoio: 49%, Enquadramento: 14%

	classification = 'apoio'
	# classification = 'enquadramento'

	preclassified_corpora = load_preclassified_corpora(filename,classification) 

	# PASSO 2. Cálculo das features dos textos pre-classificados
	preclassified_features = get_features(preclassified_corpora)

	# PASSO 3. Definição das bases de teste (75%) e treinamento (25%)
	train_features, test_features = split_features(preclassified_features, split=0.75)

	# PASSO 4. Criacao e treinamento do classificador
	classifier = nltk.NaiveBayesClassifier.train(train_features)

	# PASSO 5. Verificação da acurácia a partir da base de teste
	print('accuracy=',nltk.classify.accuracy(classifier, test_features))

	# Listagem das features mais relevantes
	print('most_informative_features=',classifier.most_informative_features())
	print('-------')
	classifier.show_most_informative_features(5)

	# Testes ad-hoc
	# adhoc_classification_tests(classifier)

	# PASSO 6. Classificacao da base de dados real
	# classify_text(classifier)


