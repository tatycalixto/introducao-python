string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

comprimento1 = len(string1)
comprimento2 = len(string2)

print("\nConteúdo das strings:")
print("String 1:", string1)
print("String 2:", string2)

print("\nComprimento das strings:")
print("String 1:", comprimento1)
print("String 2:", comprimento2)

if comprimento1 == comprimento2:
    print("\nAs strings têm o mesmo comprimento.")
    if string1 == string2:
        print("As strings são iguais.")
    else:
        print("As strings são diferentes.")
else:
    print("\nAs strings têm comprimentos diferentes.")
