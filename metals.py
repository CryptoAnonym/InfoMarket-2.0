from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def metals():
    print("Please wait...")

    chrome_options = Options()                  
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    driver.get('https://goldenmark.com/pl/australijski-kangur-1-uncja-zlota/#/282-cennik-1_dzien')
    price_g = driver.find_element_by_xpath("/html/body/main/section[1]/div/div[2]/div/section/div[1]/div/div[3]/div[5]/div[1]/div")
    gold = (price_g.text)


    print("\n***** CENY MONET BULIONOWYCH *****\n")
    print("GOLD 1 OZ: " + gold)
    input("\nEnter, aby kontynuowac.")
