import nltk

def impeachment_features(sentence):
	if 'golpe' in sentence:
		return {'golpe' : True}
	else:
		return {'golpe' : False}


texto_classificado = [	("um homem no ônibus nos perguntou se o motivo de estarmos de preto era o golpe. n saímos c essa intenção, mas n é que encaixa perfeitamente..","contra"),
						("pirando legal na batatinha: 'o golpe é homofóbico e racista'. - paaaaaaaaaaaaara tudo que eu quero… ","pro"),
						("@o_antagonista golpe é isso, ferir a constituição.","contra"),
						("golpe é eu não estar te chupando agora!","pro"),
						("@stf_oficial fracassa perante a sociedade brasileira. #somostodosgolpistas ","pro"),
						("impitma sem crime é golpe ","contra"),]


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

classifier = nltk.NaiveBayesClassifier.train(features_treinamento)

print(classifier.classify(impeachment_features('É golpe')))			# contra
print(classifier.classify(impeachment_features('É impeachment')))	# pro