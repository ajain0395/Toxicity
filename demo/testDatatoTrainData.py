#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 23:30:31 2018

@author: ashish
"""

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
'''
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
'''
# csv file name
#labelfile = "toxictest.csv"
labelfile = "test_labels.csv"
datafile = "test.csv"
'''
toxic = open('toxic.txt','w') -> 1
severe_toxic = open('severe_toxic.txt','w') ->2
obscene = open('obscene.txt','w') ->3
threat = open('threat.txt','w') ->4
insult = open('insult.txt','w') ->5
identity_hate = open('identity_hate.txt','w') ->6
non_toxic ->7
'''
# initializing the titles and rows list
fields = []
labels = []
data = []
finaldata = []

# reading csv file
with open(labelfile, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = csvreader.next()

    flag = True
    # extracting each data row one by one
    for row in csvreader:
        #row[1] = removepun(row[1])
        #row[1] = '"' + row[1] + '"'
        #row[1].replace('\n', ' ').replace('\r', '')
        flag22 = True
        '''if(row[1] == '0' and row[6] == '0' and row[5] == '0' and row[4] == '0' and row[3] == '0' and row[2] == '0'):
            continue'''
        for k in range(1,len(row)):
                if(int(row[k]) < 0):
                    flag22 = False
                    break
        if(flag22):
            labels.append(row)
#    # get total number of rows 
    print("Total no. of rows: %d"%(len(labels)))
print "Mylabels ",labels
#outfile = open("out2","w")
#outfile.writelines(labels)

fname = ""

with open(datafile, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = csvreader.next()

    flag = True
    # extracting each data row one by one
    for row in csvreader:
        #row[1] = removepun(row[1])
        #row[1] = '"' + row[1] + '"'
        #row[1].replace('\n', ' ').replace('\r', '')
        if(len(row) > 0):
            data.append(row)
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
    print("Total no. of rows: %d"%(len(data)))
    
print data[0]    
rows = []
c = 0
for lab in labels:
    print c
    c+=1
    for dat in data:
        if(dat[0] == lab[0]):
            #print "Yes"
            row = []
            row.append(dat[0])
            row.append(dat[1])
            for k in range(1,len(lab)):
                row.append(lab[k])
            rows.append(row)
            break

generatenonToxic = False
count = 0;
if(generatenonToxic):
    fname = "trainDatanonToxic2.csv"
else:
    fname = "trainDataToxic2.csv"
with open("testtest.csv", 'w') as writeFile:
    fieldnames = ["id","comment_text","toxic","severe_toxic","obscene","threat","insult","identity_hate"]
    writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
    writer.writeheader()
    writer = csv.writer(writeFile)
    for row in rows:
        list = []
        writer.writerow(row)
        '''
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
            '''
        '''if (len(list) > 0):
            writer.writerow(list)
        '''
    #writer.writerows(csvData)
#dic={}
#stop_words = set(stopwords.words('english'))
#print count
