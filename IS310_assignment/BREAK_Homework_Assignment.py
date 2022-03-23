'''DISCLAIMER

I want to say that I read and used several codes from Jackey's work.
Such as recieveing urls from the txt file - address.append((divide[2].strip()))
Save texts in dictionary in more cleaner way (.append makes text really messy and big)
Limiting scraping urls (which neccesary since return error without limiting range)
And lastly, saving the texts to txt file.

'''





import pandas as pd
import bs4
from bs4 import BeautifulSoup
import requests

# Getting urls from raw_script_urls.txt
read = open("README.txt", "r", encoding="ISO-8859-1")
urls = open("/Users/junggchangho/Desktop/workspace/IS310_assignment/raw_script_urls.txt", "r", encoding="ISO-8859-1")
#urls = pd.read_csv('/Users/junggchangho/Desktop/workspace/IS310_assignment/raw_script_urls.txt', sep=' +++$+++ ', encoding='utf=8')
#print(read.read())
#print(urls.read())
address = []
results_dict = {}
results_dict['Text'] = []

# Each urls are seperated by ' +++$+++ ', so use split to divide urls (string), and save into list 'address' by .append
for column in urls:
    divide = column.split(' +++$+++ ')
    # divide itself is list, which cannot use strip. since 3rd column [2] is url, put next to divide.
    address.append((divide[2].strip()))

print(address)


# Now, getting a actual text from the urls from 'address' list
def Text(address):
    response = requests.get(address)
    soup = BeautifulSoup(response.text, features="html.parser")
    #print(soup.text)
    # Select 'pre' since that's the main texts of content I need.
    results = soup.find_all('pre')

    for result in results:
        result = result.get_text()
        #print(result)
        # This indeed write on a txt file, but broken with pieces.
        '''results_dict['Text'].append(result)'''
        # If I do not put [0] at the end of 'result', the texts will broke like the previous one.
        results_dict[result[0]] = results


# I do not know why, but I keep getting an error if I do not set range. It seems limit is 80 urls
for add in address[0:80]:
#    print(add)
    Text(add)
# Let's see the result!
print(results_dict)

# Now save the scraped texts to txt file name 'texts.txt'.
final = open("texts.txt", 'w')
final.write(str(results_dict))