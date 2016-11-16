Introdução
==========

Este repositório refere-se a trabalho de pesquisa realizado no âmbito do grupo Resocie do Instituto de Ciência Política da Univesidade de Brasília - IPL/UnB referente às diferentes formas de enquadramento da palavra "golpe" durante os períodos de votação do processo de impeachment da ex-presidente Dilma.

Overview tecnológico
====================

* Coleta de tweets por meio da API tweepy nos períodos de votação
* Carga dos tweets coletados em um banco MongoDB
* Classificação dos tweets através da biblioteca NLTK

Análise descritiva
===================

**!!! ATENÇÃO !!!** 
> Análise preliminar apenas do período referente à votação na Câmara dos Deputados.

Quantitativos
-------------

#### Total de tweets coletados

|Mês|Qtd|
|:--:|--:|
|Abr|359.098|
|Ago|   | 

#### Quantos são retweets?

|Mês|Qtd|%|
|:--:|--:|:--:|
|Abr|359.098|100%|
|Ago|   | |


#### Total por Data

|Data|Qtd|
|:---:|---:|
|16/04/2016|100.432|
|17/04/2016|94.160|
|18/04/2016|16.4506|

#### Quantidade de Usuários Distintos
```
user.screen_name: 140.247
```
#### Quantidade de Idiomas Distintos
```
lang: 27 (pt,es,und,en,da,fr,tl,de,it,nl,et,cy,cs,sl,lv,pl,lt,tr,ja,in,ht,fi,eu,ro,vi,hu,sv)
```
#### Quantidade de Tweets por Idioma

|Idoma|Qtd|
|:-----:|:---:|
|pt|239.968|
|es|113.556|
|und|4.369|
|en|522|
|da|25|
|fr|121|
|tl|58|
|de|47|
|it|222|
|nl|3|
|et|4|
|cy|42|
|cs|7|
|sl|7|
|lv|2|
|pl|4|
|lt|4|
|ja|34|
|tr|33|
|in|26|
|ht|18|
|fi|1|
|eu|7|
|ro|12|
|vi|1|
|hu|4|
|sv|1|

No entanto, nem todos os tweets seguem o idioma presente na proporiedade `lang`. 

<details><summary>Exemplo:</summary><p>
```
{
	"_id" : ObjectId("5828533ea6e51390b3cac0ee"),
	"created_at" : "Mon Apr 18 19:30:24 +0000 2016",
	"id" : NumberLong("722145272797659140"),
	"id_str" : "722145272797659140",
	"text" : "RT @pdevechi: Haja mortadela!! https://t.co/9JawQ1zyaO",
	(…)
	"user" : {
		"id" : 14692201,
		"id_str" : "14692201",
		"name" : "Fabio Moraes ن",
		"screen_name" : "fabiomoraes",
		(…)
	},
	"geo" : null,
	"coordinates" : null,
	"place" : null,
	"contributors" : null,
	"retweeted_status" : {
		"created_at" : "Mon Apr 18 19:22:39 +0000 2016",
		"id" : NumberLong("722143323670970369"),
		"id_str" : "722143323670970369",
		"text" : "Haja mortadela!! https://t.co/9JawQ1zyaO",
		(…)
		"user" : {
			"id" : 114356391,
			"id_str" : "114356391",
			"name" : "Joga Bosta no Xico",
			"screen_name" : "pdevechi",
			(…)
		},
		"geo" : null,
		"coordinates" : null,
		"place" : null,
		"contributors" : null,
		"quoted_status_id" : NumberLong("722142904660176896"),
		"quoted_status_id_str" : "722142904660176896",
		"quoted_status" : {
			"created_at" : "Mon Apr 18 19:20:59 +0000 2016",
			"id" : NumberLong("722142904660176896"),
			"id_str" : "722142904660176896",
			"text" : "Boulos: golpe terá 'resistência popular intransigente' | Brasil 24/7 https://t.co/QUydboQCCT via @brasil247",
			(…)
			"user" : {
				"id" : 248890506,
				"id_str" : "248890506",
				"name" : "Brasil 247",
				"screen_name" : "brasil247",
				(…)
			},
			"geo" : null,
			"coordinates" : null,
			"place" : null,
			"contributors" : null,
			"is_quote_status" : false,
			"retweet_count" : 0,
			"favorite_count" : 0,
			"entities" : {
				(…)
			},
			"favorited" : false,
			"retweeted" : false,
			"possibly_sensitive" : false,
			"filter_level" : "low",
			"lang" : "pt"
		},
		"is_quote_status" : true,
		"retweet_count" : 1,
		"favorite_count" : 1,
		"entities" : {
			(…)
		},
		"favorited" : false,
		"retweeted" : false,
		"possibly_sensitive" : false,
		"filter_level" : "low",
		"lang" : "sv"
	},
	"is_quote_status" : true,
	"retweet_count" : 0,
	"favorite_count" : 0,
	"entities" : {
		(…)
	},
	"favorited" : false,
	"retweeted" : false,
	"possibly_sensitive" : false,
	"filter_level" : "low",
	"lang" : "sv",                    <---------------------
	"timestamp_ms" : "1461007824502",
}

```
</p></details>

