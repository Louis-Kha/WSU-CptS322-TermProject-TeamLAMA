from selenium.webdriver import Chrome
from selenium import webdriver
import time

# Student Login Automation

### process for the automation of routine tasks
## 1. launch 2 terminals
## 2. one with smile.py, other with StudentLoginTestCase.py (at this point it is just register automation)
## 3. after launching, student will get registered and done

# execfile("smile.py")
# subprocess.call("smile.py", shell=True)
driver = Chrome('C:\chromedriver.exe') # might need to change path here
time.sleep(3)
# opens up main screen
driver.get("http://127.0.0.1:5000/")
# taps student button
time.sleep(2)
student_btn = driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[1]/a").click()
# form fill out 
time.sleep(2)
username = driver.find_element_by_xpath("/html/body/div[2]/form/input[2]").send_keys("student1")
password = driver.find_element_by_xpath("/html/body/div[2]/form/input[3]").send_keys("p")
# register btn
time.sleep(2)
login_btn = driver.find_element_by_xpath("/html/body/div[2]/form/input[4]").click()