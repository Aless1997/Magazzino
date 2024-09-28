from repo import add, read

while True:
    print("Scegli una delle seguenti opzioni:\n")
    scelta = input("1)Inserisci articolo a magazzino.\n2)Leggi il magazzino.\n3)Esci.\n")

    if scelta == "1":
        num = int(input("Quanti articoli vuoi inserire?\n"))
        for x in range(num):
            print("Hai Scelto di aggiungere articoli a magazzino:")
            print()
            add()
            
    if scelta == "2":
        print("Hai Scelto di leggere il magazzino:")
        print()
        read()

    if scelta == "3":
        print("Arrivederci")
        break   
