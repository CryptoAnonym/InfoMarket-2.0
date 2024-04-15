from nbp import forex_price
from paprika import paprica_price_pln

def cal():
    print(""" \n***** Witaj w kalkulatorze KRYPTO-FIAT ! *****
    \n Wybierz rodzaj wymiany (np. 1):
        1. KRYPTO --> FIAT
        2. FIAT --> KRYPTO
        3. FIAT --> FIAT
        4. KRYPTO --> KRYPTO
    """)

    action = input(" Action (MENU - aby wrocic): ")
    print('')

    if action.upper() == "MENU":
        pass 
    if action.upper() != "MENU":
        if action == "1":
            krypto = input("Podaj kryptowalute (np. BTC) do zamiany: ")
            ktypo_price = paprica_price_pln(krypto.upper())
            fiat = input("Podaj na jaka walute (np. USD) zamieniamy: ")
            
            if fiat.upper() == "PLN":
                ile = input("Ile " + krypto.upper() + " wymieniamy na " + fiat.upper() + ": ")
                wynik_pln = ktypo_price * float(ile)
                print("Otrzymasz: " + str(wynik_pln)[0:8] + " " + str(fiat.upper()))
                
                input("\nEnter aby kontynuowac.")

            else:

                fiat_price = forex_price(fiat.upper())
                dzialanie = ktypo_price / fiat_price
                ile = input("Ile " + krypto.upper() + " wymieniamy na " + fiat.upper() + ": ")
                wynik = dzialanie * float(ile)

                print("Otrzymasz: " + str(wynik)[0:8] + " " + str(fiat.upper()) )
                input("\nEnter aby kontynuowac.")

        elif action == "2":
            fiat1 = input("Podaj walute (np. USD) do zamiany: ")
            fiat_price = forex_price(fiat1.upper())

            krypto1 = input("Podaj na jaka kryptowalute (np. BTC) zamieniamy: ")
            ktypo_price = paprica_price_pln(krypto1.upper())

            if fiat1.upper() == "PLN":
                ile = input("Ile " + fiat1.upper() + " wymieniamy na " + krypto1.upper() + ": ")
                wynik2_pln = float(ile) / ktypo_price 
                print("Otrzymasz: " + str(wynik2_pln)[0:8] + " " + str(krypto1.upper()) )
                input("\nEnter aby kontynuowac.")
            else:
                dzialanie2 = fiat_price / ktypo_price 

                ile = input("Ile " + fiat1.upper() + " wymieniamy na " + krypto1.upper() + ": ")
                wynik2 = dzialanie2 * float(ile)

                print("Otrzymasz: " + str(wynik2)[0:8] + " " + str(krypto1.upper()) )
                input("\nEnter aby kontynuowac.")
        
        elif action == "3":
            fiat3 = input("Podaj walute (np. USD) do zamiany: ")
            fiat_price1 = forex_price(fiat3.upper())
            fiat4 = input("Podaj na jaka walute (np. EUR) zamieniamy: ")
            fiat_price2 = forex_price(fiat4.upper())
            ile = input("Ile " + fiat3.upper() + " wymieniamy na " + fiat4.upper() + ": ")

            if fiat3.upper() == "PLN":
                wynik = float(ile) / fiat_price2

                print("Otrzymasz: " + str(wynik)[0:8] + " " + str(fiat4.upper()) )
                input("\nEnter aby kontynuowac.")

            elif fiat4.upper() == "PLN":
                wynik = float(ile) * fiat_price1

                print("Otrzymasz: " + str(wynik)[0:8] + " " + str(fiat4.upper()) )
                input("\nEnter aby kontynuowac.")

            else:
                dzialanie = float(fiat_price1) / float(fiat_price2) 
                wynik = float(ile) * dzialanie

                print("Otrzymasz: " + str(wynik)[0:8] + " " + str(fiat4.upper()) )
                input("\nEnter aby kontynuowac.")          
        
        elif action == "4":
            krypto3 = input("Podaj kryptowalute (np. BTC) do zamiany: ")
            krypto_price1 = paprica_price_pln(krypto3.upper())
            krypto4 = input("Podaj na jaka kryptowalute (np. ETH) zamieniamy: ")
            krypto_price2 = paprica_price_pln(krypto4.upper())
            ile = input("Ile " + krypto3.upper() + " wymieniamy na " + krypto4.upper() + ": ")
        
            dzialanie = float(krypto_price1) / float(krypto_price2) 
            wynik = float(ile) * dzialanie

            print("Otrzymasz: " + str(wynik)[0:8] + " " + str(krypto4.upper()) )
            input("\nEnter aby kontynuowac.")   

        else: 
            print("\n Bledny wybor. Sproboj jeszcze raz.")
        
        cal()