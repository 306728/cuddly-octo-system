import string

alower = list(string.ascii_lowercase)
aupper = list(string.ascii_uppercase)

def encryption():
  encrypted = []
  plaintext = input("Please enter plaintext: ")
  
  while not "".join(plaintext.split()).isalpha():
    plaintext = input("The plaintext can only contain alphabets and spaces: ")
  
  integer = False
  
  while not integer:  
    try:
      shift = int(input("Enter number of shifts for Caesar cipher encryption: "))
      integer = True
    except ValueError:
      print("The number of shifts must be an integer.")
  
  for i in range(len(plaintext)):
    if plaintext[i] in alower:
      encrypted.append(alower[(alower.index(plaintext[i]) + shift) % 26])
    elif plaintext[i] in aupper:
      encrypted.append(aupper[(aupper.index(plaintext[i]) + shift) % 26])
    elif plaintext[i] == " ":
      encrypted.append(" ")
  return "Your ciphertext is: " + "".join(encrypted)

def decryption():
  decrypted = []
  ciphertext = input("Please enter plaintext: ")
  
  while not "".join(ciphertext.split()).isalpha():
    ciphertext = input("The ciphertext can only contain alphabets and spaces: ")
  
  integer = False
  
  while not integer:  
    try:
      shift = int(input("Enter number of shifts performed previously: "))
      integer = True
    except ValueError:
      print("The number of shifts must be an integer.")
  
  for i in range(len(ciphertext)):
    if ciphertext[i] in alower:
      decrypted.append(alower[(alower.index(ciphertext[i]) - shift) % 26])
    elif ciphertext[i] in aupper:
      decrypted.append(aupper[(aupper.index(ciphertext[i]) - shift) % 26])
    elif ciphertext[i] == " ":
      decrypted.append(" ")
  return "Your ciphertext is: " + "".join(decrypted)
  

print(encryption())
print(decryption())
