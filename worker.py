import multiprocessing as mp
import time
import json
import urllib.request as lb
import ast
from collections import Counter
import operator

def new_worker(id, conn):
    worker = mp.Process(target=main, args=(id, conn,))
    worker.start()
    return worker

def main(id, conn):
    while(True):
        job = conn.blpop('queue:jobs', 0)
        job = json.loads(job[1])
        switch = {
            'count' : count,
            'enum' : enum,
        }
        switch.get(job['op'], -1)(job, conn)

def count(job, conn):
    if not job['result'] :
        count = 0
        try:
            text = lb.urlopen(job['data']).read().decode('utf-8')
            text = split(text, [' ',',','.',';',':','\t','\n',])
            for word in text :
                if word != '':
                    count += 1
        except:
            print(job['data']+' file doesnt exist')
        
        count = {
                'end' : False,
                'result' : count,
            }
        conn.rpush('queue:merge'+str(job['id']),json.dumps(count))

    else :
        result = {
                'end' : True,
                'result' : 0,
            }
        conn.rpush('queue:merge'+str(job['id']),json.dumps(result))
        merged = conn.blpop('queue:merge'+str(job['id']), 0)
        merged = json.loads(merged[1])
        while not merged['end']:
            aux = conn.blpop('queue:merge'+str(job['id']), 0)
            aux = json.loads(aux[1])
            merged['result'] +=(aux['result'])
            merged['end'] = aux['end']
        conn.rpush('queue:result'+str(job['id']),json.dumps(merged))

def enum(job, conn):
    if not job['result'] :
        dict = {}
        try:
            text = lb.urlopen(job['data']).read().decode('utf-8')
            text = split(text, [' ',',','.',';',':','\t','\n',])
            for word in text :
                if word in dict:
                    dict[word] +=1
                else :
                    if word != '':
                        dict[word] = 1
        except:
            print(job['data']+' file doesnt exist')

        enum = {
            'end' : False,
            'result' : dict,
        }
        conn.rpush('queue:merge'+str(job['id']),json.dumps(enum))
    
    else :
        result = {
                'end' : True,
                'result' : {},
            }
        conn.rpush('queue:merge'+str(job['id']),json.dumps(result))
        merged = conn.blpop('queue:merge'+str(job['id']), 0)
        merged = json.loads(merged[1])
        while not merged['end']:
            aux = conn.blpop('queue:merge'+str(job['id']), 0)
            aux = json.loads(aux[1])
            merged['result'] = Counter(merged['result']) + Counter(aux['result'])
            merged['end'] = aux['end']
        merged['result'] = {k: v for k, v in sorted(merged['result'].items(), key=lambda item: item[1])}
        conn.rpush('queue:result'+str(job['id']),json.dumps(merged))

def split(txt, seps):
    default_sep = seps[0]
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]