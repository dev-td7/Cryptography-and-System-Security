import urllib
import hashlib


def check(filePath):
    with open(filePath, 'rb') as f2rb:
        mdv=hashlib.md5()
        while True:
            data=f2rb.read(4096)
            if not data:
                break
            mdv.update(data)
        return mdv.hexdigest()


urllib.urlretrieve ("http://www.winmd5.com/download/winmd5free.zip", "winmd5free.zip")
filePath="winmd5free.zip"
md5=check(filePath)
verify="73f48840b60ab6da68b03acd322445ee"
print ("The md5 value of the file is :"+md5)
print ("The verified value of the file is :"+verify)
if md5 == verify:
    print ("True")
else:
    print ("False")
