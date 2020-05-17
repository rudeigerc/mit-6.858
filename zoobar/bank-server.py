#!/usr/bin/env python3
#
# Insert bank server code here.
#

import rpclib
import sys
import bank
import auth_client
from debug import *

class BankRpcServer(rpclib.RpcServer):
    def rpc_init(self, username):
        return bank.init(username)

    def rpc_transfer(self, sender, recipient, zoobars, token):
        if not auth_client.check_token(sender, token) and self.caller != "profile":
            raise PermissionError()
        return bank.transfer(sender, recipient, zoobars)

    def rpc_balance(self, username):
        return bank.balance(username)

    def rpc_get_log(self, username):
        return bank.get_log(username)

if len(sys.argv) != 2:
    print(sys.argv[0], "too few args")

s = BankRpcServer()
s.run_fork(sys.argv[1])
