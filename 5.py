from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
import time

adresler= "0x66a6Bd6D2c28a7413F22bf26F4030D3f46C3400a"

a= 1
found_nmbr=0
number = int(input("Please enter the number: "))
start = time.time()

for x in range (number):

    time1 = time.time() - start
    private_key = keccak_256(token_bytes(32)).digest()
    public_key= PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr= keccak_256(public_key).digest()[-20:].hex()
    public_address="0"+addr

    public_address = "0x66a6Bd6D2c28a7413F22bf26F4030D3f46C3400a"
    aranan_varmi = adresler.find(public_address)
    if aranan_varmi != -1:
        print("Lun tay char gaye")
        findings = open("pattay.txt", "a" )
        findings.write (private_key.hex() + "  " + public_address + "\n")
        findings.close()
        print("private_key    :     : " + private_key.hex() )
        print("Address        :     : " + public_address )
        time.sleep =(3)
        found_nmbr = found_nmbr+1
    else:
        print(" " + private_key.hex() + " - " + public_address + '\t' + str(a)+  " Founded = " + str(found_nmbr))
        a+=1
print("total time %s second" %time1)




