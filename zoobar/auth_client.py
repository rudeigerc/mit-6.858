from debug import *
from zoodb import *
import rpclib

sys.path.append(os.getcwd())
import readconf

host = readconf.read_conf().lookup_host('auth')

def login(username, password):
    with rpclib.client_connect(host) as c:
        return c.call('login', username=username, password=password)

def register(username, password):
    with rpclib.client_connect(host) as c:
        return c.call('register', username=username, password=password)

def check_token(username, token):
    with rpclib.client_connect(host) as c:
        return c.call('check_token', username=username, token=token)
