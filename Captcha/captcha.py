from random import randint
import captcha_text as t
import captcha_response as r
import captcha_qn as q
i=randint(0,10)
if i < 4: t.cap_txt()
elif i < 7: r.cap_resp()
else: q.ask()