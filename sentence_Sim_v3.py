from flask import request
from math import sqrt
from math import log10

#function to calcualte similarity score
def calculate_sim(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 1 #both are empty
    elif len(s1) == 0 or len(s2) == 0:
        return 0 #similarity is zero as only one is empty

    s1 = s1.lower()
    s2 = s2.lower()

    ##removing punctuations
    punctuation_list = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for i in punctuation_list:
        if i == '\'' or i == '"':
            #replace with nothing
            s1 = s1.replace(i, "") 
            s2 = s2.replace(i, "")
        else: #replace with space
            s1 = s1.replace(i, " ") 
            s2 = s2.replace(i, " ")
    
    ### REMOVE NON-ALPHABETS
    doc1 = ""
    doc2 = ""

    for ch in s1:
        if ch.isalpha() or ch == " ":
            #allow only alphabet or space
            doc1 = doc1 + ch
    
    for ch in s2:
        if ch.isalpha() or ch == " ":
            #allow only alphabet or space
            doc2 = doc2 + ch

    sentences = [doc1, doc2] #should take only 2 texts to compare

    # transform docs into lists of words
    docs = [l.split() for l in sentences ]

    # print(docs)

    # accept only alphabets
    words = [] # to store words

    all_words = {} #dict
    dict_s1 = {}
    dict_s2 = {}
    cnt = 0
    total_cnt = 0
    doc1_length = 0
    doc2_length = 0

    for d in docs:
        temp = []
        for w in d:
            if len(w) > 2 and w.isalpha(): #discard words <= len 3 or if not an alphabet
                total_cnt += 1
                all_words[w] = all_words.get(w, 0) + 1 #if not present use default val: 0
                temp.append(w)
                if cnt == 0:
                    doc1_length += 1
                    dict_s1[w] = dict_s1.get(w, 0) + 1
                    dict_s2[w] = dict_s2.get(w, 0) #if key doesn't exist then set as 0
                else:
                    doc2_length += 1
                    dict_s2[w] = dict_s2.get(w, 0) + 1
                    dict_s1[w] = dict_s1.get(w, 0) #if key doesn't exist then set as 0
        
        words.append( temp )
        cnt += 1 #change cnt

    
    ##TF - IDF
    #get IDF= total no of doc / DF
    #DF = no. of documents a word is present in
    N = 2
    idf = {} 
    for word in all_words:
        df = 0
        if dict_s1[word] != 0:
            df += 1
        if dict_s2[word] != 0:
            df += 1
        
        idf[word] =  ( N / (df) )
        
    
    tfidf_d1 = {}
    tfidf_d2 = {}

    for word in all_words:
        tfidf_d1[word] = (dict_s1[word] / doc1_length) * (idf[word])
        tfidf_d2[word] = (dict_s2[word] / doc2_length) * (idf[word])

    # print(tfidf_d1, tfidf_d2)

    print("total words", total_cnt) #total words accepted in both sentences
    
    #cal cos sim
    #num = a1*b1 + a2*b2
    #deno = sqrt(a1**2 + a2**2) * sqrt(b1**2 + b2**2)
    num = 0
    deno1 = 0
    deno2 = 0

    # for word in all_words:
    #     num += dict_s1[word] * dict_s2[word]
    #     if word in dict_s1:
    #         deno1 += dict_s1[word] ** 2
    #         # print(dict_s1[key])
    #     if word in dict_s2:
    #         deno2 += dict_s2[word] ** 2

    ### tfidf
    for word in all_words:
        num += tfidf_d1[word] * tfidf_d2[word]
        if word in dict_s1:
            deno1 += tfidf_d1[word] ** 2
            # print(dict_s1[key])
        if word in dict_s2:
            deno2 += tfidf_d2[word] ** 2

    deno = sqrt(deno1) * sqrt(deno2)

    if deno == 0:
        sim = 0
    else:
        sim = num/deno

    if sim >= 0.99999: #to handle exact match
        sim = 1
    
    return sim

##################
if __name__ == "__main__":

    ## take input from user or POST method:
    ## 2 sentences:
    s1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for orangesdfg."
    # s1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
    s2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."

    #extra for now
    s3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."

    # print("Enter or paste first sentence for comparision:")
    # a = input()
    # print("Enter or paste second sentence to compare to:")
    # b = input()


    # print("Similarity Score = ", calculate_sim(a, b) )
    print("Similarity Score = ", calculate_sim(s1, s2) )
