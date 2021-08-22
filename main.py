import requests
import smtplib
from bs4 import BeautifulSoup

BUY_PRICE = 200
URL = "https://www.amazon.com/dp/B01LVZY19H/ref=syn_sd_onsite_desktop_183?psc=1&uh_it=2bf5a510eb810e82f1fd58f10106272d_CT&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRUxKQUFNWlVIQUZJJmVuY3J5cHRlZElkPUEwNTkxODEwM0VVMlJNV1RUOTAyViZlbmNyeXB0ZWRBZElkPUEwMTI0NzY2M0lCNFRMRjFLUEtXVCZ3aWRnZXROYW1lPXNkX29uc2l0ZV9kZXNrdG9wJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="


def send_email(title, current_price, link):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user="", password="")
    connection.sendmail(
        from_addr="",
        to_addrs="",
        msg=f"Subject:Amazon Price Alert!\n\n{title} now {current_price}\n{link}"
    )


response = requests.get(
    url=URL,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78",
        "Accept-Language": "en-US,en;q=0.9"
    }
)

soup = BeautifulSoup(response.text, "lxml")

price_tag = soup.find(id="priceblock_ourprice")
product_title = soup.find(id="productTitle").getText().strip()
price = float(price_tag.getText().split("$")[1])

if price < BUY_PRICE:
    send_email(product_title.getText(), price, URL)
