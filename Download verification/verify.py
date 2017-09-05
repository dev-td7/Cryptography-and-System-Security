from urllib.request import urlretrieve as ret
import hashlib
import sys

def report(blocknr, blocksize, size):
    global a_file
    prefix = "Downloading "+a_file[0]+": "
    current = blocknr*blocksize
    sys.stdout.write(("{0}%\r"+prefix).format(int(100.0*current/size)))

def check(filePath):
    with open(filePath, 'rb') as f2rb:
        mdv=hashlib.md5()
        while True:
            data=f2rb.read(4096)
            if not data:
                break
            mdv.update(data)
        return mdv.hexdigest()

files = []
with open("files.data") as f:
    while True:
        a_file=f.readline()
        if a_file is '': break
        a_file = a_file.split(',')
        for i in range(0,len(a_file)): a_file[i] = a_file[i].strip()
        files.append(a_file)

print("------------------------------------------------------------------------")
print("\n Verify your downloads with this inbuilt download validator!")
print("\n ---> An application by Tejas & Rushin <----")
print("\n We have following files in our repository:")
i=1
for a_file in files:
    print("\t"+str(i)+". "+a_file[0])
    i+=1

print("\n We would make sure you get the valid file from our repository.\n")
index = input(" I want to download file at _  index\r I want to download file at ")
print()

if index is '':
    print(" No input. About to exit.....")
    _=input(" Press any key to exit.")
elif int(index) > len(files):
    print(" We don't have so many files yet. Work in progress.")
    _=input(" Press any key to exit.")
else:
    file_name = input('Provide a file name (Do not provide extension): ')
    index=int(index)
    a_file = files[index-1]
    ret(a_file[1],file_name+a_file[len(a_file)-1], report)
    print("\n Download finished!\n")
    print(" Starting verification with our secret method..\n")
    valid_md5 = a_file[2]
    calculated_md5 = check(file_name+a_file[len(a_file)-1])
    if valid_md5 == calculated_md5:
        print(" You have the correct copy!")
    else:
        print(" The file seems corrupted!")

print("\n------------------------------------------------------------------------")