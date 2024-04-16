import requests

def BTC():
    get_blockchain_info()
    get_fee_estimates()
    wallet_address = input("\nPodaj adres portfela Bitcoi : ")
    get_wallet_balance(wallet_address)
    menu = input("\nEnter by kontynuować lub MENU - aby wrócić. \n")
    if menu.upper() == "MENU":
        pass
    else:
        BTC()



def get_blockchain_info():
    url = "https://blockchain.info/latestblock"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        block_height = data["height"]
        block_hash = data["hash"]
        print("Aktualny blok:")
        print("Wysokość bloku:", block_height)
        print("Hash bloku:", block_hash)
    else:
        print("Nie udało się pobrać danych o bloku.")

def get_fee_estimates():
    url = "https://mempool.space/api/v1/fees/recommended"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        fastest_fee = data["fastestFee"]
        half_hour_fee = data["halfHourFee"]
        hour_fee = data["hourFee"]
        print("\nSzacowane opłaty transakcyjne:\n")
        print("Najszybsza:", fastest_fee, "sat/vB")
        print("30 minut:", half_hour_fee, "sat/vB")
        print("1 godzina:", hour_fee, "sat/vB")
    else:
        print("Nie udało się pobrać szacowanych opłat transakcyjnych.")

def get_wallet_balance(wallet_address):
    url = f"https://blockchain.info/rawaddr/{wallet_address}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx status codes)
        data = response.json()
        final_balance = data["final_balance"]
        print("\nStan salda dla adresu", wallet_address, "wynosi:", final_balance/100000000, "BTC")
    except requests.exceptions.RequestException as e:
        print("Wystąpił błąd podczas próby pobrania danych:")
        print(e)
    except KeyError:
        print("Niepoprawna odpowiedź API. Brak oczekiwanych danych.")


