# tee ratkaisu tänne
nimi = input("Kenelle teos omistetaan: ")
tiedoston_nimi = input("Mihin kirjoitetaan: ")
omistuskirjoitus = f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi"

try:
    with open(tiedoston_nimi, 'w') as tiedosto:
        tiedosto.write(omistuskirjoitus)
        print(f"{omistuskirjoitus} on tallennettu {tiedoston_nimi} kansioon onnistuneesti.")
except:
    print("Tiedoston kirjoittaminen epäonnistui.")


