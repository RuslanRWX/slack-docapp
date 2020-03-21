from flask import request, jsonify
from .etcd_client import *
import re

def get_doc():
    #data = request.json
    #return jsonify(data)
    #return jsonify(request.form.to_dict())
    #return 'Hi '+request.values['user_name']+'\nAre you ready?\n'+request.values['text']
    #key=request.values['text'].split()
    #return key[0]
    return get_etcd(request.values['text'])
    #return get_etcd('testval')

def put_doc():
    #data = request.json
    #return jsonify(data)
    #return jsonify(request.form.to_dict())
    #return 'Hi '+request.values['user_name']+'\nAre you ready?\n'+request.values['text']
    #key=request.values['text'].split()
    #key2=request.values['text'].splitlines(keepends=True)
    key=re.split('(\W)', request.values['text'])
    #print(type(' '.join(str(e) for e in key[1:1000])))
    #return key[0]
 #   return put_etcd(key[0], ' '.join(str(e) for e in key[1:1000]))
   # return key
    return put_etcd(key[0], ' '.join(str(e) for e in key[1:]))
   # #return get_etcd('testval')

