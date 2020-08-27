#dseral@gmail.com
#PATRICK JUSU CEASER CIPHER CRYPT APP.   
# we need 2 helper mappings, from letters to ints and the inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

# Number of shift count(n) 
key = int(input('Enter the secret key: '))
plaintext = (input("Enter the text you would like to cipher:"))

# encipher
ciphertext = ""
for c in plaintext.upper():
    if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
    else: ciphertext += c

# decipher
plaintext2 = ""
for c in ciphertext.upper():
    if c.isalpha(): plaintext2 += I2L[ (L2I[c] - key)%26 ]
    else: plaintext2 += c

print(plaintext)
print(ciphertext)
print(plaintext2)

input("press enter to close")
