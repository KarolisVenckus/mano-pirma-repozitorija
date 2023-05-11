# import sqlite3

# # Prisijungimas prie duomenų bazės (arba sukūrimas, jei dar neegzistuoja)
# conn = sqlite3.connect('automobiliai.db')
# c = conn.cursor()

# # Sukuriame lentelę "automobiliai", jei ji dar neegzistuoja
# c.execute('''CREATE TABLE IF NOT EXISTS automobiliai
#              (marke TEXT, modelis TEXT, spalva TEXT, metai INTEGER, kaina REAL)''')

# # Uždaryti prisijungimą prie duomenų bazės
# conn.close()



import sqlite3

def naujas_irasas():
    marke = input("Įveskite automobilio markę: ")
    modelis = input("Įveskite automobilio modelį: ")
    spalva = input("Įveskite automobilio spalvą: ")
    metai = int(input("Įveskite automobilio pagaminimo metus: "))
    kaina = float(input("Įveskite automobilio kainą: "))

    conn = sqlite3.connect('automobiliai.db')
    c = conn.cursor()

    # Įterpiame naują įrašą į duomenų bazę
    c.execute("INSERT INTO automobiliai VALUES (?, ?, ?, ?, ?)",
              (marke, modelis, spalva, metai, kaina))

    conn.commit()
    conn.close()

    print("Automobilis sėkmingai įvestas į duomenų bazę.")

def ieskoti_irasu():
    conn = sqlite3.connect('automobiliai.db')
    c = conn.cursor()

    # Vartotojo įvesti parametrai
    marke = input("Įveskite automobilio markę (palikite tuščią, jei nenorite paieškos pagal šį parametrą): ")
    modelis = input("Įveskite automobilio modelį (palikite tuščią, jei nenorite paieškos pagal šį parametrą): ")
    spalva = input("Įveskite automobilio spalvą (palikite tuščią, jei nenorite paieškos pagal šį parametrą): ")
    metai_nuo = input("Įveskite minimalius automobilio pagaminimo metus (palikite tuščią, jei nenorite apriboti): ")
    metai_iki = input("Įveskite maksimalius automobilio pagaminimo metus (palikite tuščią, jei nenorite apriboti): ")
    kaina_nuo = input("Įveskite minimalią automobilio kainą (palikite tuščią, jei nenorite apriboti): ")
    kaina_iki = input("Įveskite maksimalią automobilio kainą (palikite tuščią, jei nenorite apriboti): ")

    # Sudarome SQL užklausą pagal vartotojo įvestus parametrus
    sql = "SELECT * FROM automobiliai WHERE 1=1"

    if marke:
        sql += f" AND marke = '{marke}'"
    if modelis:
        sql += f" AND modelis = '{modelis}'"
    if spalva:
        sql += f" AND spalva = '{spalva}'"
    if metai_nuo:
        sql += f" AND metai >= {metai_nuo}"
    if metai_iki:
        sql += f" AND metai <= {metai_iki}"
    if kaina_nuo:
        sql += f" AND kaina >= {kaina_nuo}"
    if kaina_iki:
        sql += f" AND kaina <= {kaina_iki}"

    # Atlikti užklausą ir gauti rezultatus
    c.execute(sql)
    results = c.fetchall()

    # Spausdiname rezultatus
    print("Rasti įrašai:")
    for row in results:
        print(row)

    conn.close()
    
while True:
    print("\nPasirinkite veiksmą:")
    print("1 - Įvesti naują automobilio įrašą")
    print("2 - Ieškoti automobilio įrašų")
    print("0 - Baigti programą")
    veiksmas = input("Jūsų pasirinkimas: ")

    if veiksmas == "1":
        naujas_irasas()
    elif veiksmas == "2":
        ieskoti_irasu()
    elif veiksmas == "0":
        break
    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.")