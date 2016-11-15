import csv
import json
import re
import nltk
import sys
import collections

# CATEGORIES = [ 'pro', 'contra', 'indiferente' ]

# from nltk.classify import apply_features

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

# 15/11 18:04
# Bag of words com stopwords
# Planilha do GDcos
# 	contra = 655
# 	pro = 133
# 	indefinido = 195
# training_features= 736
# test_features= 247
# accuracy= 0.4939271255060729
# Most Informative Features
#                    mesmo = True           indefi : contra =     12.3 : 1.0
#                    dando = True           indefi : contra =     12.3 : 1.0
#                      fez = True           indefi : contra =     12.3 : 1.0
#                    renan = True           indefi : contra =     12.3 : 1.0
#                       12 = True              pro : contra =     11.5 : 1.0

# 15/11 21:12 - Com nova classificacao de Abril enviada pela Tayrine
# Bagofwords ainda co stopwords
# training_features= 726
# test_features= 244
# accuracy= 0.6598360655737705
# most_informative_features= [('quando', True), ('vou', True), ('corao', True), ("sim'", True), ('dizer', True), ('imagina', True), ('deu', True), ('copa', True), ('10', True), ('manter', True), ('coisa', True), ("'eu", True), ('algum', True), ('militncia', True), ('sei', True), ('p', True), ('te', True), ('dias', True), ('proibido', True), ('&gt;', True), ('silvio', True), ('deixar', True), ('ai', True), ('funkeiros', True), ('perto', True), ('boca', True), ('entender', True), ('gritando', True), ('mesmo', True), ('faz', True), ('tu', True), ('realmente', True), ('total', True), ('segue', True), ('dinheiro', True), ('pouco', True), ('quanto', True), ('legalidade', True), ('sade', True), ('preo', True), ('ela', True), ('eu', True), ('#impeachmentday', True), ('hora', True), ('stf', True), ('eh', True), ('fala', True), ('democracia', True), ('#golpeaquinopassa', True), ('6', True), ('engraado', True), ('20', True), ('escolher', True), ('100', True), ('vida', True), ('continua', True), ('ok', True), ('costa', True), ('br', True), ('farsa', True), ('houver', True), ('quero', True), ('casa', True), ('juntos', True), ('moraes', True), ('amigos', True), ('for', True), ('bola', True), ('portal', True), ('querido', True), ('cozinha', True), ("'se", True), ('mostra', True), ('protestos', True), ('participar', True), ('gavies', True), ('3', True), ('voltar', True), ('pessoa', True), ('ba', True), ("'nunca", True), ('caia', True), ('numa', True), ('sero', True), ('senador', True), ("'no", True), ('@portalvermelho', True), ('indo', True), ('pr-golpe', True), ('vitria', True), ('transmitir', True), ('filha', True), ('ah', True), ('galera', True), ('tbm', True), ('oq', True), ('@brasil_de_fato', True), ('vejo', True), ('17/04', True), ('@folha', True)]
# -------
# Most Informative Features
#                   quando = True              pro : contra =     20.0 : 1.0
#                      vou = True              pro : contra =     14.7 : 1.0
#                    corao = True              pro : contra =     14.7 : 1.0
#                     sim' = True           indefi : contra =     14.6 : 1.0
#                    dizer = True              pro : contra =     12.0 : 1.0


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

		# Pra cada texto da atual categoria
		for corpus in corpora[category]:
			features[category].append(bag_of_words(corpus))

	return features  


# Funcao auxiliar
# Reparte as features classificadas em dois grupos: 
# um para treinamento (75%) e outro para testes (25%).
# Em ambos, quantidades identicas de features de cada
# uma das categorias.
def split_features(lfeats, split=0.75):
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
	
	return train_feats, test_feats




####################
# 2. Texto pre-classificado para treinamento e testes

# 2.1. Hard coded no codigo
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


# 2.2. Carregado a partir do CSV
def load_preclassified_corpora(filename):
	classified_corpora = collections.defaultdict(list) # um dict como outro qualquer, que atribuiu 
													   # uma lista vazia automaticamente a novas chaves
													   # criadas, evitando fazer d['k'] = {} 
													   # So isso :-)

	with open(filename, newline='') as csvfile:
		
		# 2.2.1. Como acessar os campos do CSV

		# 2.2.1.1 Ler CSV como Array e acessar os campos atraves de indices: row[0], row[1]...
		# reader = csv.reader(csvfile, delimiter=',', quotechar='"')

		# 2.2.1.2. Ler como Dict e acessar os campos atraves de chaves: row['nome'], row['endereco']...
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

		for row in reader:
			# 2.2.1.1 
			# print(row[4],row[5],row[6],row[7])

			# 2.2.1.2.
			# print(row['TEXTO'],row['PRO'],row['CONTRA'],row['INDEFINIDO'],bag_of_words(row['TEXTO']))

			if int(row['PRO']):
				label = 'pro'
			elif int(row['CONTRA']):
				label = 'contra'
			else:
				label = 'indefinido' 
			
			
			classified_corpora[label].append(row['TEXTO'])


	return classified_corpora

# 2.3. Lido diretamente a partir do Google Spreadsheet
# TODO (ver gsheet.py)

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

# def classify_text(classifier):
	# acessar o mongo
	# db.tweets.aggregate([ {$project: { _id:0, text : "$retweeted_status.text"} } ])

if __name__ == '__main__':

	# Carregar os dados de treinamento e teste
	preclassified_corpora = load_preclassified_corpora('AmostraABRIL-AriadneeMarisaREVIS2.utf8.csv')
	# iconv -c -t UTF8 AmostraABRIL-AriadneeMarisaREVIS2.csv > AmostraABRIL-AriadneeMarisaREVIS2.utf8.csv
		# 'AmostraAGOSTO - AMOSTRAAGO10003110-2.csv'


	# Cálculo das features dos textos preclassificados
	preclassified_features = get_features(preclassified_corpora)

	# Treinamento do algoritmo
	train_features, test_features = split_features(preclassified_features, split=0.75)
	print('training_features=',len(train_features))
	print('test_features=',len(test_features))


	# ?????

	# 2. Jeito obvio
	# features_treinamento = []
	# for t in texto_classificado:
	# 	text = t[0]
	# 	vote = t[1]
	# 	print('[%s] - [%s]' % (text,vote))
	# 	features_treinamento.append((impeachment_features(text),vote))

	# 3. Jeito pythoniano
	# features_treinamento = [ (impeachment_features(sentence),vote) for (sentence,vote) in texto_classificado ]


	# Criacao e treinamento do do classificador
	classifier = nltk.NaiveBayesClassifier.train(train_features)

	# Verificação da acurácia
	print('accuracy=',nltk.classify.accuracy(classifier, test_features))

	# Listagem das features mais relevantes
	print('most_informative_features=',classifier.most_informative_features())
	print('-------')
	classifier.show_most_informative_features(5)

	# Testes ad-hoc
	# adhoc_classification_tests(classifier)

	# Classificacao da base de dados real
	# classify_text(classifier)


