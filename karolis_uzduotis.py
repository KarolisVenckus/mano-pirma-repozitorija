Pinigu_Tipas = input("Pasirinkite kokia valiuta jus norite iskeisti (Svarams S, Eurams E)! ")
Suma = input("Iveskite suma! ")
if Pinigu_Tipas == "S":
    Eurai = float(Suma) * 1.14
    print(f"Iskeitus pinigus jum liko {Eurai:2f}! ")
elif Pinigu_Tipas == "E":
    Svarai = float(Suma) / 0.88
    print(f"Iskeitus pinigus jum liko {Svarai:2f}!")
else:
    print(f"Jus ivedete netinkama valiuta. ")

print(f"Aciu kad naudojote mano konverteri! \U0001F600")

Ginklas = input("Jus uzpuole monstras! Pasirinkite ginkla! (Kumstis, Kardas arba Lankas): ")
if Ginklas == "Kumstis":
    print(f"Jus trenkete monstrui, bet jis nieko nepajuto... \U0001F923")
elif Ginklas == "Kardas":
    print(f"Jus smogete monstrui kardu, ir jus ji iveikete! \U0001f600")
elif Ginkas == "Lankas":
    print(f"Jus saunate i monstra su lanku, bet jis pagavo strele ir mete ja i jus... \U0001F606")
else:
    print(f"Netinkamas ginklo paisirinkimas. ")

print(f"Aciu kad zaidete mano zaidima! \U0001F600")
