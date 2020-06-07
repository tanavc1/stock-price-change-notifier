import requests
from bs4 import BeautifulSoup
import smtplib
import time
ticker = input("Enter stock ticker symbol")
advticker = ticker.replace(' ' , '')
wantedprice = input("What price do you want to be notified at?")
numwantedprice = float(wantedprice)
ran = input("Do you want to be notified when it goes up or down?")
rann = ran.replace(' ', '')
url = 'https://markets.businessinsider.com/stocks/' + advticker + '-stock'
def stockfunction():
 print(url)
 res = requests.get(url)
 soup = BeautifulSoup(res.text, 'html.parser')
 priceholder = soup.find(class_='push-data aktien-big-font text-nowrap no-padding-at-all').text
 #print(priceholder)
 numpriceholder = float(priceholder)
 print(numpriceholder)
 if (rann == "up") :
  if (numwantedprice <= numpriceholder) :
    email_send()
 if (rann == "down") :
  if (numwantedprice >= numpriceholder):
            email_send()


def email_send():
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.ehlo()

     server.login('tanavc01@gmail.com', 'ohifeaeyzywgdnev')

     subject = 'stock price has met your goal!'
     body = 'here is the link: ' + url
     msg = f"Subject: {subject}\n\n{body}"

     server.sendmail(
         'tanavc01@gmail.com',
         'tanav.chinthapatla@gmail.com',
         msg
     )
     print('EMAIL SENT')

     server.quit()


while(True):
    stockfunction()
    time.sleep(60*60)






