import datetime
from os import environ
from telnetlib import EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#<option value="198179">09:00 AM - 10:00 AM</option>
#<option value="198180">10:00 AM - 11:00 AM</option>
#<option value="198181">11:00 AM - 12:00 PM</option>
#<option value="198182">12:00 PM - 01:00 PM</option>
#<option value="198183">01:00 PM - 02:00 PM</option>
#<option value="198185">03:00 PM - 04:00 PM</option>
#<option value="198186">04:00 PM - 05:00 PM</option>
#<option value="198187">05:00 PM - 06:00 PM</option>
#<option value="198188">06:00 PM - 07:00 PM</option>
#<option value="198189">07:00 PM - 08:00 PM</option>
#<option value="198190">08:00 PM - 09:00 PM</option>
#<option value="198191">09:00 PM - 10:00 PM</option>

def Booking():

    today = date.today()
    d1 = today.strftime("%m/%d/%Y")
    NxtWeek = today + datetime.timedelta(days=7)
    w1 = NxtWeek.strftime("%m/%d/%Y")
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    try:
        driver.get("Website")
        driver.find_element(By.XPATH,'//*[@id="Username"]').send_keys("username")
        driver.find_element(By.XPATH,'//*[@id="Password"]').send_keys("password")
        driver.find_element(By.XPATH,'//*[@id="loginBtn"]').click()
        sleep(2)
        driver.find_element(By.XPATH,'//*[@id="StartDate"]').click()
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").send_keys(Keys.DELETE).key_up(Keys.CONTROL).send_keys(w1).send_keys(Keys.ENTER).perform()
        #DateInput = driver.find_element(By.XPATH,'//*[@id="StartDate"]')
        #DateInput.clear()
        #driver.find_element(By.XPATH,'//*[@id="StartDate"]').send_keys(w1)
        sleep(1)
        select_element = driver.find_element(By.ID, 'SelectedAmenityTimeSlotID')
        select_object = Select(select_element)
        #select_object.select_by_value("198190")
        select_object.select_by_visible_text('09:00 AM - 10:00 AM')
        #sleep(5)
        driver.find_element(By.XPATH,'//*[@id="btnBookNow"]').click()
        sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(By.XPATH, '//*[@id="divStep1Details"]/div[4]/input').click()
        sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(By.XPATH,'//*[@id="SignatureDisclaimer"]').click()
        driver.find_element(By.XPATH,'//*[@id="FullNameInSignature"]').send_keys("kasra")
        driver.find_element(By.XPATH,'//*[@id="savebtn"]').click()
        sleep(2)
        driver.find_element(By.XPATH,'//*[@id="bookingform2"]/div[3]/input').click()

        print("Booked Successfully")

    except:
        print("Booking Failed")

    finally:
        driver.quit()


if __name__ == '__main__':
    Booking()