from random import randint
patterns = ['*','#','.','=']
def cap_pat():
    what,how_much = patterns[randint(0,len(patterns)-1)], randint(3,6)
    print "Enter '"+what+"' "+str(how_much)+" times below:\n"
    if raw_input().strip() == what*how_much: print '\nAuthentication passed :)'
    else: print '\nAuthentication failed :('

# Now you know the secret recipe (^_^)