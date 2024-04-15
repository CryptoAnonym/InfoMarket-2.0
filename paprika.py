import requests
from nbp import forex_price

crypto = requests.get("https://api.coinpaprika.com/v1/tickers")

if crypto.ok == True:              
    data = crypto.json()

    def paprika():

        print("\n***** DANE KRYPTOWALUT Z COINPAPRIKA.COM *****")
        print("***** Wyszukiwanie tikerze (np. BTC) *****")
        print("")
        in_data = input("Wpisz tiker waluty (MENU - aby wrocic): ")
        
        def papricaAll(crypt):          
            i = 0
            while i <= 100:
                if i < 100:
                    z = data[i]
                    name = z["name"]
                    tiker = z["symbol"]
                    rank = z["rank"]
                    supply = z["total_supply"]
                    maxSuplay = z["max_supply"]
                    akk = z["last_updated"]
                    i += 1 
                    cos = z["quotes"]
                    cos2 = cos["USD"]
                    price = cos2["price"]

                    mCapTiker = cos2["market_cap"] / 1000000000
                    ath_price = cos2["ath_price"]
                    ath_date = cos2["ath_date"]
                    percent_from_price_ath= cos2["percent_from_price_ath"]
                        
                    change24 = cos2["market_cap_change_24h"]
                    change1 = cos2["percent_change_1h"]
                    change7 = cos2["percent_change_7d"]
                    change30 = cos2["percent_change_30d"]
                    changeY = cos2["percent_change_1y"]

                    if tiker == str(crypt): # or name == str(crypt) :
                        usd_price = forex_price("USD")
                        pln = usd_price * price

                        print("\n|"+ tiker + "|" + " "+ name + " = "+ str(price)[0:8] +" " + "|USD| / " +  str(pln)[0:8] +  " |PLN|") 
                        
                        print("\nAktualizacja: "+ str(akk[0:10]) + " " + str(akk[11:19]) + "\nRanking nr: " + str(rank) +  "\n Zmiana ceny w ostatnim czasie: ")
                        print(" * 1h: " + str(change1) + " %" +  "\n * 24h: " + str(change24)+ " %"  + "\n * 7d: " + str(change7) 
                            + " %" + "\n * 30d: " + str(change30)+ " %"+ "\n * 1y: " + str(changeY)+ " %" )
                        print("Market: " + str(mCapTiker)[0:5] + " MLD USD" + "\nATH: " + str(ath_price)[0:6] + " USD" + "\n ATH data: " + ath_date[0:10] + "\n Od ATH: " + str(percent_from_price_ath) + " %" )
                        print("Monet w obrocie: " + str(supply) + "\n 0 = Brak danych")

                        print("Maxymalna podaż: " + str(maxSuplay) + "\n 0 = Nieskończona")
                        break
                else:
                    print("\nBledna waluta. Sprobuj jesszcze raz.")
                    break
        
        if in_data.upper() == "MENU":
            pass
        if in_data.upper() != "MENU":
            papricaAll(in_data.upper())
            input("\nEnter, aby kontynuowac.")
            paprika()

else:
    print("Connect with COINPAPRIKA API ERROR!")
    
def paprica_price_print(crypt):         
            i = 0
            while i <= 100:
                if i < 100:
                    z = data[i]
                    name = z["name"]
                    tiker = z["symbol"]
                    rank = z["rank"]
                    supply = z["total_supply"]
                    maxSuplay = z["max_supply"]
                    akk = z["last_updated"]
                    i += 1 
                    cos = z["quotes"]
                    cos2 = cos["USD"]
                    price = cos2["price"]

                    mCapTiker = cos2["market_cap"] / 1000000000
                    ath_price = cos2["ath_price"]
                    ath_date = cos2["ath_date"]
                    percent_from_price_ath= cos2["percent_from_price_ath"]
                        
                    change24 = cos2["market_cap_change_24h"]
                    change1 = cos2["percent_change_1h"]
                    change7 = cos2["percent_change_7d"]
                    change30 = cos2["percent_change_30d"]
                    changeY = cos2["percent_change_1y"]

                    if tiker == str(crypt): # or name == str(crypt) :
                        usd_price = forex_price("USD")
                        pln = usd_price * price

                        print("|"+ tiker + "|" + " "+ name + " = "+ str(price)[0:8] + " |USD|") 
                        print("|"+ tiker + "|" + " "+ name + " = "+ str(pln)[0:8] +  " |PLN|")
                        break

def paprica_price(crypt):          
            i = 0
            while i <= 100:
                if i < 100:
                    z = data[i]
                    name = z["name"]
                    tiker = z["symbol"]
                    i += 1 
                    cos = z["quotes"]
                    cos2 = cos["USD"]
                    price = cos2["price"]

                    if tiker == str(crypt): # or name == str(crypt) :
                        usd_price = forex_price("USD")
                        pln = usd_price * price

                        return price
                        break

def paprica_price_pln(crypt):          
            i = 0
            while i <= 100:
                if i < 100:
                    z = data[i]
                    name = z["name"]
                    tiker = z["symbol"]
                    i += 1 
                    cos = z["quotes"]
                    cos2 = cos["USD"]
                    price = cos2["price"]

                    if tiker == str(crypt): # or name == str(crypt) :
                        usd_price = forex_price("USD")
                        pln = usd_price * price

                        return pln
                        break
