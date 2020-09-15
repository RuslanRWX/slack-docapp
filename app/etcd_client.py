import etcd3
#ETCDCTL_API=3
import os

if os.environ['ETCD_SERVER']:
    etcd = etcd3.client(host=os.environ['ETCD_SERVER'], port=2379)
else:
    etcd = etcd3.client()

#etcd = etcd3.client()
#etcd = etcd3.client(host='127.0.0.1', port=2379, ca_cert=CA_PATH, cert_key=KEY_PATH, cert_cert=CERT_PATH)

#etcd = etcd3.client('10.0.221.1', 2379) #, cert=(CERT_PATH, KEY_PATH), verify=CA_PATH)
#etcd.version()

def put_etcd(key, data):
    try:
        etcd.put(key, data)
        text="I have added \n"+"Key: "+key+"\n Document:\n"+data+"\nThank you!"
        return text
    except:
        return "ERROR PUT"
     

def get_etcd(key):
    return etcd.get(key)[0]


def help_doc():
    data=[m.key.decode('UTF-8') for (_, m) in etcd.get_all()]
    help_text = "\n/doc ".join(data)
    return "HELP documentation keys:\n/doc "+help_text


def delete_etcd(key):
    etcd.delete(key)
    return key+" has been delete"

