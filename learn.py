# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# keep Chrome browser open after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
#
# url_amazon = "https://www.amazon.com/Instant-pot-plus-60-Programmable/dp/B01NBKTPTS/?th=1"
# url_bet = "https://superbet.pl/zaklady-bukmacherskie/dzisiaj"
#
# url_ngana = "https://www.nganatech.com/"
#
#
# # driver.get(url_amazon)

# driver.get(url_bet)
#
# driver.get(url_ngana)

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# competitor = driver.find_element(By.XPATH, value='//*[@id="S-245"]/div[1]/a/span/span')

# print(f"The price is {price_dollar.text}.{price_cents.text}")

# print(f"The competitor is {competitor}")

# #driver.close()

# driver.quit()

# from bs4 import BeautifulSoup
# import requests
#
#
# header= {
#     "user-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
#     "Accept-Language": "en-GB; en-US; q=0.9;en;q=0.8"
# }
#
# url_rent = "https://superbet.pl/zaklady-bukmacherskie/pilka-nozna/dzisiaj"
#
# page = requests.get(url_rent, headers=header)
# soup = BeautifulSoup(page.content, 'html.parser')

# elements_bets = soup.find_all("div", class_="event-card__main-content")

# print(soup)


user = "desire"
students = ["claude"," orange"]
colors = ["orange","black", "pink","blue"]
even_numbers = [2,4,6,8,10]

# users_object = {
#     {
#     "age":10,
#     "email":"test@gmail.com"},
#     {
#     "age":10,
#     "email":"test@gmail.com"},
#     {
#     "age":10,
#     "email":"test@gmail.com"
#     }
# }

tuples = ( "claude"," orange", 1,0.2)

# print(colors)

# for ibara in colors:
#     print("this color is " + ibara)

# total = 0
# for num in even_numbers:
#     total = total + num
# print(total)

# word = "yes"
# while word == "yes":
#     print(1+2)

# mood = "bad"

# mood = input("What is your mood today?")
#
# while mood == 'good':
#     print("happy new year")

# even_numbers.sort(reverse=True)


# print(even_numbers)

guess = True
guess_number = 2

while guess:
    print("I have numbers from 1 to 10,Guess my magic number")
    number = input("Give your bet?")
    if number == guess_number:
        print("Congrats you are genius")
        continue_asking = False
    if number != guess_number:
        print("Try again")
























