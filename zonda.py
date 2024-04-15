import requests

daneZonda = requests.get("https://api.zonda.exchange/rest/trading/ticker")

if daneZonda.ok == True:
    dane3 = daneZonda.json()["items"]

    def exchange():
        def zonda(rynek): # wyszukiwarka rynków w zondzie(bitbay)  
            if rynek in dane3:         
                test = dane3[rynek]

                bid = test["highestBid"]
                ask = test["lowestAsk"]
            
            
                print("\nNajwyzsza oferta kupna: " + str(bid)[0:6] + " " + str(rynek)[4:7] )
                print("Najnizsza oferta sprzedazy: " + str(ask)[0:6] + " "+ str(rynek)[4:7] + "\n")
            else:
                print("\nBrak rynku! Sproboj jeszcze raz.")

        print("\n***** Witaj w wyszukiwarce rynkow na gieldzie ZONDA! *****")
        print("        (Rynek wyszukujemy wg schematu: BTC-PLN)     ")
        
        in_data = input("\nPodaj rynek, ktorego szukasz (MENU - aby wrocic): ")

        if in_data.upper() == "MENU":
            pass

        if in_data.upper() != "MENU":
            if len(in_data) == 7:
                if in_data.find("-") != -1:
                    zonda(in_data.upper())

                else :
                    print("\nBledny rynek! Sproboj jeszcze raz.")
            else :
                print("\nBledny rynek! Sproboj jeszcze raz.")
            
            input("\nEnter, aby kontynuowac.")
            exchange()

else:
    print("Connect with Zonda API ERROR!")
