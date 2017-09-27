from random import randint
import captcha_text as t, captcha_response as r, captcha_qn as q, captcha_pattern as p
i=randint(0,4)
print '\n--------------------------------------------------------'
print 'iCaptcha'
print '--------------------------------------------------------'
print 'Prove you are a human first.\n'
if i is 1: t.cap_txt()
elif i is 2: r.cap_resp()
elif i is 3: q.ask()
else: p.cap_pat()
print '--------------------------------------------------------'