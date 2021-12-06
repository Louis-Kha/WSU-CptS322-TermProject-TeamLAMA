from selenium.webdriver import Chrome
import time

# Student Registration Automation

# working version

### process for the automation of routine tasks
## 1. launch 2 terminals
## 2. one with smile.py, other with StudentLoginTestCase.py (at this point it is just register automation)
## 3. after launching, student will get registered and done

driver = Chrome('C:\chromedriver.exe') # might need to change path here
time.sleep(3)
# opens up main screen
driver.get("http://127.0.0.1:5000/")
# taps student button
time.sleep(1)
student_btn = driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[1]/a").click()
# taps registration button
time.sleep(1)
register_btn = driver.find_element_by_xpath("/html/body/div[2]/p/a").click()
# form fill out 
time.sleep(1)
username = driver.find_element_by_xpath("/html/body/div[2]/form/div/input[1]").send_keys("student1")
wsuid = driver.find_element_by_xpath("/html/body/div[2]/form/div/input[2]").send_keys("1234567890")
firstname = driver.find_element_by_xpath("/html/body/div[2]/form/div/input[3]").send_keys("student")
lastname = driver.find_element_by_xpath("/html/body/div[2]/form/div/input[4]").send_keys("one")
email = driver.find_element_by_xpath("/html/body/div[2]/form/div/input[5]").send_keys("studentone@gmail.com")
address = driver.find_element_by_xpath("/html/body/div[2]/form/div/input[6]").send_keys("testaddress120")
phonenum = driver.find_element_by_xpath("/html/body/div[2]/form/div/input[7]").send_keys("1234567890")
password = driver.find_element_by_xpath("/html/body/div[2]/form/div/input[8]").send_keys("p")
passwordrepeat = driver.find_element_by_xpath("/html/body/div[2]/form/div/input[9]").send_keys("p")
# register btn
time.sleep(1)
register_btn = driver.find_element_by_xpath("/html/body/div[2]/form/input[2]").click()

