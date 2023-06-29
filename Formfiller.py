import pandas as pd
import requests
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import time
import numpy as np

from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

df = pd.read_excel('/home/rithvik/web_scraping/form_filling/test_links.xlsx')

# # options = ChromeOptions()
# # options.add_argument("--headless=new")
# # options.add_experimental_option("detach", True)
# # path = Service("/home/ubuntu/web_scraping/chromedriver.exe")

options = Options()
options.add_argument("--headless=new")
path = Service("/home/rithvik/web_scraping/msedgedriver.exe")

# df = pd.read_excel('test_links1.xlsx')

index = {
  "Fname": "Sandy",
  "Lname": "N",
  "FULLname": "Sandy N",
  "email": "soundharya@chezuba.net",
  "phone": "(317)7321438",
  "subject": "Virtual Volunteering"
}
message = "Hey,I came across your organization and was delighted to lean about your efforts. I'd like to speak with you about how we could provide free virtual volunteers to your nonprofit. I eagerly await your response."
#Links = ['www.face4kids.org']

no_form = []
form = []
no_page = []
no_contact_pg = []
ss = []
form_on_diff = []
count =0
start_time = time.time()

for link in df['Links']:
    try:
        driver = Edge(service= path,options=options)
        # driver = Edge()
        # wait = WebDriverWait(driver, 10)
    except:
        print("unable to open chrome")
    count +=1
    try:
        if link[:4] == "http":
            url = link
        else:
            url = "http://" + link
        try:
            driver.get(url)
            
            no_page.append('')
            sleep(2)
            print(count)
        except:
            no_page.append('no page')
    except:
        pass
        
    try:
        cont_url = driver.find_element(By.CSS_SELECTOR, value = "a[href *='contact']").get_attribute('href')
        driver.get(cont_url)
        sleep(2)
    except:
        no_contact_pg.append(count)
        
    # try:
    #     div1 = driver.find_element(By.CSS_SELECTOR, value = "a[href *='form']").click()
    # except:
    #     pass
        
    try:
        form_tag = driver.find_element(By.TAG_NAME, "form")
        no_form.append('')
    except:
        no_form.append('No Form')
        
	#FILLING EMAIL
    e_check = False
    try:
        temp = form_tag.find_elements(By.CSS_SELECTOR, value = "input[name *='mail'i]")
        e_check = True    
    except:
        pass
   
    if e_check == False:
        try:
            temp = form_tag.find_elements(By.CSS_SELECTOR, value = "input[placeholder *='Email'i]")
            e_check = True
        except:
            pass
    
    if e_check== False:
        try:
            temp = form_tag.find_elements(By.CSS_SELECTOR, value = "input[type *='email']")
            e_check = True
        except:
            pass

    # try:
    #     temp = driver.find_elements(By.CSS_SELECTOR, value = "input[data-aid *='email'i]")
    #     e_check = True
    # except:
    #     pass
    try:
        for et in temp:
            try:
                et.send_keys(index['email'])
            except:
                pass
    except:
        pass

    #FILLING FIRST NAME AND LAST NAME
    FN_check = False
    try:
        temp = form_tag.find_element(By.CSS_SELECTOR, value = "input[name *='fname'i]").send_keys(index['Fname'])

        FN_check = True
    except:
        pass
    
    if FN_check == False:
        try:
            temp = form_tag.find_element(By.CSS_SELECTOR, value = "input[name *='first'i]").click().send_keys(index['Fname'])
            FN_check = True
        except:
            pass
    if FN_check == False:
        try:
            temp = form_tag.find_element(By.CSS_SELECTOR, value = "input[placeholder *='First'i]").send_keys(index['Fname'])
            FN_check = True
        except:
            pass
        
    LN_check = False
    try:
        temp = form_tag.find_element(By.CSS_SELECTOR, value = "input[placeholder *='Last'i]").send_keys(index['Lname'])
        LN_check = True
    except:
        pass    
    if LN_check == False:
        try:
            temp = form_tag.find_element(By.CSS_SELECTOR, value = "input[name *='lname'i]").send_keys(index['Lname'])
            LN_check = True
        except:
            pass

    if LN_check == False:
        try:
            temp = form_tag.find_element(By.CSS_SELECTOR, value = "input[name *='last'i]").send_keys(index['Lname'])
            LN_check = True
        except:
            pass    
    
    
    #FILLING FULL NAME
    if FN_check == False:
        FULN_check = False
        try:
            temp = form_tag.find_element(By.CSS_SELECTOR, value = "input[name *='name'i]").send_keys(index['FULLname'])
            FULN_check = True
        except:
            pass
        if FULN_check == False:
            try:
                temp = form_tag.find_element(By.CSS_SELECTOR, value = "input[placeholder *='Name'i]").send_keys(index['FULLname'])
            except:
                pass
    
	
    #FILLING SUBJECT
    sub_check = False    
    try:
        temp = form_tag.find_element(By.CSS_SELECTOR, value = "input[name *='subject'i]").send_keys(index['subject'])
        sub_check = True
    except:
        pass
    if sub_check == False:
        try:
            temp = form_tag.find_element(By.CSS_SELECTOR, value = "input[placeholder *='Subject'i]").send_keys(index['subject'])
            sub_check = True
        except:
            pass
    if sub_check == False:
        try:
            temp = form_tag.find_element(By.CSS_SELECTOR, value = "input[data-aid *='subject'i]").send_keys(index['subject'])
            sub_check = True
        except:
            pass
    
    #FILLING PHONE NUMBER
    
    try:
        temp = form_tag.find_element(By.CSS_SELECTOR, value = "input[placeholder *='Phone'i]").send_keys(index['phone'])
    except:
        pass
    #FILLING MESSAGE
    try:
        temp = form_tag.find_element(By.TAG_NAME, 'textarea').send_keys(message)
    except:
        pass
    
    
    
    #SUBMIT BUTTON
    check = False
    try:
        sub = form_tag.find_element(By.CSS_SELECTOR, value = "button[type *= 'submit']").click()
        # element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id *= 'submit']")))
        # sub = form_tag.find_element(By.CSS_SELECTOR, value = "button[id *= 'submit']").click()

        # # sub = form_tag.find_element(By.XPATH, '//*[@id="wpforms-submit-546"]').click()
        
        check = True
    except:
        pass

    if check == False:     
        try:
            sub = form_tag.find_element(By.CSS_SELECTOR, value = "input[type *= 'submit']").click()
            check = True
        except:
            pass
    if check == False:    
        try:    
            sub = form_tag.find_element(By.CSS_SELECTOR, value = "button[data-testid *= 'buttonElement']").click()
            check = True
        except:
            pass
    if check == False:    
        try:    
            sub = form_tag.find_element(By.CSS_SELECTOR, value = "button[type *= 'buttonElement']").click()
            check = True
        except:
            pass


    sleep(4)
    try:
        print("before ss")
    except:
        pass
    
    try:
        if check == True:
            total_height = driver.execute_script("return document.documentElement.scrollHeight")
            driver.set_window_size(1920, total_height)
            screenshot = driver.find_element(By.TAG_NAME, 'body').screenshot_as_png
            
            ss_name = '/home/rithvik/DATA/'+ str(count) + '.png'
            # ss_name =  str(count) + '.png'
            with open(ss_name, 'wb') as file:
                file.write(screenshot)
    except:
        ss.append(count)
    try:
        driver.close()
    except:
        pass


elapsed_time = time.time() - start_time
print(len(no_form))
print(len(no_page))
    
#df = pd.DataFrame({"No Contact Page": pd.Series(no_contact_pg), "No Form":pd.Series(no_form), "With Form":pd.Series(form),"Broken Link": pd.Series(no_page), "SS not captured": pd.Series(ss), 'Form on dif page': pd.Series(form_on_diff), 'Time taken': pd.Series(elapsed_time)})
df['Form'] = no_form
df["Broken Link"] = no_page

timez = pd.Series(elapsed_time, index=np.arange(elapsed_time))
df['Time Taken'] = timez

df.to_excel("Failure report.xlsx", index = False)
