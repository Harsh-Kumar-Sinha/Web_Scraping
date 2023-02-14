# Importing Libraries
import requests
from bs4 import BeautifulSoup

# URLs from where to fetch data 
urls = ["https://www.anthem.com/ca/faqs/california/account-and-caregiver-access/","https://www.anthem.com/ca/faqs/california/alternative-languages/",
"https://www.anthem.com/ca/faqs/california/behavioral-health-resource-center/","https://www.anthem.com/ca/faqs/california/benefits-claims/",
"https://www.anthem.com/ca/faqs/california/customer-support/","https://www.anthem.com/ca/faqs/california/dependent-care/",
"https://www.anthem.com/ca/faqs/california/doctors-hospitals-facilities/","https://www.anthem.com/ca/faqs/california/emergency-care/",
"https://www.anthem.com/ca/faqs/california/health-wellness/","https://www.anthem.com/ca/faqs/california/laws-rights-protect-you/",
"https://www.anthem.com/ca/faqs/california/pharmacy/","https://www.anthem.com/ca/faqs/california/technical-issues/"]

# A list where Questions-Answers will be stored 
#my_dict = {}
# questions = []
# answers = []


print("-------------------------------------------------------------------------")
count = 1
# Parsing code
for url in urls:
    questions = []
    answers = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    faq_questions = soup.find_all("div", class_="panel-heading")
    faq_answers = soup.find_all("div", class_ = "panel-collapse collapse")

    for faq_element in faq_questions:
        que = faq_element.find("a").text.strip()
        questions.append(que)

    for faq_element in faq_answers:
        ans = faq_element.find("p").text.strip()
        answers.append(ans)

    print(f"{count}-{len(questions)}")
    count += 1

    
#my_dict = dict(zip(questions, answers))
#print(my_dict)
#print(len(my_dict))

print("-------------------------------------------------------------------------")

