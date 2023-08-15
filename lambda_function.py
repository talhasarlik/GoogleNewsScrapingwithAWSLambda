from bs4 import BeautifulSoup
import requests
import pymysql
from datetime import datetime
import time
from zoneinfo import ZoneInfo

# Database configurations
endpoint='ottoo-case-study.c9wd65fvawq8.eu-north-1.rds.amazonaws.com'
username='admin'
password='casestudy'

# Connection to database
mydb = pymysql.connect(
    host=endpoint,
    user=username,
    password=password,
    db=None
)

# Creating database and table
mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE google_news_lambda_test")
# print("ok")
# mycursor.execute("SELECT * FROM google_news_data")
# print("selected")
# result = mycursor.fetchall()
# for row in result:
#     print(row)
# mycursor.execute("CREATE DATABASE IF NOT EXIST google_news_lambda_test")
# mycursor.execute("USE google_news_lambda_test")
# mycursor.execute("CREATE TABLE IF NOT EXIST google_news_data (url VARCHAR(8000), Header VARCHAR(255), Summary VARCHAR(255), Publisher VARCHAR(100), Release_date DATETIME, Place INTEGER, Category VARCHAR(20), Last_Check ENUM('YES','NO'))")

# # INSERT formula
# sqlFormula = "INSERT INTO google_news_data (url, Header, Summary, Publisher, Release_Date, Place, Category, Last_Check) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

# # Dictionary for url's of different categories
# categories = ["Türkiye", "Dünya", "İş", "Bilim ve Teknoloji", "Eğlence", "Spor", "Sağlık"]
# category_url = {
#   "Türkiye" : "CAAqIggKIhxDQkFTRHdvSkwyMHZNREY2Ym1OZkVnSjBjaWdBUAE",
#   "Dünya" : "CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FuUnlHZ0pVVWlnQVAB",
#   "İş" : "CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuUnlHZ0pVVWlnQVAB",
#   "Bilim ve Teknoloji" : "CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSjBjaG9DVkZJb0FBUAE",
#   "Eğlence" : "CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FuUnlHZ0pVVWlnQVAB",
#   "Spor" : "CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FuUnlHZ0pVVWlnQVAB",
#   "Sağlık" : "CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FuUnlLQUFQAQ"
# }

# url_header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}


# def lambda_handler(event, context):
#   # Set last check status as no of the old values at the database
#   mycursor.execute("UPDATE google_news_data SET Last_Check = 'NO' WHERE Last_Check = 'YES'")
#   mydb.commit
    
#   for category in categories:
#     # Set the url and call BeautifulSoup
#     url = f"https://news.google.com/topics/{category_url[category]}?hl=tr&gl=TR&ceid=TR%3Atr"
#     html = requests.get(url, headers=url_header)
#     print(html.text)
#     soup = BeautifulSoup(html.text, 'html.parser')
    
#     # Header list
#     headers = soup.find_all('h4')
#     # url list
#     links = soup.find_all(class_='WwrzSb')
#     #Publisher list
#     publishers = soup.find_all(class_ = "vr1PYe")
#     #Date list
#     dates = soup.find_all(class_ = "hvbAAd")
#     print(dates)

#     for index, header in enumerate(headers):
#       # url
#       url = f"https://news.google.com{links[index]['href'][1:]}"
#       # Header
#       header = header.text
#       # Summary
#       try:
#         new_html = requests.get(url, timeout=10)
#         new_soup = BeautifulSoup(new_html.text, 'html.parser')
#         summ = new_soup.find('h2').text
#       except:
#         summ = "Summary of the new cannot be found."
#       # Publisher
#       publisher = publishers[index].text
#       # Date
#       date = dates[index]['datetime']
#       date = date[:10]+ ' ' + date[11:-1]
      
#       #Creating a temp tuple for inserting data
#       temp = (url, header, summ, publisher, date, index+1, category , 'YES')
#       mycursor.execute(sqlFormula, temp)
#       mydb.commit()

#   # Commit the changes
#   mydb.commit()
  
#   turkey_dt = datetime.now(tz=ZoneInfo("Europe/Istanbul"))
#   print("Database succesfully updated at ", turkey_dt)





