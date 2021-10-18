from test_framework import generic_test
from test_framework.test_failure import TestFailure
from sortedcontainers import SortedDict

class ClientsCreditsInfo:

    def __init__(self):
        self.credits_to_clients=SortedDict()
        self.clients_to_credits={}
        self.add_alls=0

    def insert(self, client_id: str, c: int) -> None:
        if c not in self.credits_to_clients:
            self.credits_to_clients[c-self.add_alls]=set()
        self.credits_to_clients[c-self.add_alls].add(client_id)
        self.clients_to_credits[client_id]=(c-self.add_alls)
        
        return 

    def remove(self, client_id: str) -> bool:
        # TODO - you fill in here.
        if client_id in self.clients_to_credits:
            c=self.clients_to_credits[client_id]
            del self.clients_to_credits[client_id]
            self.credits_to_clients.get(c).remove(client_id)
            return True
        else:
            return False

    def lookup(self, client_id: str) -> int:
        # TODO - you fill in here.
        if client_id not in self.clients_to_credits:
            return -1
        c=self.clients_to_credits[client_id]
        return c+self.add_alls

    def add_all(self, C: int) -> None:
        # TODO - you fill in here.
        # this will not actually change the order tho so just keep a record of add alls
        self.add_alls+=C
        return

    def max(self) -> str:
        highestkey,cset=max(self.credits_to_clients)
        
        return next(iter(cset))


def client_credits_info_tester(ops):
    cr = ClientsCreditsInfo()

    for x in ops:
        op = x[0]
        s_arg = x[1]
        i_arg = x[2]
        if op == 'ClientsCreditsInfo':
            pass
        if op == 'max':
            result = cr.max()
            if result != s_arg:
                raise TestFailure('Max: return value mismatch')
        elif op == 'remove':
            result = cr.remove(s_arg)
            if result != i_arg:
                raise TestFailure('Remove: return value mismatch')
        elif op == 'insert':
            cr.insert(s_arg, i_arg)
        elif op == 'add_all':
            cr.add_all(i_arg)
        elif op == 'lookup':
            result = cr.lookup(s_arg)
            if result != i_arg:
                raise TestFailure('Lookup: return value mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('adding_credits.py',
                                       'adding_credits.tsv',
                                       client_credits_info_tester))
