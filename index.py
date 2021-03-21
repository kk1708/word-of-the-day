import requests
from bs4 import BeautifulSoup

#connecting to the website and creating the beautiful soup object
source = requests.get("https://www.dictionary.com/e/word-of-the-day/", timeout=5)

#testing to see if connection can be established
if source.status_code !=200:
	print("Couldn't connect to the website")
	exit()

soup=BeautifulSoup(source.text,"html.parser")

print("The Word of the Day\n")

try:
	#printing the word of the day
	word = soup.find("div", class_="otd-item-headword__word")
	wod= word.h1.text
	print(wod.upper())
except:
	print("Couldn't get the word")

try:
	#printing the type of the word
	wordType = soup.find("span", class_="luna-pos")
	print(wordType.text)
except:
	print("Couldn't get the part of the speech")

try:
	#printing the definition of the word
	d = soup.find("div", class_="otd-item-headword__pos")
	definition = d.find_all("p")
	try:
		print("\nDefinition of "+wod+": "+definition[2].text)
	except:
		print("\nDefinition of "+wod+": "+definition[1].text)
except:
	print("Couldn't get the definition of the word")

try:
	#printing examples of the word
	example = soup.find("div", class_="wotd-item-example__content")
	print("\nExample of "+wod+" in a sentence: "+"'"+example.p.text+"'\n")
except:
	print("Couldn't get the example of the word")
