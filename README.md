# Sentence Smialrity Web Application

#### Dataset
Sample dataset files have been provided in the "/datasets" folder.

Dataset link: 
https://www.kaggle.com/neferfufi/lastfm


#### Major Dependencies:
The following tools and packages need to be installed:
Spark, Keras, Python 3.6

#### Steps to follow to run the code:
1) Install the following packages:
   datetime, surprise ,sklearn, implicit, keras, itertools,
   findspark,pyspark, mllib.recommendation.ALS, mllib.recommendation.MatrixFactorizationModel, 
   mllib.recommendation.Rating   
2) Change the path of the dataset file from where its reading
3) Run the program using Anaconda Jupiter notebook

#### Folder structure
/: contains 

#### DockerHub Link

#### Results of different metrics:

Results:
					s1 vs s1       s1 vs s2     s1 vs s3
Cos sim        :    1            0.87940         0.54524
cos sim-stopwords:  1            0.76964         0.29852
TF - cos sim   :    1            0.87940         0.54524
TFIDF - cos sim:    1            0.67114         0.24819
TFIDF-stopwords:    1            0.47336         0.10211

s1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
s2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
s3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."
