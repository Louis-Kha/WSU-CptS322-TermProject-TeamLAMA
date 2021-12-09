import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep

# How to run
# 1 cd into tests
# 2 in the cmd type: python -m unittest selenium_unittests.py

# User fixure
@pytest.fixture
def user1():
    return  {'username':'faculty1@wsu.edu', 
             'wsuID':'1234567890',
             'firstname':'f',
             'lastname':'l',
             'email':'f@wsu.edu', 
             'address':'fjdfru4t4gurjgr',
             'phonenum':'234567890',
             'password':'a',
             'wpassword':'wp'}

# User fixure
# Faculty
@pytest.fixture
def user2():
    return  {'username':'fclt@wsu.edu', 
             'email':'fclt@wsu.edu', 
             'password':'a'}

# User fixures
@pytest.fixture
def user3():
    return  {'username':'student1@wsu.edu', 
             'wsuID':'0123456789',
             'firstname':'s',
             'lastname':'l',
             'email':'s@wsu.edu', 
             'address':'4ut7ug8figirjgtg',
             'phonenum':'11234567890',
             'password':'b',
             'wpassword':'wp'}

# User fixures
@pytest.fixture
def user4():
    return  {'username':'studentappr@wsu.edu', 
             'wsuID':'012345678900',
             'firstname':'ss',
             'lastname':'ll',
             'email':'ss@wsu.edu', 
             'address':'4ut7ug8figirjgtgtg',
             'phonenum':'1123456789001',
             'password':'b',
             'wpassword':'wp'}

@pytest.fixture
def user5():
    return  {'username':'studentapplyw@wsu.edu', 
             'wsuID':'01234567890011',
             'firstname':'sss',
             'lastname':'lll',
             'email':'sss@wsu.edu', 
             'address':'4ut7ug8figirjgtgtgtt',
             'phonenum':'112345678900112',
             'password':'b',
             'wpassword':'wp'}

@pytest.fixture
def browser(): # configured correctly
    opts = Options()
    opts.headless = True # change to false to display stuff
    driver = webdriver.Chrome(options=opts, executable_path = 'C:\chromedriver.exe')
    driver.implicitly_wait(10)
    yield driver
    # For cleanup, quit the driver
    driver.quit()

### Failed Registrations --works--
def test_faculty_failed_register_form(browser,user2): 
    # tests need to fail because not enough info is provided for faculty
    browser.get('http://127.0.0.1:5000/Facultyregister')
    browser.find_element_by_name("username").send_keys(user2['username'])
    sleep(1)
    browser.find_element_by_name("email").send_keys(user2['email'])
    sleep(1)
    browser.find_element_by_name("password1").send_keys(user2['password'])
    sleep(1)
    browser.find_element_by_name("password2").send_keys(user2['password'])    
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    content = browser.page_source
    assert 'Faculty Register' in content

def test_student_failed_register_form(browser,user2): 
    # tests need to fail because not enough info is provided for student
    browser.get('http://127.0.0.1:5000/register')
    browser.find_element_by_name("username").send_keys(user2['username'])
    sleep(1)
    browser.find_element_by_name("email").send_keys(user2['email'])
    sleep(1)
    browser.find_element_by_name("password1").send_keys(user2['password'])
    sleep(1)
    browser.find_element_by_name("password2").send_keys(user2['password'])    
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    content = browser.page_source
    assert 'Register' in content

# ### Successful Registrations
def test_faculty_success_register_form(browser,user1): # works!!!!
    # should succeed
    browser.get('http://127.0.0.1:5000/Facultyregister')
    browser.find_element_by_name("username").send_keys(user1['username'])
    sleep(1)
    browser.find_element_by_name("wsuID").send_keys(user1['wsuID'])
    sleep(1)
    browser.find_element_by_name("firstName").send_keys(user1['firstname'])
    sleep(1)
    browser.find_element_by_name("lastName").send_keys(user1['lastname'])
    sleep(1)
    browser.find_element_by_name("email").send_keys(user1['email'])
    sleep(1)
    browser.find_element_by_name("address").send_keys(user1['address'])
    sleep(1)
    browser.find_element_by_name("phoneNumber").send_keys(user1['phonenum'])
    sleep(1)
    browser.find_element_by_name("password1").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("password2").send_keys(user1['password'])    
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    content = browser.page_source
    assert 'You are now a registered user' in content

