Introdução
==========

Este repositório refere-se a trabalho de pesquisa realizado no âmbito do grupo Resocie do Instituto de Ciência Política da Univesidade de Brasília - IPOL/UnB referente às diferentes formas de enquadramento da palavra "golpe" durante os períodos de votação do processo de impeachment da ex-presidente Dilma.

Overview tecnológico
====================

* Coleta de tweets por meio da API tweepy nos períodos de votação
* Carga dos tweets coletados em um banco MongoDB
* Classificação dos tweets através da biblioteca NLTK

Análise descritiva
===================

Quantitativos
-------------

#### Total de tweets coletados

|Mês|Qtd|
|:--:|--:|
|Abr|359.098|
|Ago|617.303| 
|Set|214.946|
|TOTAL|1.191.347|

#### Quantos são retweets?

|Mês|Qtd|%|
|:--:|--:|:--:|
|Abr|359.098|100%|
|Ago|617.303|100%|
|Set|214.946|100%|
|TOTAL|1.191.347|100%|

Achei estranho isso...

#### Total por Data

|Data|Qtd|
|:---:|---:|
|16/04/2016|100.432|
|17/04/2016|94.160|
|18/04/2016|164.506|
|30/08/2016|165.514|
|13/08/2016|451.789|
|01/09/2016|214.946|

#### Quantidade de Usuários Distintos
```
user.screen_name: 394.914
```
#### Quantidade de Idiomas Distintos (só Abr)
```
lang: 27 (pt,es,und,en,da,fr,tl,de,it,nl,et,cy,cs,sl,lv,pl,lt,tr,ja,in,ht,fi,eu,ro,vi,hu,sv)
```
#### Quantidade de Tweets por Idioma (só Abr)

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
|150.486 (13%)|1.191.347|

### Tweets mais retweetados

#### Tweets mais retweetados, geral

|Qtd Retweets|Usuário|Texto|
|:--:|:--:|:--|
|10344|dilmabr|O golpe é contra o povo e a Nação. É misógino. É homofóbico. É racista. É a imposição da intolerância, preconceito, violência #LutarSempre|
|7170|liliantintori|Que hable la calle, y que hable la calle con gente, y que hable la calle en paz y que hable la calle en democracia. https://t.co/Ed0q5ASztp|
|6810|dilmabr|Um carinhoso abraço a todo povo brasileiro, que compartilha comigo a crença na democracia e o sonho da justiça #LutarSempre|
|4268|CFKArgentina|Se consumó en Brasil el golpe institucional: Nueva forma de violentar la soberanía popular. #dilmarousseff|
|3920|diImabr|Hoje nossa democracia foi ferida. O Brasil perdeu. Eu perdi. Mas eu detestaria estar no lugar dos que me venceram. A luta está só começando.|
|3637|NicolasMaduro|Toda la Solidaridad con @dilmabr y el PueblodeBrasil,condenamos el GolpeOligárquico de la derecha¡Quién Lucha Vence! https://t.co/0MkBrgsTwE|
|3451|ricardope|Tem dois grupos comemorando o GOLPE contra Dilma: os que vão tirar direitos dos trabalhadores e os que ainda não sabem que vão perdê-los.|
|3149|evoespueblo|Condenamos el golpe parlamentario contra la democracia brasileña. Acompañamos a Dilma, Lula y su pueblo en esta hora difícil. #FuerzaDilma|
|3016|dilmabr|O golpe é contra os movimentos sociais e sindicais e contra os que lutam por direitos em todas as suas acepções #LutarSempre|
|2979|leandraleal|Estou extremamente triste e decepcionada com essa farsa. Feliz é aquele que acredita que isso foi justo, que isso ñ é um golpe.|


#### Tweets mais retweetados, mês a mês.

**Abril**

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

**Agosto**

|Qtd Retweets|Usuário|Texto|
|:--:|:--:|:--|
|8362|dilmabr|O golpe é contra o povo e a Nação. É misógino. É homofóbico. É racista. É a imposição da intolerância, preconceito, violência #LutarSempre|
|5449|dilmabr|Um carinhoso abraço a todo povo brasileiro, que compartilha comigo a crença na democracia e o sonho da justiça #LutarSempre|
|3740|diImabr|Hoje nossa democracia foi ferida. O Brasil perdeu. Eu perdi. Mas eu detestaria estar no lugar dos que me venceram. A luta está só começando.|
|3535|CFKArgentina|Se consumó en Brasil el golpe institucional: Nueva forma de violentar la soberanía popular. #dilmarousseff|
|3267|ricardope|Tem dois grupos comemorando o GOLPE contra Dilma: os que vão tirar direitos dos trabalhadores e os que ainda não sabem que vão perdê-los.|
|2743|dilmabr|O golpe é contra os movimentos sociais e sindicais e contra os que lutam por direitos em todas as suas acepções #LutarSempre|
|2718|leandraleal|Estou extremamente triste e decepcionada com essa farsa. Feliz é aquele que acredita que isso foi justo, que isso ñ é um golpe.|
|2621|NicolasMaduro|Toda la Solidaridad con @dilmabr y el PueblodeBrasil,condenamos el GolpeOligárquico de la derecha¡Quién Lucha Vence! https://t.co/0MkBrgsTwE|
|2334|evoespueblo|Condenamos el golpe parlamentario contra la democracia brasileña. Acompañamos a Dilma, Lula y su pueblo en esta hora difícil. #FuerzaDilma|
|2250|evoespueblo|Si prospera golpe parlamentario contra gobierno democrático de @dilmabr, Bolivia convocará a su embajador. Defendamos la democracia y la paz|

