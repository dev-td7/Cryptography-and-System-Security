from random import randint
def calc(op1, op, op2):
    if op is '+': return op1+op2
    if op is '-': return op1-op2
    if op is '*': return op1*op2
def cap_resp():
    a,b,op=randint(1,10),randint(1,10),['+','-','*'][randint(0,2)]
    r=calc(a,op,b)
    if input('\nPlease authenticate the transaction\n\n'+str(a)+' '+str(op)+' '+str(b)+' = ') == r: print 'Authentication passed :)'
    else: print 'Authentication failed :('