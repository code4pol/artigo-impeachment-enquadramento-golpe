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


# Funcao auxiliar
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


	classified_features = get_features(classified_corpora)

	return classified_features

# 2.3. Lido diretamente a partir do Google Spreadsheet
# TODO (ver gsheet.py)

if __name__ == '__main__':

	preclassified_features = load_preclassified_corpora('AmostraAGOSTO - AMOSTRAAGO10003110-2.csv')


	####################
	# 3. Cálculo das features dos textos classificados

	# features = [ (impeachment_features(sentence),vote) for (sentence,vote) in texto_classificado ]
	# training_features = features[:4]
	# test_features = features[4:]

	# Pra não colocar tudo na memória
	# training_features = apply_features(impeachment_features, classified_features[:500])
	# test_features = apply_features(impeachment_features, classified_features[500:])


	train_features, test_features = split_features(preclassified_features, split=0.75)
	print('training_features=',len(train_features))
	print('test_features=',len(test_features))

	# print('features=',features)
	# print('training_features=',training_features)
	# print('test_features=',test_features)

	# 1. Exemplo
	# [({:},),({:},)]
	# features_treinamento = [({'golpe':True},'contra'),
	# 						({'golpe':False},'pro')]

	# 2. Jeito obvio
	# features_treinamento = []
	# for t in texto_classificado:
	# 	text = t[0]
	# 	vote = t[1]
	# 	print('[%s] - [%s]' % (text,vote))
	# 	features_treinamento.append((impeachment_features(text),vote))

	# 3. Jeito pythoniano
	# features_treinamento = [ (impeachment_features(sentence),vote) for (sentence,vote) in texto_classificado ]

	# print('features_treinamento',features_treinamento)

	# Criacao do classificador
	classifier = nltk.NaiveBayesClassifier.train(train_features)

	# Teste de duas sentenças
	# print(classifier.classify(impeachment_features('É golpe')))			# contra
	# print(classifier.classify(impeachment_features('É impeachment')))	# pro

	# Verificação da acurácia
	print('accuracy=',nltk.classify.accuracy(classifier, test_features))

	print('most_informative_features=',len(classifier.most_informative_features()))
	print('-------')
	classifier.show_most_informative_features(5)

	# testes
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

	i = 0
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

