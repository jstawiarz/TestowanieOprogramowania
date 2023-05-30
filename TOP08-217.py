from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ==== test automatyczny TOP08-217 =====

# stworzenie instancji Chrome i dodanie opcji headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# ==== TC step 1 - otwarcie strony ====

driver.get("https://todolist.james.am/#/")
 
# czas na załadowanie strony
time.sleep(7)

# ==== TC step 2 - dodaj nowe zadanie ====

new_task = driver.find_element(By.CSS_SELECTOR, "body > ng-view > section > header > form > input")
new_task.send_keys("Zadanie 1")
new_task.send_keys(Keys.RETURN)

# sprawdzenie czy zadanie zostało dodane
try:
    driver.find_element(By.CSS_SELECTOR, "body > ng-view > section > section > ul > li") 
except:
    print("Zadanie nie zostało dodane. Krok 2 nieudany.")

# ==== TC step 3 - oznacz jako zaznaczone ====

checkbox = driver.find_element(By.CSS_SELECTOR, "body > ng-view > section > section > ul > li > div > input")
checkbox.click()

# sprawdzenie czy zakończone
try:
    driver.find_element(By.XPATH, '*//li[@class="ng-scope completed"]')
except:
    print("Zadanie nie zostało oznaczone jako zakończone. Krok 3 nieudany.")


# ==== TC step 4 - odznacz zakończenie ====

checkbox = driver.find_element(By.CSS_SELECTOR, "body > ng-view > section > section > ul > li > div > input")
checkbox.click()

# sprawdzenie czy odznaczone
try:
    driver.find_element(By.XPATH, '*//li[@class="ng-scope"]')
except:
    print("Zadanie nie zostało poprawnie odznaczone jako zakończone. Krok 4 nieudany.")