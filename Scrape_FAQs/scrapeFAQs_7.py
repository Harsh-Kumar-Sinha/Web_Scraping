import requests
from bs4 import BeautifulSoup

url = "https://www.anthem.com/ca/faqs/california/doctors-hospitals-facilities/"

# Send an HTTP request to the URL
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, "html.parser")

faq_questions = soup.find_all("div", class_="panel-heading")
faq_answers = soup.find_all("div", class_ = "panel-collapse collapse")

questions = []
for faq_element in faq_questions:
    question = faq_element.find("a").text.strip()
    questions.append(question)

# Store the extracted information
print(questions)

answers = []
for faq_element in faq_answers:
    question = faq_element.find("p").text.strip()
    answers.append(question)

print(answers)

my_dict = dict(zip(questions, answers))
print(my_dict)