#### Quantidade de Tweets Distintos que foram retweetados

|Tweets Originais|Retweets|
|---:|--:|
|57.858|359.098|

#### Tweets mais retweetados

|Qtd Retweets|Usuário|Texto|
|:--:|:--:|:--|
|1562|luscas|golpe é o q eu gasto com xerox todo mes|
|1490|hramosallup|Régimen moribundo tilda d \"golpe a la democracia brasileña\" juicio a Dilma Rousseff. Resto combo (Ortega,Evo,Correa y castros)no ha opinado.|
|1304|hramosallup|Ganó Brasil. Poco a poco la democracia latinoamericana va diluyendo sus pesadillas.|
|1178|EugenioDerbez|Ahora la naturaleza golpeó a nuestros hermanos de Ecuador, mis oraciones están con ustedes 🙏🏼|
|1157|jeanwyllys_real|\"Em nome da população LGBT, do povo negro exterminado nas periferias, dos trabalhadores da cultura, dos sem-teto/terra, voto NÃO AO GOLPE!\"|
|1116|matheuss_pe|ATENÇÃO!!!! NOVO GOLPE NA PRAÇA!!!! https://t.co/xjF1jMkidU|
|1073|dukechargista|Uma dúvida: o \"Tchau, Querida\" se refere à Dilma ou a Democracia?|
|1004|evoespueblo|No al golpe congresal. Defendamos la democracia del Brasil, su liderazgo regional y la estabilidad de América Latina.|
|925|diImabr|PRONUNCIAMENTO À NAÇÃO CONTRA O GOLPE!\nhttps://t.co/SO4umYBhwT|
|809|RitaLisauskas|O cara foi no microfone, dedicou o voto ao torturador-mor de 64, louvou o golpe de 2016 e cês tão chocados é com o cuspe? Esse país tá louco|

#### Quantidade de Tweets por Termos

|Termo|Qtd|
|:--|--:|
|golp|171.140|
|golpe|166.924|
|golpistas|3.603|
|demo|97.133|
|democr|94.114|
|democracia|91.318|
|democr.*golp|7.022|
|golp.*democr|10.645|

#### Termos mais Recorrentes

|Termo|Qtd|
|:--:|--:|
|de|184.008|
|a|133.356|
|o|128.919|
|golpe|128.591|
|que|92.818|
|e|81.227|
|la|70.977|
|democracia|70.484|
|é|60.104|
|da|55.557|
|do|54.606|
|contra|50.385|
||49.224|
|en|46.026|
|no|43.262|
|não|40.166|
|Brasil|36.361|
|y|34.788|
|el|33.794|
|em|31.785|
|se|29.344|
|por|28.667|
|O|27.312|
|para|27.225|
|um|25.710|
|un|25.366|
|Golpe|24.900|
|na|24.429|
|Dilma|24.064|
|vai|23.370|
|es|23.123|
|com|20.387|
|pela|19.892|
|A|18.010|
|los|17.390|
|ter|16.973|
|q|16.948|
|ao|16.024|
|dos|15.676|
|GOLPE|15.573|

#### Hashtags mais Recorrentes

|Hashtag|Qtd
|:--:|--:|
||267.687|
|DilmaFicaGolpeSai|6.032|
|RespeiteAsUrnas|5.494|
|GolpeAquiNãoPassa|5.307|
|NoAlGolpeADilma|5.261|
|ImpeachmentDay|3.885|
|NaoVaiTerGolpe|3.429|
|AlutaComeçou|2.714|
|Impeachment|2.712|
|Brasil|2.072|
|GolpeAquiNaoPassa|1.871|
|ElMundoConDilma|1.639|
|ALutaComeçou|1.483|
|NãoVaiTerGolpe|1.223|
|OBrasilPrecisa|770|
|ForaDilmaFueraMaduro|675|
|InternetJusta|492|
|BrasilContraOGolpe|491|
|ALutaContinua|470|
|ondeOsFracosNaoTêmVez|464|


# Classificação

Foram realizadas até o momento 4 ciclos de classificação. Cada um com diferentes bases de treinamento:

|Base de Treinamento|#Pros|#Contras|#Indiferente|Acurácia|
|:--|--:|--:|--:|:--:|
|Planilha do Google v20161111|655|133|195|49.39%|
|AmostraABRIL-AriadneeMarisaREVIS2.xls|166|667|137|65.98%|
|AmostraAGOSTOREVIS1411.xls|137|656|188|49.59%|
|AmostraABRIL-AriadneeMarisaREVIS2.xls+AmostraAGOSTOREVIS1411.xls|303|1323|325|48.26%|

Vamos utilizar apenas o arquivo `AmostraABRIL-AriadneeMarisaREVIS2.xls` para fazer a classificação.

|# Textos|Tempo|# Pró|# Contra|# Indefinido|
|--:|:--:|--:|--:|--:|
|359.098|17:16.73|49.778|254.180|55.140|