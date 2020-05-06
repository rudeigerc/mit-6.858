from debug import *
from zoodb import *
import rpclib

sys.path.append(os.getcwd())
import readconf

host = readconf.read_conf().lookup_host('bank')

def init(username):
    with rpclib.client_connect(host) as c:
        return c.call('init', username=username)

def transfer(sender, recipient, zoobars, token):
    with rpclib.client_connect(host) as c:
        return c.call('transfer', sender=sender, recipient=recipient, zoobars=zoobars, token=token)

def balance(username):
    with rpclib.client_connect(host) as c:
        return c.call('balance', username=username)

def get_log(username):
    with rpclib.client_connect(host) as c:
        return c.call('get_log', username=username)
