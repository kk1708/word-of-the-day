import requests
from bs4 import BeautifulSoup

#connecting to the website and creating the beautiful soup object
source = requests.get("https://www.dictionary.com/e/word-of-the-day/", timeout=5).text
soup=BeautifulSoup(source,"lxml")

print("The Word of the Day\n")

#printing the word of the day
word = soup.find("div", class_="otd-item-headword__word")
wod= word.h1.text
print(wod.upper())

#printing the type of the word
wordType = soup.find("span", class_="luna-pos")
print(wordType.text)

#printing the definition of the word
d = soup.find("div", class_="otd-item-headword__pos")
definition = d.find_all("p")
print("\nDefinition of "+wod+": "+definition[1].text)

#printing examples of the word
example = soup.find("div", class_="wotd-item-example__content")
print("\nExample of "+wod+" in a sentence: "+"'"+example.p.text+"'\n")
