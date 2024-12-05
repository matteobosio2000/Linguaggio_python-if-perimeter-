import math

def calcola_perimetro():
    print("Scegli la figura geometrica per calcolare il perimetro:")
    print("1. Quadrato")
    print("2. Rettangolo")
    print("3. Triangolo")
    print("4. Cerchio")
    scelta = input("Inserisci il numero corrispondente alla figura: ")

    if scelta == "1":
        lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        perimetro = 4 * lato
        print(f"Il perimetro del quadrato è: {perimetro}")


    elif scelta == "2":
        base = float(input("Inserisci la lunghezza della base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        perimetro = 2 * (base + altezza)
        print(f"Il perimetro del rettangolo è: {perimetro}")


    elif scelta == "3":
        lato1 = float(input("Inserisci la lunghezza del primo lato del triangolo: "))
        lato2 = float(input("Inserisci la lunghezza del secondo lato del triangolo: "))
        lato3 = float(input("Inserisci la lunghezza del terzo lato del triangolo: "))
        perimetro = lato1 + lato2 + lato3
        print(f"Il perimetro del triangolo è: {perimetro}")
  

    elif scelta == "4":
        raggio = float(input("Inserisci la lunghezza del raggio del cerchio: "))
        perimetro = 2 * math.pi * raggio
        print(f"La circonferenza del cerchio è: {perimetro}")


    else:
        print("Scelta non valida. Riprova!")

# Chiamata alla funzione
calcola_perimetro()

