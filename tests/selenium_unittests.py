import unittest
import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

# first launch the server in the separate terminal using the "python smile.py"
# cd into the automated tests folder : cd automated_tests
# to run the tests: "python -m unittest app_unittesting.py"

# User fixure
@pytest.fixture
def user1():
    # faculty
    return  {'username':'arslanay', 'wsuid':'111222333', 'firstname':'Sakire', 'lastname':'Arslanay', 'email':'arslanay@wsu.edu', 'password':'strongpassword', 'address':'testaddyhmu', 'phonenum':'+12345678900'}

# User fixure
@pytest.fixture
def user2():
    # student
    return  {'username':'john', 'email':'john@wsu.edu', 'password':'alsostrongpassword'}

class TermProjectTesting(unittest.TestCase):

    def test_studentlogin(self):
        print("works!")

    def test_facultylogin(self):
        print("works!")

    def test_student_registration(self):
        print("works!")

    def test_fregistration(self):
        print("works!")

if __name__ == '__main__':
    unittest.main()

