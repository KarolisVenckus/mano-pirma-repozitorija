import os
while True:
    os.system('clear')
    print("--------[ Musu uber programele ]----------")
    print("1: aidas")
    print("0: iseiti")
    pasirinkimas = input("pasirinkite")
    if pasirinkimas == "0":
        break
    if pasirinkimas == "1":
        tekstas = input("Saukite:")
        print((tekstas+" ") * 3)