#Enter your custom interval value in seconds. Default: 14400 (4 hours)
interval = 14400
#Enter article id (URL)
articleId = "silber-kaenguru-1-oz-2022"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from threading import Timer

def createDriver():
    options = Options()
    options.add_argument("headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    ser = Service(ChromeDriverManager().install())

    global driver
    driver = webdriver.Chrome(service=ser, options=options)

def writeToFile(value):
    f = open("result.txt", "w")
    f.write(value)
    f.close()

def updateValue():
    driver.get('https://philoro.de/shop/silbermuenzen/' + articleId)

    element = driver.find_element(By.CSS_SELECTOR, "var[data-buyid]")
    price = element.get_attribute('innerHTML')
    
    writeToFile(price)
    print(price)

    Timer(interval, updateValue).start()

createDriver()
updateValue()

