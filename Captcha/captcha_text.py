from random import randint
def cap_txt():
    r1,r2,i,captcha_str=randint(3,10),randint(1,10),0,''
    while i<r1:
        if r2<6: captcha_str+=str(randint(0,9))
        else: captcha_str+=chr(randint(65,65+25))
        i,r2=i+1,randint(1,10)
    if raw_input('\nEnter the characters as seen here -> '+captcha_str+'\n> ') == captcha_str: print '\nAuthentication passed :)'
    else: print '\nAuthentication failed :('