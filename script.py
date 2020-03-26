import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities #this was added
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#for the browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('window-size=1600x900')
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-gpu")
options.add_argument("--dns-prefetch-disable")
options.add_argument("--always-authorize-plugins")
options.add_argument("enable-automation")
options.add_argument("--disable-browser-side-navigation")

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptSslCerts'] = True 
capabilities['acceptInsecureCerts'] = True

#locaton of the chrome driver
#if you need a new vertion of the webcriver, go here: https://chromedriver.chromium.org/downloads
filename = "C:\\Users\\hewbo\\AppData\\Local\\Programs\\Python\\chromedriver.exe"
username = "ADD YOUR USERNAME HERE"
password = "ADD YOUR PASSWORD HERE"
name = "YOUR NAME"
needed_help = "WHAT YOU NEED HELP WITH"

#starting up browser
browser = webdriver.Chrome(options = options,executable_path=filename,desired_capabilities=capabilities)

#going to office hours site
browser.get("https://lobster.eecs.umich.edu/eecsoh/")

#defining maximum wait time for a page to load (make larger for slower internet conections)
wait = WebDriverWait(browser, 10)


#elements of the page
fresh = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'eecs280')))
sign_up = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/div/div[3]/div/div/form/div[1]/div[4]/div/button[1]")
sign_up_name = browser.find_element_by_id("signUpName1")
descrip = browser.find_element_by_id("signUpDescription1")

fresh.click()


time.sleep(1)

web_text = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/div/p/span[3]").text
#*************************************************************************************************************************************************



#*************************************************************************************************************************************************

sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div')))
sign_in.click()

#seeing all the open windows
window_id = browser.window_handles


email = username + "@umich.edu"

#switching to the popup window
browser.switch_to.window(window_id[1])
 
#enter email
test = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type=email]')))
test.send_keys(email)
test.send_keys(Keys.ENTER)

#umich info enter
user = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/form/fieldset/div[1]/div/input')))
user.send_keys(username)
browser.find_element_by_xpath("/html/body/main/div/div/form/fieldset/div[2]/div/input").send_keys(password)
browser.find_element_by_xpath("/html/body/main/div/div/form/fieldset/input").click()


#switching the frame, because the duo element is hidden in a frame
browser.switch_to.frame('duo_iframe')
page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button')))
page.click()

#wait for the page to change
while(browser.current_url == "https://weblogin.umich.edu/cosign-bin/cosign.cgi"):
	continue

#go back to the main window
browser.switch_to.window(window_id[0])

#enter help info
sign_up_name.send_keys(name)
descrip.send_keys(needed_help)


#loop until the button is active
while(not sign_up.is_enabled()):
	fresh.click()

#signup for the queue
sign_up.click()


browser.close()
