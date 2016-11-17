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

Testamos a acurácia com diferentes bases de treinamento:

1. AmostraAGOSTO - AMOSTRAAGO10003110-2.csv
2. AmostraABRIL-AriadneeMarisaREVIS2.utf8.csv
3. AmostraAGOSTOREVIS1411.utf8.csv
4. textos-preclassificados-abril-e-agosto-2016111.csv (AmostraABRIL-AriadneeMarisaREVIS2.xls+AmostraAGOSTOREVIS1411.xls)
5. AmostraABRIL-AriadneeMarisaREDUZIDA.utf8.csv (Planilha do Google v20161111)


## Classificação em termos de Apoio

#### Testes de Acurácia

|Base de Treinamento|#Pros|#Contras|#Indiferente|Acurácia|
|:--|--:|--:|--:|:--:|
|1|133|655|195|49.39%|
|2|166|667|137|65.98%|
|3|137|656|188|49.59%|
|4|303|1323|325|48.26%|
|5|167|267|137|60.41%|

#### Classificação com arquivo 2

|Cenário|# Textos|Tempo|# Pró|# Contra|# Indefinido|
|:--|--:|:--:|--:|--:|--:|
|Todos os tweets de Abr|359.098|17:16.73|49.778 (14%)|254.180 (71%)|55.140 (15%)|
|Todos de Abr só os com 'golp'|247.839|04:08.84|40.366 (16%)|162.769 (66%)|44.704 (18%)|
|Abr+Ago só os com 'golp'|785.551|14:13.94|143.891 (18%)|505.791 (64%)|135.869 (17%)|

## Classificação em termos de Enquadramento

#### Testes de Acurácia

|Base|#Dem|#Eco|#Min|#Cor|#Int|#Ide|#Cot|#Mid|#His|#Mob|#Ofe|#Out|Acurácia|
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|:--:|
|1|211|28|22|52|45|134|91|73|57|46|0|224|14.00%|
|2|187|34|20|68|52|36|76|59|39|129|52|218|14.69%|
|3|204|30|22|51|47|46|88|67|66|44|106|210|17.26%|
|4|391|64|42|119|99|82|164|126|105|173|158|428|17.69%|
|5|103|22|10|40|27|22|64|28|19|60|37|139|16.43%|

#### Classificação com arquivo 4

|Cenário|Total de Twets|Total Classificado ('golp')|
|:--|--:|--:|
|Só Abr|359.098|247.839|
|Abr+Ago|1.191.347|803.941|

Distribuição da classe de maior probabilidade:

|Classe|Só Abr|Abr+Ago|
|:--:|--:|--:|
|MINORIAS|60.953|139.852|
|INTERNACIONAL|32.456|140.105|
|HISTORIA|31.128|119.381|
|ECONOMIA|21.834|57.723|
|MOBILIZACAO|18.867|33.089|
|IDEOLOGIA|18.729|93.549|
|OUTROS|16.664|12.280|
|DEMOCRACIA|13.913|93.549|
|COTIDIANO|12.000|41.251|
|OFENSAS|7.511|263.90|
|MIDIA|7.376|26.158|
|CORRUPCAO|6.408|46.472|

Ainda tem muito o que ser feito, como:

* ~~Agregar os dados também do período de agosto~~
* Ajustar a geração de features pra classificação
* ~~Balancear as quantidades de cada categoria na base de treinamento.~~
 - Não balanceou, mas já deu uma melhorada boa no arquivo `AmostraABRIL-AriadneeMarisaREDUZIDA`. Infelizmente, não impactou no resultado.
* Consultas georeferenciadas
* ~~Confirmar se carga da base de treinamentos está inserindo corpus em mais de uma chave.~~
  - Não estava. Foi corrigido. 
* Refazer testes de acurácia apos correção do item acima.