**Setembro**

|Qtd Retweets|Usuário|Texto|
|:--:|:--:|:--|
|7170|liliantintori|Que hable la calle, y que hable la calle con gente, y que hable la calle en paz y que hable la calle en democracia. https://t.co/Ed0q5ASztp|
|2578|MichelPesquera|Mi solidaridad y respeto a todos los venezolanos que hoy luchan por su libertad y su democracia enhorabuena!!! https://t.co/iq5Ivsk9rB|
|2023|Albert_Rivera|Todo mi apoyo a los cientos de miles de venezolanos que hoy tomaron Caracas, pidiendo democracia y libertad ¡Fuerza! https://t.co/a6PugU6zs8|
|1982|dilmabr|O golpe é contra o povo e a Nação. É misógino. É homofóbico. É racista. É a imposição da intolerância, preconceito, violência #LutarSempre|
|1884|MariaCorinaYA|Pero este #1S hay una diferencia respecto a 1958: esta será la última dictadura. Vzla conquista la democracia https://t.co/3TKrNCs1Bg|
|1361|dilmabr|Um carinhoso abraço a todo povo brasileiro, que compartilha comigo a crença na democracia e o sonho da justiça #LutarSempre|
|1292|MariaCorinaYA|Pero este #1S hay una diferencia respecto a 1958: esta será la última dictadura. Vzla conquista la democracia https://t.co/rvzkFyi3WI|
|1208|InfoVzlaNet|Grande, grande Venezuela, los paranoicos hablando de golpe violento y el pueblo hablo claro y fuerte PACIFICAMENTE https://t.co/s9GmHKaHoe|
|1063|MariaCorinaYA|Gral @vladimirpadrino, sobre su conciencia descansa paz d la República.Los venezolanos y democracia internac. vigilan respeto a Constitución|
|1039|leandraleal|Se vc acha q artista q é contra o golpe foi comprado pela lei rouanet, 1o #foratemer, 2o pesquise a lei, 3o minha ideologia ñ esta a venda|

#### Quantidade de Tweets por Termos (só Abr)

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

#### Termos mais Recorrentes (só Abr)

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
||852752|
|LutarSempre|35118|
|ImpeachmentDay|19099|
|PelaDemocracia|9530|
|ForaTemer|8291|
|DilmaRousseff|7518|
|1S|7111|
|DilmaFicaGolpeSai|6032|
|dilmarousseff|5735|
|RespeiteAsUrnas|5494|
|Brasil|5441|
|GolpeAquiNãoPassa|5307|
|NoAlGolpeADilma|5267|
|FuerzaDilma|4202|
|impeachmentday|3752|
|ChavismoQuierePaz|3738|
|Impeachment|3620|
|LatinoaméricaConDilma|3597|
|NaoVaiTerGolpe|3447|
|AlutaComeçou|2714|


# Classificação

Testamos a acurácia com diferentes bases de treinamento:

1. AmostraAGOSTO - AMOSTRAAGO10003110-2.csv (Planilha do Google v20161111)
2. AmostraABRIL-AriadneeMarisaREVIS2.utf8.csv
3. AmostraAGOSTOREVIS1411.utf8.csv
4. textos-preclassificados-abril-e-agosto-2016111.csv (AmostraABRIL-AriadneeMarisaREVIS2.xls+AmostraAGOSTOREVIS1411.xls)
5. AmostraABRIL-AriadneeMarisaREDUZIDA.utf8.csv 


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

Lembram que o algoritmo de classificação, na verdade, calcula a probabilidade de cada uma das classes e aponta aquela com maior valor? Pois é, eu somei todas as probabilidades de cada classe. Vejam abaixo. 

|Enquadramento|∑Probabilidade|
|:--|--:|
|CORRUPCAO|60101.098497207546|
|COTIDIANO|40882.65259785218|
|DEMOCRACIA|56122.21306812528|
|ECONOMIA|75491.73388663886|
|HISTORIA|117251.04461587015|
|IDEOLOGIA|82426.73380597659|
|INTERNACIONAL|97365.68430156795|
|MIDIA|44937.85497099285|
|MINORIAS|124484.76946453906|
|MOBILIZACAO|36989.14343670376|
|OFENSAS|46429.29648471466|
|OUTROS|21458.774869916313|

Significa que, no geral, a classe que ganhou maior probabilidade global de enquadramento foi CORRUPCAO, seguida de COTIDIANO etc.

Fiz o mesmo para a classificação sobre o apoio ao impeachment.

|Apoio|∑Probabilidade|
|:--|--:|
|CONTRA|427846.87994303973|
|INDEFINIDO|186325.4502970152|
|PRO|171378.66976033096|


Ainda tem muito o que ser feito, como:

* ~~Agregar os dados também do período de agosto~~
* Ajustar a geração de features pra classificação
* ~~Balancear as quantidades de cada categoria na base de treinamento.~~
 - Não balanceou, mas já deu uma melhorada boa no arquivo `AmostraABRIL-AriadneeMarisaREDUZIDA`. Infelizmente, não impactou no resultado.
* Consultas georeferenciadas
* ~~Confirmar se carga da base de treinamentos está inserindo corpus em mais de uma chave.~~
  - Não estava. Foi corrigido. 
* Refazer testes de acurácia apos correção do item acima.