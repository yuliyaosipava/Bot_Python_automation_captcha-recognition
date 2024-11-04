from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instantiate the WebDriver
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Load the target page
captcha_page_url = "https://visa.vfsglobal.com/blr/en/pol/login"
#driver.get(captcha_page_url)

options = Options()
browser = uc.Chrome(executable_path=r"c:\Python311\Lib\site-packages\chromedriver_binary\chromedriver.exe", options=options)
browser.get(captcha_page_url)

WebDriverWait(browser, 600).until(EC.presence_of_element_located((By.ID, "mat-input-0")))
time.sleep(1)
browser.find_element(by=By.ID, value="mat-input-0").send_keys('tratra@gmail.com')
browser.find_element(by=By.ID, value="mat-input-1").send_keys('trutru!')   

# Solve the Captcha
print("Solving Captcha")
solver = TwoCaptcha("0633d04a720972d48853559b37cc31c9")
response = solver.recaptcha(sitekey='6LdJReUUAAAAAPR1hddg-9JUC_TO13OrlKVpukHL', url=captcha_page_url, version='v3')
code = response['code']
print(f"Successfully solved the Captcha. The solve code is {code}")

# Set the solved Captcha
#recaptcha_response_element = browser.find_element(By.ID, 'g-recaptcha-response')
time.sleep(5)
#browser.find_element(By.ID, value="rc-anchor-container").click()
browser.find_element(By.ID, "rc-anchor-container").click()
time.sleep(5)

# Submit the form
submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[class="mat-focus-indicator btn mat-btn-lg btn-block btn-brand-orange mat-stroked-button mat-button-base ng-star-inserted"]')
submit_btn.click()



browser.execute_script(f'arguments[0].value = "{code}";', recaptcha_response_element)
#print(recaptcha_response_element)
# Submit the form
#time.sleep(5)
browser.find_element(By.XPATH, "//button/span[contains(text(),' Sign In')]").click()
   
time.sleep(5)
# Pause the execution so you can see the screen after submission before closing the driver
input("Press enter to continue")
def suppress_exception_in_del(uc):
    old_del = uc.Chrome.__del__

    def new_del(self) -> None:
        try:
            old_del(self)
        except:
            pass
    
    setattr(uc.Chrome, '__del__', new_del)

suppress_exception_in_del(uc) 
