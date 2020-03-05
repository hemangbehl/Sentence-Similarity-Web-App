# Sentence Similarity Web Application

## Description
This web application takes two sentences as input and gives a similarity score.
Metric used here is cosine similarity. The sentences are parsed and any non-alphabetic characters are discarded. Stopwords are also removed. TF-IDF is also applied on the sentences.
```
Tf-idf = tf * idf
where tf = count of term 't' in the document / no. of words in that document
idf = total no. of documents / document freq
df (document freq) = no. of documents a word is present in
```

## Steps to follow to run the code:
The code can be run via multiple ways:

### (a) Python code
- open a terminal and type *"git clone https://github.com/hemangbehl/Sentence-Similarity-Web-App.git "*
- run the command *"cd simscore"* to enter the folder "simscore"
- run the command *"python sentence_Sim_v3.py"*
- enter the two sentences to compare
- similarity score will be displayed

### (b) Web app using Flask
- open a terminal and type *"git clone https://github.com/hemangbehl/Sentence-Similarity-Web-App.git "*
- run the command *"cd simscore"* to enter the folder "simscore"
- run the command *"python app.py"*
- go to **http://0.0.0.0:5000/** or **http://localhost:5000/** using a web browser
- enter the two sentences to compare
- similarity score will be displayed

### (c) Using Dockerfile from DockerHub
- open a terminal and type *"docker pull hemang18/simscore:latest "*
- run the command *"docker run -d -p 5000:5000 hemang18/simscore"*
- go to **http://0.0.0.0:5000/** using a web browser
- enter the two sentences to compare
- similarity score will be displayed

(if using Docker Toolbox with VirtualBox in Windows, then the web server link would be **http://192.168.99.100:5000/**

## DockerHub Link
https://hub.docker.com/r/hemang18/simscore


## Results of different metrics:

**Results:**

| Tables                | s1 vs s1      | s1 vs s2| s1 vs s3  |
| -------------         |:-------------:|:-----:  |:-----:|
| **Cos sim:**          |  1    | 0.87940  | 0.54524 |
| **cos sim-stopwords:**|  1    | 0.76964  | 0.29852 |
| **TF - cos sim   :**  |  1    | 0.87940  | 0.54524 |
| **TFIDF - cos sim:**  |  1    | 0.67114  | 0.24819 |
| **TFIDF - stopwords:**|  1    | 0.47336  | 0.10211 |

**Sample sentences used:**

s1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."

s2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."

s3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."

## Authors

* **Hemang Behl** - [hemangbehl](https://github.com/hemangbehl) [LinkedIn](https://www.linkedin.com/in/hemangbehl/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
