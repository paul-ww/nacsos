import os, sys, time, resource, re, gc, shutil
from nltk import ngrams
from multiprocess import Pool
from functools import partial
from mongoengine import *
from urllib.parse import urlparse, parse_qsl
connect('mongoengine_documents')

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BasicBrowser.settings")
django.setup()

from scoping.models import *

import pymongo
from pymongo import MongoClient
#client = MongoClient()
#db = client.documents
#scopus_docs = db.scopus_docs

class scopus_doc(DynamicDocument):
    scopus_id = StringField(required=True, max_length=50, unique=True)
    PY = IntField(required=True)

class similarity(Document):
    wos_ut = StringField(required=True, max_length=50)
    scopus_id = StringField(required=True, max_length=50,unique_with='wos_ut')
    scopus_do = BooleanField(required=True, max_length=50)
    wos_do = BooleanField(required=True, max_length=50)
    do_match = BooleanField()
    jaccard = FloatField()
    py_diff = IntField()

def shingle(text,k):
    
    text = text.lower()
    shingleLength = k
    tokens = text.split()

    shingles = [tokens[i:i+shingleLength] for i in range(len(tokens) - shingleLength + 1) if len(tokens[i]) < 4]
    shingles = ngrams(tokens,k)
    s_set = set()
    for s in shingles:
        s_set.add(s)

    return s_set

def jaccard(s1,s2):
    try:
        return len(s1.intersection(s2)) / len(s1.union(s2))
    except:
        return 0

def compare(d1,dc2):
    django.db.connections.close_all()
    s_docs = scopus_doc.objects.all()
    d1 = s_docs[d1]
    if not hasattr(d1,'shingle'):
        return
    d1.shingle_list = d1.shingle
    d1.shingle = set()
    for li in list(d1.shingle_list):
        d1.shingle.add(tuple(li))
    for d2 in dc2:
        try:
            j = jaccard(d1.shingle,d2.shingle)
            if hasattr(d1,'DO'):
                d1_do = True
            else:
                d1_do = False
            if d2.wosarticle.di is not None:
                d2_do = True
            else:
                d2_do = False
            if d1_do and d2_do:
                if d1.DO == d2.wosarticle.di and len(d1.DO) > 5:
                    match = True
                else:
                    match = False
            else:
                match = False
            try:
                py_diff = d1.PY - d2.PY
            except:
                py_diff = None
            sim = similarity(
                scopus_id=d1.scopus_id,
                wos_ut=d2.UT,
                scopus_do=d1_do,
                wos_do=d2_do,
                do_match=match,
                jaccard=j,
                py_diff=py_diff
            )
            sim.save()
            django.db.connections.close_all()
        except:
            pass



def main():
    docs = []
    s_docs = scopus_doc.objects.all()
    unshingled_s_docs = s_docs.filter(shingle__exists=False)
    print(unshingled_s_docs.count())
    for sd in unshingled_s_docs:
        try:
            sd.shingle = list(shingle(sd.TI,2))
            sd.save()
        except:
            pass
      

    wos_docs = Doc.objects.all()[:10000]
    for wd in wos_docs:
        wd.shingle = shingle(wd.title,2)

    s_docs_i = range(s_docs.count())

    #s_docs_i = range(20)

    pool = Pool(processes=8)
    pool.map(partial(compare,dc2=wos_docs),s_docs_i)
    pool.terminate()
    
    
    

if __name__ == '__main__':
    t0 = time.time()	
    main()
    totalTime = time.time() - t0

    tm = int(totalTime//60)
    ts = round(totalTime-(tm*60),2)

    

    print("done! total time: " + str(tm) + " minutes and " + str(ts) + " seconds")
    print("a maximum of " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000) + " MB was used")
