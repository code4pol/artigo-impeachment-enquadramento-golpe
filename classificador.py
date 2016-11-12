import csv
import nltk
from nltk.classify import apply_features


# 1. Funcao geradora de features
def impeachment_features(sentence):
	if 'golpe' in sentence:
		return {'golpe' : True}
	else:
		return {'golpe' : False}


####################
# 2. Texto pre-classificado para treinamento e testes

# 2.1. Hard coded no codigo
# texto_classificado = [	("um homem no ônibus nos perguntou se o motivo de estarmos de preto era o golpe. n saímos c essa intenção, mas n é que encaixa perfeitamente..","contra"),
# 						("pirando legal na batatinha: 'o golpe é homofóbico e racista'. - paaaaaaaaaaaaara tudo que eu quero… ","pro"),
# 						("@o_antagonista golpe é isso, ferir a constituição.","contra"),
# 						("golpe é eu não estar te chupando agora!","pro"),
# 						("@stf_oficial fracassa perante a sociedade brasileira. #somostodosgolpistas ","pro"),
# 						("impitma sem crime é golpe ","contra"),]


# 2.2. Carregado a partir do CSV
texto_classificado = []
with open('AmostraAGOSTO - AMOSTRAAGO10003110-2.csv', newline='') as csvfile:
	
	# 2.2.1. Ler CSV como Array e acessar os campos atraves de indices: row[0], row[1]...
	# reader = csv.reader(csvfile, delimiter=',', quotechar='"')

	# 2.2.2. Ler como Dict e acessar os campos atraves de chaves: row['nome'], row['endereco']...
	reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

	for row in reader:
		# 2.2.1. 
		# print(row[4],row[5],row[6],row[7])

		# 2.2.2.
		print(row['TEXTO'],row['PRO'],row['CONTRA'],row['INDEFINIDO'])

		if int(row['PRO']):
			opiniao = 'pro'
		elif int(row['CONTRA']):
			opiniao = 'contra'
		else:
			opiniao = 'indefinido' 
		
		# opiniao = True if row['PRO'] else False if row['CONTRA'] else Nil if row['INDEFINIDO']
		
		texto_classificado.append((row['TEXTO'],opiniao))

print('texto_classificado=',texto_classificado)

# 2.3. Lido diretamente a partir do Google Spreadsheet
# TODO (ver gsheet.py)


####################
# 3. Cálculo das features dos textos classificados

# features = [ (impeachment_features(sentence),vote) for (sentence,vote) in texto_classificado ]
# training_features = features[:4]
# test_features = features[4:]

# Pra não colocar tudo na memória
training_features = apply_features(impeachment_features, texto_classificado[:3])
test_features = apply_features(impeachment_features, texto_classificado[3:])

# print('features=',features)
print('training_features=',training_features)
print('test_features=',test_features)

# 1. Exemplo
# [({:},),({:},)]
features_treinamento = [({'golpe':True},'contra'),
						({'golpe':False},'true')]

# 2. Jeito obvio
# features_treinamento = []
# for t in texto_classificado:
# 	text = t[0]
# 	vote = t[1]
# 	print('[%s] - [%s]' % (text,vote))
# 	features_treinamento.append((impeachment_features(text),vote))

# 3. Jeito pythoniano
# features_treinamento = [ (impeachment_features(sentence),vote) for (sentence,vote) in texto_classificado ]

print('features_treinamento',features_treinamento)

# Criacao do classificador
classifier = nltk.NaiveBayesClassifier.train(features_treinamento)

# Teste de duas sentenças
print(classifier.classify(impeachment_features('É golpe')))			# contra
print(classifier.classify(impeachment_features('É impeachment')))	# pro

# Verificação da acurácia
print('accuracy=',nltk.classify.accuracy(classifier, test_features))

classifier.show_most_informative_features(5)


