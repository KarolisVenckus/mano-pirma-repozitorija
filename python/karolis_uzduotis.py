pinigu_tipas = input("Pasirinkite kokia valiuta jus norite iskeisti (Svarams S, Eurams E)! ")
suma = input("Iveskite suma! ")
if pinigu_tipas == "S":
    eurai = float(suma) * 1.14
    print(f"Iskeitus pinigus jum liko {eurai:2f}! ")
elif pinigu_tipas == "E":
    svarai = float(suma) * 0.88
    print(f"Iskeitus pinigus jum liko {svarai:2f}!")
else:
    print(f"Jus ivedete netinkama valiuta. ")

print(f"Aciu kad naudojote mano konverteri! \U0001F600")


ginklas = input("Jus uzpuole monstras! Pasirinkite ginkla! (Kumstis, Kardas arba Lankas): ")
if ginklas == "Kumstis":
    print(f"Jus trenkete monstrui, bet jis nieko nepajuto... \U0001F923")
    print("-------------------Jus pralaimejote!------------------------")
elif ginklas == "Kardas":
    print(f"Jus smogete monstrui kardu, ir jus ji iveikete! \U0001f600")
    print("-------------------Jus laimejote!--------------")
elif ginklas == "Lankas":
    print(f"Jus saunate i monstra su lanku, bet jis pagavo strele ir mete ja i jus... \U0001F606")
    print("---------------------------Jus pralaimejote!----------------------------")
else:
    print(f"Netinkamas ginklo paisirinkimas. ")

print(f"Aciu kad zaidete mano zaidima! \U0001F600")
