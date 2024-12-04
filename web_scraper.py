import smtplib,time
from selenium import webdriver
from  selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/Denill-Comfortable-T-Strap-Sandal-Women/dp/B07VGLNWQK/ref=sr_1_1?crid=8YACATKRM73A&dib=eyJ2IjoiMSJ9.jEOdw_EvObHkXW_c5YsVNFj3kGq3BciqoDoYyLecLXe3F3UcRQ0cvmI3KqVPKreKnLgwYiGA_HGhn4ereHbTOE5XPR1_N75N5XQJYstuVdpSzkFrpMFiNwX-_dpPACxaAUzVHghcJpMgIUMq8uI4lLLstBPOB5EuSgG8_inOtAxAKxakILLcoeTNNHKRdl3_7WakW1QD0DNqlgmhR_dGyaI6bZ9sKkkEn1IUj-om6wbI87Yx6g-tOqdmE06px7I6UvVxOpXFjZTMEHiWkIXGk5BUT4v7HvelD0RwnFfUSN4.zLMrJKV-F88HO5Tp6C16TJvcaG90HvjEnIzF74eADyI&dib_tag=se&keywords=pencil+heels+for+girls&qid=1723565387&s=apparel&sprefix=%2Capparel%2C1693&sr=1-1")
time.sleep(12)
price = driver.find_element(By.CLASS_NAME,value="a-price-whole")
price = int(price.text)
print(price)

if price < 500 :
    my_email = "p8114394@gmail.com"
    password = "fcux wvsp zgij pdps"
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="p1219513@gmil.com",msg="go buy\nyour sandle it is below 500 \n grab it")
    connection.close()

input()
driver.quit()