def test_student1_success_register_form(browser,user3): # works!!!!
    # should succeed
    browser.get('http://127.0.0.1:5000/register')
    browser.find_element_by_name("username").send_keys(user3['username'])
    sleep(1)
    browser.find_element_by_name("wsuID").send_keys(user3['wsuID'])
    sleep(1)
    browser.find_element_by_name("firstName").send_keys(user3['firstname'])
    sleep(1)
    browser.find_element_by_name("lastName").send_keys(user3['lastname'])
    sleep(1)
    browser.find_element_by_name("email").send_keys(user3['email'])
    sleep(1)
    browser.find_element_by_name("address").send_keys(user3['address'])
    sleep(1)
    browser.find_element_by_name("phoneNumber").send_keys(user3['phonenum'])
    sleep(1)
    browser.find_element_by_name("password1").send_keys(user3['password'])
    sleep(1)
    browser.find_element_by_name("password2").send_keys(user3['password'])    
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    content = browser.page_source
    assert 'You are now a registered user' in content

def test_student2_success_register_form(browser,user4): # works!!!!
    # should succeed
    browser.get('http://127.0.0.1:5000/register')
    browser.find_element_by_name("username").send_keys(user4['username'])
    sleep(1)
    browser.find_element_by_name("wsuID").send_keys(user4['wsuID'])
    sleep(1)
    browser.find_element_by_name("firstName").send_keys(user4['firstname'])
    sleep(1)
    browser.find_element_by_name("lastName").send_keys(user4['lastname'])
    sleep(1)
    browser.find_element_by_name("email").send_keys(user4['email'])
    sleep(1)
    browser.find_element_by_name("address").send_keys(user4['address'])
    sleep(1)
    browser.find_element_by_name("phoneNumber").send_keys(user4['phonenum'])
    sleep(1)
    browser.find_element_by_name("password1").send_keys(user4['password'])
    sleep(1)
    browser.find_element_by_name("password2").send_keys(user4['password'])    
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    content = browser.page_source
    assert 'You are now a registered user' in content

def test_student3_success_register_form(browser,user5): # works!!!!
    # should succeed
    browser.get('http://127.0.0.1:5000/register')
    browser.find_element_by_name("username").send_keys(user5['username'])
    sleep(1)
    browser.find_element_by_name("wsuID").send_keys(user5['wsuID'])
    sleep(1)
    browser.find_element_by_name("firstName").send_keys(user5['firstname'])
    sleep(1)
    browser.find_element_by_name("lastName").send_keys(user5['lastname'])
    sleep(1)
    browser.find_element_by_name("email").send_keys(user5['email'])
    sleep(1)
    browser.find_element_by_name("address").send_keys(user5['address'])
    sleep(1)
    browser.find_element_by_name("phoneNumber").send_keys(user5['phonenum'])
    sleep(1)
    browser.find_element_by_name("password1").send_keys(user5['password'])
    sleep(1)
    browser.find_element_by_name("password2").send_keys(user5['password'])    
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    content = browser.page_source
    assert 'You are now a registered user' in content

