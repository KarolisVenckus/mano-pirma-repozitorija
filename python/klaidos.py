# try:
#     sk1 = float(input("Įveskite pirmą skaičių: "))
#     sk2 = float(input("Įveskite antrą skaičių: "))
#     dalmuo = sk1 / sk2
#     print("Skaičių dalmenys yra:", dalmuo)
# except ValueError:
#     print("Įvestas neteisingas reikšmės tipas. Prašome įvesti skaičių.")
# except ZeroDivisionError:
#     print("Dalinti iš nulio negalima.")


while True:
    try:
        skaicius = float(input("Įveskite teigiamą skaičių: "))
        if skaicius > 0:
            break
        else:
            print("Įveskite teigiamą skaičių!")
    except ValueError:
        print("Klaida! Įveskite teigiamą skaičių.")