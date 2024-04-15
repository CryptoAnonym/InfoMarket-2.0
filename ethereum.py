from web3 import Web3
from web3.eth import Eth
from paprika import paprica_price

infura= "https://mainnet.infura.io/v3/2c6b6d6fcb964eee88bc0e2e83c8f654"
web3 = Web3(Web3.HTTPProvider(infura))

nr_bloku = web3.eth.block_number 
gas = web3.eth.gas_price
gwei = gas / 1000000000

def eth():

    eth_price = paprica_price("ETH")
    print("\n***** Witaj w przeglądarce sieci ETHEREUM *****")
    print(" **** Aktualny nr bloku Ethereum: " + str(nr_bloku) +" ****\n")
    print(" Aktualna cena ETH: " + str(eth_price)[0:7] + " |USD|")
    print(" Aktualna cena gazu: " + str(round(gwei, 2)) + " Gwei\n")
 

    def eth_balans(wallet):  

        balance = web3.eth.get_balance(wallet)          #wyszukiwarka adresu
        b_wallet = web3.from_wei(balance, "ether")

        print("\nAdres posiada: " + str(b_wallet) + " ETH" )
    
    def transacion(hash):                               #wyszukiwarka transakcji
        tx = web3.eth.get_transaction(hash)

        from_eth = tx["from"]
        to_eth = tx["to"]
        blockNumber = tx["blockNumber"]
        gas_price = tx["gasPrice"] / 1000000000
        value = tx["value"] / 1000000000000000000

        print("\nFrom: " + str(from_eth))
        print("To: " + str(to_eth))
        print("Block number: " + str(blockNumber))
        print("Gas price: " + str(gas_price) + " Gwei")
        print("Value: " + str(value) + " ETH")

    in_data = input("\nWpisz adres ETH lub hash transakcji (MENU - aby wrocic): ")

    l_znakow = len(in_data)

    if in_data.upper() == "MENU":
        pass

    if in_data.upper() != "MENU":
        if l_znakow == 42:
            eth_balans(in_data)
        elif l_znakow == 66:
            transacion(in_data)
        else:
            print("\nBledna ilosc znakow. Sproboj jeszcze raz.")
        
        input("\nEnter, aby kontynuowac.")
        eth()
    

