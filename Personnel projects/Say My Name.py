from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t


opt=Options()
print("Building Envirorment	(ETA 10-20 seconds)")
print('')
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
dr=webdriver.Firefox(firefox_options=opt)
print("Build Success!")
print('')
print("	    SHERLOCK @ HINDUSTHAN     ")
print('')
img=timg.Renderer()
img.load_image_from_file("/home/r00t/s.png")
img.resize(30,40)
img.render(timg.ASCIIMethod)
print("	   COPYRIGHT: ACRPSM@DEVOLOPERS")
print('')


def search(roll):
	
    dr.get("https://hicet902.examly.io/login")
    mail=roll+"@hicet.ac.in"
    t.sleep(5)
    print("Sending Keys.../")
    ele=dr.find_element_by_id('email')
    ele.send_keys(mail)
    btn=dr.find_element_by_id('lgnNext0').click()
    print("Keys Send Successfully!")
    try:
    	WebDriverWait(dr, 10).until(EC.element_to_be_clickable((By.ID, "lgnLogin0")))

    except:
    	print('Something Went Wrong(Timeout/UserNotFound)')
    	print('')
    	ui()
    
    name=dr.find_element_by_class_name("head.position-top-6px").text
    return name

def ui():
	rollno=input("Enter The Roll Number: ")
	print('')
	print('Fetching Details.../')
	name=search(rollno)
	nl=name.split(',')
	print("User Found: ",nl[1:])
	print('')
	print('--------------------------------------')
	ui()

ui()
