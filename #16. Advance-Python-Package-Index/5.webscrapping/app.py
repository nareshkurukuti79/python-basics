import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")

# print(questions)
# print(type(questions))

# print("attributes")
# print(questions[0].attrs)

# print("id value")
# print(questions[0].get("id", 0))

# print(questions[0].select_one(".s-link"))

# print(questions[0].select_one(".s-link").getText())

i = 0
for question in questions:
    print(i+" "+question.select_one(".s-link").getText())
    i = i+1
