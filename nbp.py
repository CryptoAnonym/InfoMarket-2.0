import requests

odpNBP = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")

if odpNBP.ok == True:  
    data = odpNBP.json()[0]

    def nbp():

        table = data["table"]
        no = data["no"]
        effectiveDate = data["effectiveDate"]
        rates = data["rates"]

        print("***** KURSY WALUT Z NARODOWEGO BANKU POLSKIEGO *****")
        print("Kursy walut dla: " + "tabela: " + table + " " + "numer: " + no + " " + "data:" + " " + effectiveDate)
        print("")

        in_data = input("Wpisz tiker waluty (ALL - dla wszystkich, MENU - aby wrocic): ")


        if in_data.upper() == "MENU":
            pass
        if in_data.upper() != "MENU":
            if in_data == "all":
                print("")
                for rate in rates:
                    waluta = rate["currency"]
                    tiker = rate["code"]
                    price4 = rate["mid"]
                    print("|"+ tiker + "|" + waluta.upper() + "= "+ str(price4)+ " " + "|PLN|" )
            else:
                for rate in rates:
                    waluta = rate["currency"]
                    tiker = rate["code"]
                    price4 = rate["mid"]
                    if tiker == in_data.upper() :
                        print("\n|"+ tiker + "|" + waluta.upper() + "= "+ str(price4)+ " " + "|PLN|" )
                    else: 
                        continue

            input("\nEnter, aby kontynuowac.")
            nbp()
else:
    print("Connect with NBP API ERROR!")


def forex_price(x):
    rates = data["rates"]
    for rate in rates:
        tiker = rate["code"]
        price4 = rate["mid"]
        if tiker == x:
            return price4


