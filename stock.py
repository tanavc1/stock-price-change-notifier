import requests
from bs4 import BeautifulSoup
import smtplib
import time
ticker = input("Enter stock ticker symbol")
advticker = ticker.replace(' ' , '')
wantedprice = input("What price do you want the stock at?")
numwantedprice = float(wantedprice)
def stockfunction():
 url = 'https://markets.businessinsider.com/stocks/' + advticker + '-stock'
 print(url)
 print(url)
 res = requests.get(url)
 soup = BeautifulSoup(res.text, 'html.parser')
 priceholder = soup.find(class_='push-data aktien-big-font text-nowrap no-padding-at-all').text
 #print(priceholder)
 numpriceholder = float(priceholder)
 print(numpriceholder)
 if (numwantedprice >= numpriceholder) :
    email_send()


def email_send():
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.ehlo()

     server.login('tanavc01@gmail.com', 'ohifeaeyzywgdnev')

     subject = 'stock price is in your range!'
     body = 'here is the link: '
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
