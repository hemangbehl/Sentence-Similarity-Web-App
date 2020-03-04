from math import sqrt

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

    stopwords = set(["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"])

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
            if w not in stopwords: #discard stopwords
            # if len(w) > 2 and w not in stopwords: #discard stopwords
            # if len(w) > 2:
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

    
    ## #TF - IDF
    ## get IDF= total no of doc / DF
    ## DF = no. of documents a word is present in
    N = 2
    idf = {} 
    for word in all_words:
        df = 0
        if dict_s1[word] != 0:
            df += 1
        if dict_s2[word] != 0:
            df += 1
        
        idf[word] =  ( N / (df) )   #log 10  removed as no. of documents is too small
        
    ### TFIDF
    tfidf_d1 = {}
    tfidf_d2 = {}

    for word in all_words:
        tfidf_d1[word] = (dict_s1[word] / doc1_length) * (idf[word])
        tfidf_d2[word] = (dict_s2[word] / doc2_length) * (idf[word])
    
    # tf_d1 = {}
    # tf_d2 = {}
    # for word in all_words:
    #     tf_d1[word] = (dict_s1[word] / doc1_length)
    #     tf_d2[word] = (dict_s2[word] / doc2_length)
    
    #cal cos sim
    #num = a1*b1 + a2*b2
    #deno = sqrt(a1**2 + a2**2) * sqrt(b1**2 + b2**2)
    num = 0
    deno1 = 0
    deno2 = 0

    # ### #simple term count - similar to TF
    # for word in all_words:
    #     num += dict_s1[word] * dict_s2[word]
    #     if word in dict_s1:
    #         deno1 += dict_s1[word] ** 2
    #     if word in dict_s2:
    #         deno2 += dict_s2[word] ** 2

    # ### tf
    # for word in all_words:
    #     num += tf_d1[word] * tf_d2[word]
    #     if word in dict_s1:
    #         deno1 += tf_d1[word] ** 2
    #     if word in dict_s2:
    #         deno2 += tf_d2[word] ** 2

    ### TFIDF
    for word in all_words:
        num += tfidf_d1[word] * tfidf_d2[word]
        if word in dict_s1:
            deno1 += tfidf_d1[word] ** 2
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

if __name__ == "__main__":

    ## 2 sentences:
    # s1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
    # s2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
    
    # #extra for now
    # s3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."
    # print("Similarity Score = ", calculate_sim(s1, s2) )

    ## take input from user:
    print("Enter or paste first sentence for comparision:")
    a = input()
    print("Enter or paste second sentence to compare to:")
    b = input()

    print("Similarity Score = ", calculate_sim(a, b) )


    '''
    Results:
                        s1 vs s1       s1 vs s2     s1 vs s3
    Cos sim        :    1            0.87940         0.54524
    cos sim-stopwords:  1            0.76964         0.29852
    TF - cos sim   :    1            0.87940         0.54524
    TFIDF - cos sim:    1            0.67114         0.24819
    TFIDF-stopwords:    1            0.47336         0.10211

    '''