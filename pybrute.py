import sys,pyAesCrypt,time
s=time.time()
b=64*64
dic=sys.argv[1]
fi=sys.argv[2]
out=sys.argv[3]
pas=open(dic,'rb').readlines()
n=0
print('***brute forcing file...***')
total=len(pas)
while True:
    passf=pas[n].strip('\n'.encode('utf-8'))
    try:
        pyAesCrypt.decryptFile(fi,out,passf.decode('utf-8'),b)
        print('  ***file decrypted***')
        e=time.time()
        print('password: {%s}'%passf.decode('utf-8'))
        print('time taken:',e-s)
        print(f'{n/(e-s)} passwords per second')
        sys.exit()
    except Exception:
        n+=1
