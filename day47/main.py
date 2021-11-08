import requests
from bs4 import BeautifulSoup
import smtplib
from decouple import config

my_email = config('MYEMAIL')
emailpassword = config('EMAILPASSWORD')

headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36","Accept-Language":"en-US,en;q=0.9"}

endpoint = ("https://www.amazon.com/KitchenAid-KSM7586PFP-7-Quart-Stand-Frosted/dp/B008XF78IQ/ref=sr_1_5?keywords=kitchen%2Baid%2Bmixer&qid=1636334962&qsid=130-7706042-6707727&sr=8-5&sres=B000P9GWFS%2CB01HKAUJ4E%2CB008XF78PE%2CB00CBFZCTG%2CB00QUGZHSI%2CB009VUHLHA%2CB01K2FQ4DE%2CB07NY8VX89%2CB099VZ4NQ9%2CB08CXKVSKX%2CB08GQN2DNF%2CB07RKTYQV7%2CB08CKJM8G4%2CB0987CKSCT%2CB08LD244VC%2CB091PLRW67&srpt=FOOD_MIXER&th=1")

response = requests.get(endpoint, headers=headers)
print(response.status_code)
amazon_page = response.text

amazon_soup = BeautifulSoup(amazon_page,'html.parser')
price_tag = amazon_soup.find(name="span",class_="a-offscreen")
amazon_price = price_tag.getText()
price = amazon_price[1:]
print(price)

with smtplib.SMTP("smtp.gmail.com") as apple:
    apple.starttls()
    apple.login(user=my_email,password=emailpassword)
    apple.sendmail(
        from_addr=my_email, 
        to_addrs="ashdev97@yahoo.com", 
        msg=f"Subject:You are getting a KitchenAid!!!\n\n New price is{price}"
    )