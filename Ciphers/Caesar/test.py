import Caesar

print("Ingrese texto a cifrar: ")
text=input()

code=Caesar.encrypt(3, text)
print(code)
print(Caesar.encrypt(-3, code))