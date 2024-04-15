
import time
from info import global_info
from zonda import exchange
from nbp import nbp, forex_price
from ethereum import eth
from paprika import paprika, paprica_price_print
from cal import cal
from metals import metals


while True:
  print("=======================================================")
  print("============= infoMarket terminal version =============")
  print("=========== Start: %s ===========" % time.ctime())

  print("""
    info - ogolne informacje o rynku
    paprika - informacje o krypto z serwisu coinpaprica
    zonda - wyszukiwarka rynkow na gieldzie ZONDA
    nbp - kursy walut z Narodowego Banku Polskiego
    eth - przeglad sieci Ethereum
    cal - kalkulator wymian (krypto-fiat, krypto-krypto, fiat-fiat)
    exit - wyjscie

    """)

  paprica_price_print("BTC")
  print("|USD| Dolar Amerykański = " +str(forex_price("USD")) + " |PLN|\n")

  action = input("Action: ")

  if action.upper() == "ZONDA":
    exchange()
  elif action.upper() == "INFO":
    global_info()
  elif action.upper() == "NBP":
    nbp()
  elif action.upper() == "ETH":
    eth()
  elif action.upper() == "PAPRIKA":
    paprika()
  elif action.upper() == "CAL":
    cal()
  elif action.upper() == "EXIT":
    break
  #elif action.upper() == "METALS":
    #metals()
  else:
    print("\nERROR! Bledna komenda. Sproboj jeszcze raz. ")
    
