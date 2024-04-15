import requests

globale = requests.get("https://api.coinpaprika.com/v1/global")

if globale.ok == True:                  
    data5 = globale.json()


    def global_info():
        mCap = (data5["market_cap_usd"] / 1000000000000)
        mCapChange = data5["market_cap_change_24h"]
        mCapAth = (data5["market_cap_ath_value"] / 1000000000000)
        mCapAthDate = data5["market_cap_ath_date"]
        volume24 = (data5["volume_24h_usd"] / 1000000000)
        btcd = data5["bitcoin_dominance_percentage"]

        rATH = mCapAth - mCap
        procentodATH = ((rATH) / (mCapAth) * -100)

        print(" \n Kapitalizacja rynku krypto: " + str(mCap)[0:5] + " BLN USD")
        print(" Zmiana w 24h:  " + str(mCapChange) + " %")
        print(" ATH kapitalizacji:  " + str(mCapAth)[0:5]+ " BLN USD data: " + str(mCapAthDate[0:10]) + " " + str(mCapAthDate[11:19]))
        print(" Zmiana od ATH mCap:  " + str(-rATH)[0:5]+ " BLN USD " + str(procentodATH)[0:5] + " %")
        print(" Volumen mCap 24h:  " + str(volume24)[0:5]+ " MLD USD")
        print(" Dominacja BTC:  " + str(btcd)+ " %")
        input("\nEnter aby kontynuowac.")

else:
    print("Connect with papricacoin/global API ERROR!") 
    input("\nEnter aby kontynuowac.")