# ### Failed Logins
# Invalid Username or Password
def test_student_fail_login_1(browser,user3): # no username provided
    browser.get('http://127.0.0.1:5000/login')
    browser.find_element_by_name("password").send_keys(user3['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    content = browser.page_source
    assert 'Student Sign In' in content

def test_student_fail_login_2(browser,user3): # wrong password provided
    browser.get('http://127.0.0.1:5000/login')
    browser.find_element_by_name("username").send_keys(user3['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user3['wpassword'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    content = browser.page_source
    assert 'Invalid Username or Password' in content

def test_faculty_fail_login_1(browser,user1): # no username provided
    browser.get('http://127.0.0.1:5000/FacultyLogin')
    browser.find_element_by_name("password").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    content = browser.page_source
    assert 'Faculty Sign In' in content

def test_faculty_fail_login_2(browser,user1): # wrong password provided
    browser.get('http://127.0.0.1:5000/FacultyLogin')
    browser.find_element_by_name("username").send_keys(user1['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user1['wpassword'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    content = browser.page_source
    assert 'Invalid Username or Password' in content

### Successfull logins/logouts --works all above--
def test_student_success_loginlogout(browser,user3): 
    browser.get('http://127.0.0.1:5000/login')
    browser.find_element_by_name("username").send_keys(user3['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user3['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[3]/a").click()
    content = browser.page_source
    assert 'Student Sign In' in content

def test_faculty_success_loginlogout(browser,user1): 
    browser.get('http://127.0.0.1:5000/FacultyLogin')
    browser.find_element_by_name("username").send_keys(user1['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[4]/a").click()
    content = browser.page_source
    assert 'Faculty Sign In' in content

### Main page redirect testing
def test_student_mainpage(browser,user3):  # error
    browser.get('http://127.0.0.1:5000/login')
    browser.find_element_by_name("username").send_keys(user3['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user3['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[1]/a").click()
    content = browser.page_source
    assert 'Student Index - ResearchApp' in content

def test_faculty_mainpage(browser,user1): 
    browser.get('http://127.0.0.1:5000/FacultyLogin')
    browser.find_element_by_name("username").send_keys(user1['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(5)
    browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[2]/a").click()
    content = browser.page_source
    assert 'Faculty Main Page - ResearchApp' in content

## Display Profile testing --works--
def test_student_dprofile(browser,user3): 
    browser.get('http://127.0.0.1:5000/login')
    browser.find_element_by_name("username").send_keys(user3['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user3['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[2]/a").click()
    content = browser.page_source
    assert 'User Profile - ResearchApp' in content

# webelement time=driver.findElement(By.id("input_name")).getAttribute("value");

def test_faculty_dprofile(browser,user1): 
    browser.get('http://127.0.0.1:5000/FacultyLogin')
    browser.find_element_by_name("username").send_keys(user1['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[3]/a").click()
    content = browser.page_source
    assert 'User Profile - ResearchApp' in content

## Edit profile information 
# Changes have been saved.
def test_student_eprofile_fail(browser,user3): # no password provided
    browser.get('http://127.0.0.1:5000/login')
    browser.find_element_by_name("username").send_keys(user3['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user3['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[2]/a").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/p[16]/a").click()
    sleep(1)
    browser.find_element_by_name("submit").click()
    content = browser.page_source
    assert 'Edit Profile - ResearchApp' in content

def test_student_eprofile_success(browser,user3): 
    browser.get('http://127.0.0.1:5000/login')
    browser.find_element_by_name("username").send_keys(user3['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user3['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[2]/a").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/p[16]/a").click()
    sleep(1)
    browser.find_element_by_name("gradDate").send_keys("11111111")
    sleep(1)
    browser.find_element_by_name("cumGPA").send_keys("4.0")
    sleep(1)
    browser.find_element_by_name("techCourseGPA").send_keys("4.0")
    sleep(1)
    browser.find_element_by_name("experienceDesc").send_keys("Testing desc")
    sleep(1)
    browser.find_element_by_name("password").send_keys(user3['password'])
    sleep(1)
    browser.find_element_by_name("password2").send_keys(user3['password'])
    sleep(1)
    browser.find_element_by_name("userMajors").click()
    sleep(1)
    browser.find_element_by_name("userTechnicalCourses").click()
    sleep(1)
    browser.find_element_by_name("rFieldTags").click()
    sleep(1)
    browser.find_element_by_name("knownLang").click()
    sleep(1)
    browser.find_element_by_name("submit").click()
    content = browser.page_source
    assert 'Changes have been saved.' in content


def test_faculty_eprofile_fail(browser,user1): # no password provided
    browser.get('http://127.0.0.1:5000/FacultyLogin')
    browser.find_element_by_name("username").send_keys(user1['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[3]/a").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/p[8]/a").click()
    sleep(1)
    browser.find_element_by_name("submit").click()
    content = browser.page_source
    assert 'Edit Profile - ResearchApp' in content

def test_faculty_eprofile_success(browser,user1): 
    browser.get('http://127.0.0.1:5000/FacultyLogin')
    browser.find_element_by_name("username").send_keys(user1['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[3]/a").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/p[8]/a").click()
    sleep(1)
    browser.find_element_by_name("password").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("password2").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    content = browser.page_source
    assert 'Changes have been saved.' in content

# Faculty create a research position
def test_newposition_fail(browser,user1): # one of the inputs is missing
    browser.get('http://127.0.0.1:5000/FacultyLogin')
    browser.find_element_by_name("username").send_keys(user1['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[1]/a").click()
    sleep(1)
    browser.find_element_by_name("researchDesc").send_keys('test description')
    sleep(1)
    browser.find_element_by_name("submit").click()
    content = browser.page_source
    assert 'New Research Position - ResearchApp' in content

def test_newposition_success(browser,user1): # New Research Position Has Been Created!
    browser.get('http://127.0.0.1:5000/FacultyLogin')
    browser.find_element_by_name("username").send_keys(user1['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[1]/a").click()
    sleep(1)
    browser.find_element_by_name("title").send_keys('test title')
    sleep(1)
    browser.find_element_by_name("researchDesc").send_keys('test description')
    sleep(1)
    browser.find_element_by_name("researchFields").send_keys('test research fields')
    sleep(1)
    browser.find_element_by_name("requiredQualifications").send_keys('test qualifications')
    sleep(1)
    browser.find_element_by_name("startDate").send_keys('11111111')
    sleep(1)
    browser.find_element_by_name("endDate").send_keys('2222222')
    sleep(1)
    browser.find_element_by_name("requiredHours").click()
    sleep(1)
    browser.find_element_by_name("requiredHours").click()
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    content = browser.page_source
    assert 'New Research Position Has Been Created!' in content

## Student position application
def test_applyposition_fail(browser,user3): # one of the inputs is missing
    # Apply To Research Position Page
    browser.get('http://127.0.0.1:5000/login')
    browser.find_element_by_name("username").send_keys(user3['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user3['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr[2]/td[2]/div[8]/form/input").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div[2]/form/input").click()
    sleep(1)
    browser.find_element_by_name("name").send_keys(user3['username'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    content = browser.page_source
    assert 'Apply To Research Position Page' in content

def test_applyposition_success1(browser,user3): # New Research Position Has Been Created!
    # You Have Successfully Applied To A New Position!
    browser.get('http://127.0.0.1:5000/login')
    browser.find_element_by_name("username").send_keys(user3['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user3['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr[2]/td[2]/div[8]/form/input").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div[2]/form/input").click()
    sleep(1)
    browser.find_element_by_name("name").send_keys(user3['username'])
    sleep(1)
    browser.find_element_by_name("description").send_keys('Test Description')
    sleep(1)
    browser.find_element_by_name("reference").send_keys('Test Faculty')
    sleep(1)
    browser.find_element_by_name("submit").click()
    content = browser.page_source
    assert 'You Have Successfully Applied To A New Position!' in content

def test_applyposition_success2(browser,user4): # New Research Position Has Been Created!
    # You Have Successfully Applied To A New Position!
    browser.get('http://127.0.0.1:5000/login')
    browser.find_element_by_name("username").send_keys(user4['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user4['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr[2]/td[2]/div[8]/form/input").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div[2]/form/input").click()
    sleep(1)
    browser.find_element_by_name("name").send_keys(user4['username'])
    sleep(1)
    browser.find_element_by_name("description").send_keys('Test Description')
    sleep(1)
    browser.find_element_by_name("reference").send_keys('Test Faculty')
    sleep(1)
    browser.find_element_by_name("submit").click()
    content = browser.page_source
    assert 'You Have Successfully Applied To A New Position!' in content

def test_applyposition_success3(browser,user5): # New Research Position Has Been Created!
    # You Have Successfully Applied To A New Position!
    browser.get('http://127.0.0.1:5000/login')
    browser.find_element_by_name("username").send_keys(user5['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user5['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr[2]/td[2]/div[8]/form/input").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div[2]/form/input").click()
    sleep(1)
    browser.find_element_by_name("name").send_keys(user5['username'])
    sleep(1)
    browser.find_element_by_name("description").send_keys('Test Description')
    sleep(1)
    browser.find_element_by_name("reference").send_keys('Test Faculty')
    sleep(1)
    browser.find_element_by_name("submit").click()
    content = browser.page_source
    assert 'You Have Successfully Applied To A New Position!' in content

# will have to modify this one, only one of the students will withdrawal
def test_withdrawlposition_success(browser,user5): # New Research Position Has Been Created!
    # You Have Successfully Withdrawed Your Application!
    browser.get('http://127.0.0.1:5000/login') # --requires update from Mitchell--
    browser.find_element_by_name("username").send_keys(user5['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user5['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3) # modify x passes here
    browser.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr[2]/td[2]/div[8]/form/input").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div[2]/form/input").click()
    sleep(1)
    content = browser.page_source
    assert 'You Have Successfully Withdrawed Your Application!' in content
    # last one withdrawals from the class
    
## faculty applicants managements
# button has a name of the applicants
def test_applyposition_interview_approve(browser,user1): # New Research Position Has Been Created!
    # You Have Successfully Applied To A New Position!
    browser.get('http://127.0.0.1:5000/FacultyLogin')
    browser.find_element_by_name("username").send_keys(user1['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr[2]/td[2]/div[8]/form/input").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/form[3]/input").click()
    sleep(1)
    # approve for interview
    browser.find_element_by_xpath("/html/body/div[2]/div/form[2]/input").click()
    sleep(1)
    content = browser.page_source
    assert 'Approved for Interview' in content

def test_applyposition_interview_hire(browser,user1): # New Research Position Has Been Created!
    browser.get('http://127.0.0.1:5000/FacultyLogin')
    browser.find_element_by_name("username").send_keys(user1['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr[2]/td[2]/div[8]/form/input").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/form[3]/input").click()
    sleep(1)
    # hire
    browser.find_element_by_xpath("/html/body/div[2]/div/form[3]/input").click()
    sleep(1)
    content = browser.page_source
    assert 'Hired' in content
    # first one gets approved and hired

def test_applyposition_interview_reject(browser,user1): # New Research Position Has Been Created!
    # You Have Successfully Applied To A New Position!
    # --now works!--
    browser.get('http://127.0.0.1:5000/FacultyLogin')
    browser.find_element_by_name("username").send_keys(user1['username'])
    sleep(1)
    browser.find_element_by_name("password").send_keys(user1['password'])
    sleep(1)
    browser.find_element_by_name("submit").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr[2]/td[2]/div[8]/form/input").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/form[2]/input").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/form[3]/input").click()
    sleep(1)
    # reject for interview
    content = browser.page_source
    assert 'Rejected' in content

# ## ------- I think those are all the tests -------

if __name__ == "__main__":
    retcode = pytest.main()