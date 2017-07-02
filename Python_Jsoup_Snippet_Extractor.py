from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords
import re



import sys

def extract(s):

    docidList=s.split(":")
    qterm = "The New York Times"
    qterm=qterm.lower().split()
    stops = set(stopwords.words("english"))
    filtered_words = [word for word in qterm if word not in stops]

    reg =''
    for m in filtered_words:
        reg=reg+".*"+m

    reg=reg+".*"
    retList=[]
    for doc in docidList:
        soup = bs(open(doc),"lxml")
        l= soup.body.findAll(text=re.compile(reg,re.I))
        n =[]
        for x in l:
            m = re.search("[A-Za-z0-9.,!/[$]*", x.strip())
            if (m.group(0)!=''):
                n.append(x)
        s=''
        for x in n:
            s = x.strip()+"........."+s

        retList.append(s)

    for x in retList:
        print x

extract("/home/amitd92/solr/NYTimesData/NYTimesDownloadData/82c0270f-6c90-47f6-aedf-0dcc0de129f5.html:/home/amitd92/solr/NYTimesData/NYTimesDownloadData/05aa4d7b-5cc0-45cf-9234-72f4660889f9.html:/home/amitd92/solr/NYTimesData/NYTimesDownloadData/dccf42bf-869a-4d60-be82-0247cb14734b.html:/home/amitd92/solr/NYTimesData/NYTimesDownloadData/d938bef7-1054-4613-a254-5f21fe08e26b.html:/home/amitd92/solr/NYTimesData/NYTimesDownloadData/40667344-afbf-4d9f-ab8c-22f52ca71613.html:/home/amitd92/solr/NYTimesData/NYTimesDownloadData/ace2f5c4-6718-456c-a35e-58f17668cca7.html:/home/amitd92/solr/NYTimesData/NYTimesDownloadData/9e47121e-7d61-45ca-a191-84bb72b768d5.html:/home/amitd92/solr/NYTimesData/NYTimesDownloadData/d7baaa50-9caf-47f0-b922-60a179792b61.html:/home/amitd92/solr/NYTimesData/NYTimesDownloadData/d90910c9-15eb-417b-b12d-949ad97fabb8.html:/home/amitd92/solr/NYTimesData/NYTimesDownloadData/42545f1b-2bf8-4cc2-8f1f-b625e4e0b8b5.html")