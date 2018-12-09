# -*- coding: utf-8 -*-
import csv
import string

from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize

pun = []
pun.append("\n")
pun.append("\r")
pun.append("\t")
'''pun.append("+")
pun.append("-")
pun.append("^M")
pun.append("!")
pun.append("~")
pun.append("/")
pun.append("|")
pun.append("?")
pun.append("!")
'''
#pun.append('"')
#pun.append(",")
for p in string.punctuation:
    if('$' in p or '%' in p or '@' in p or '*' in p or '#' in p or '!' in p or '?' in p):
       print p
       continue
    else:
        pun.append(p)
def removepun(stri):
    for w in pun:
        stri= stri.replace(w, " ").replace("  "," ")
    return stri

# csv file name
filename = "train.csv"
'''
toxic = open('toxic.txt','w') -> 1
severe_toxic = open('severe_toxic.txt','w') ->2
obscene = open('obscene.txt','w') ->3
threat = open('threat.txt','w') ->4
insult = open('insult.txt','w') ->5
non_toxic ->6
identity_hate = open('identity_hate.txt','w')
'''
# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = csvreader.next()

    flag = True
    # extracting each data row one by one
    for row in csvreader:
        row[1] = removepun(row[1])
        row[1] = '"' + row[1] + '"'
        #row[1].replace('\n', ' ').replace('\r', '')
        rows.append(row)
        '''
        if(row[2] == '1'):
            toxic.write(row[1])
        if (row[3] == '1'):
            severe_toxic.write(+row[1]+)
        if (row[4] == '1'):
            obscene.write("|"+row[1]+"|")
        if (row[5] == '1'):
            threat.write("|"+row[1]+"|")
        if (row[6] == '1'):
            insult.write("|"+row[1]+"|")
        if (row[7] == '1'):
            identity_hate.write("|"+row[1]+"|")
        '''
        '''if flag == True:
            print row
            flag = False
        '''
#    # get total number of rows 
    print("Total no. of rows: %d"%(len(rows)))

fname = ""

generatenonToxic = False
count = 0;
if(generatenonToxic):
    fname = "trainDatanonToxic.csv"
else:
    fname = "trainDataToxic.csv"
with open(fname, 'w') as writeFile:
    fieldnames = ["comment","class"]
    writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
    writer.writeheader()
    writer = csv.writer(writeFile)
    for row in rows:
        list = []
        if (row[2] == '1'):
            list = []
            list.append(row[1])
            count +=1
            list.append("toxic")
            writer.writerow(list)
        if (row[3] == '1'):
            list = []
            list.append(row[1])
            list.append("severe_toxic")
            writer.writerow(list)
        if (row[4] == '1'):
            list = []
            list.append(row[1])
            list.append("obscene")
            writer.writerow(list)
        if (row[5] == '1'):
            list = []
            list.append(row[1])
            list.append( "threat")
            writer.writerow(list)
        if (row[6] == '1'):
            list = []
            list.append(row[1])
            list.append("insult")
            writer.writerow(list)
        if (row[7] == '1'):
            list = []
            list.append(row[1])
            list.append("identity_hate")
            writer.writerow(list)
        if(row[7] == '0' and row[6] == '0' and row[5] == '0' and row[4] == '0' and row[3] == '0' and row[2] == '0' and generatenonToxic):
            list = []
            list.append(row[1])
            list.append("non_toxic")
            writer.writerow(list)
        '''if (len(list) > 0):
            writer.writerow(list)
        '''
    #writer.writerows(csvData)
#dic={}
#stop_words = set(stopwords.words('english'))
print count
'''
vocab=[]
dic_id={}
for i in rows:
    for col in range(2,8):
        if i[col]=='1':
            #i[1]=i[1].decode('utf-8').strip()
            try:
                word_tokens = word_tokenize(i[1]) 
                filtered_sentence = [] 
                for w in word_tokens: 
                    w=w.lower()                    
                    if w not in stop_words: 
                        filtered_sentence.append(w) 
                vocab.extend(filtered_sentence)
                try:
                    dic[col].append(" ".join(filtered_sentence))
                    dic_id[col].append(i[0])
                except:
                    dic[col]=[]  
                    dic_id[col]=[]
                    dic_id[col].append(i[0])
                    dic[col].append(" ".join(filtered_sentence))
            except:
                continue
    
vocab=list(set(vocab))
print "hello"
dic_tf={}
dic_vocab={}
lis={}
'''
'''
#import copy
#for wor in vocab:
##    dic_vocab[wor]=0
#dic_test={}
#for i in range(2,8):
#    print i    
#    dic_tf[i]=[]  
#    dic_test[i]={}
#    index=0
#    for com in dic[i]:
##        print com        
##        dic2=copy.deepcopy(dic_vocab)
#        try:        
#            lis={}        
#            word_tokens = word_tokenize(com)
#            for k in word_tokens:
#                lis[k]=word_tokens.count(k)
#                try:                
#                    dic_test[i][k].append(dic_id[i][index])
#                except:
#                    dic_test[i][k]=[]                    
#                    dic_test[i][k].append(dic_id[i][index])
#            dic_tf[i].append(lis)
#            index+=1
#        except:
#            index+=1            
#            continue
#        
#dic_tfidf={}
#for i in range(2,8):
#    dic_tfidf[i]=[]        
#    for index in range(0,len(dic_tf[i])):
#        com=dic_tf[i][index]
#        l={}
#        for w in com.keys():
#            l[w]=dic_tf[i][index][w]*(1/float(len(dic_test[i][w])))
#        dic_tfidf[i].append(l)
'''
'''
import json
with open("tfidf.json",'w') as f:
    json.dump(dic_tfidf,f)
'''
