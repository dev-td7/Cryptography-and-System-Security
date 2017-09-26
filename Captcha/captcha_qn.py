from random import randint
qa = {'What is last name of Indian Prime Minister?': 'modi', 'Which company manufactures iPhones?': 'apple', 'What is the surname of Tejas?': 'dastane'}
qns = [x for x in qa.keys()]
def ask():
    qn = qns[randint(0,2)]
    if raw_input('\n'+qn+'\n> ').lower() == qa[qn]: print 'Authentication passed :)'
    else: print 'Authentication failed :('