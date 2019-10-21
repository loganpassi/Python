#Logan Passi
#09/25/19
#craigslistScraper.py
#Program to search sites like craigslist to find a Sony GDM-FW900 CRT monitor ಥ_ಥ

from fake_useragent import UserAgent
from urllib.request import urlopen, Request

import os
from bs4 import BeautifulSoup
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import time

def main():
    cityList = []
    urlList = []
    keyword = "FW900+%7C+A7217A+%7C+FW0911+%7C+FW9010+%7C+"
    file = open("F:\\Desktop\\pyScript\\craigslist.txt", "r") #open list of cities for each craiglist url
    for entry in file:
        entry = entry[:-1]  # removes the newline at the end of each city
        cityList.append(entry)

    for city in cityList: #concatenate the url out of the keyword and city and other stuff
        urlList.append("https://" + str(city) + ".craigslist.org/search/sss?query=" + str(keyword) + "&excats=20-170&sort=rel")

    file.close() #close input file

    proxyCrawler(urlList)

#function to send an email once an FW900 listing has been found
def sendMail(url):
    port = 465
    password = #sending email pw
    senderAdd = #sending email
    recievingAdd = #receiving email
    context = ssl.create_default_context()
    #subject = "Subject: FW900 FOUND!\n\n"


    message = MIMEMultipart("alternative")
    message["Subject"] = "FW900 FOUND!!!"
    message["From"] = senderAdd
    message["To"] = recievingAdd

    text = """\
    FW900 FOUND!"""
    html = "<html><body><a href = " + str(url) + ">" + str(url) + "</a></body></html>"

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(senderAdd, password)
        server.sendmail(
            senderAdd, recievingAdd, message.as_string()
        )


    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(senderAdd, password)


#function to search craigslist for the FW900
def clSearch(soup, url):
    searchResult = str(soup.find('div', 'alert-sm', 'alert-warning')) #looks for specific html that appears if nothing is found from the search result
    notFoundString = '<div class="alert alert-sm alert-warning">Nothing found for that search. (All words must match.)</div>' #<-- this is what appears when nothing is found from the searchresult
    if searchResult == notFoundString:
        print(url)
        print("Nothing...\n")
    else:
        print("\n==========================")
        print("FW900 FOUND!")
        print(url)
        sendMail(url)
        print("==========================\n")
        input("Press any key to continue searching...")

#fucntion to crawl through the proxies
def proxyCrawler(urlList):
    proxyList = proxyScraper() #return a list of proxies
    proxyIndex = randomElem(proxyList)
    http_proxy = proxyList[proxyIndex]
    i = 1
    j = 1
    while True:
        if i % 5 == 0:
            proxyIndex = randomElem(proxyList)
            http_proxy = proxyList[proxyIndex] #chooses a new proxy from the list of proxies
        if i % 50 == 0:
            proxyList = proxyScraper() #gets a new list of proxies
            i = 0

        ua = UserAgent()
        urlIndex = randomElem(urlList)
        url = urlList[urlIndex]
        urlReq = Request(url)
        urlReq.add_header("User-Agent", ua.random)

        while True:
            try:
                urlDoc = urlopen(urlReq).read().decode("utf8")
                print("#" + str(j))
                print("Current Proxy: " + http_proxy["ip"] + ":" + http_proxy["port"])
                break
            except:
                try:#
                    del proxyList[proxyIndex]
                    print('Proxy ' + http_proxy['ip'] + ':' + http_proxy['port'] + ' deleted.\n')
                    proxyIndex = randomElem(proxyList)
                    http_proxy = proxyList[proxyIndex]
                except:
                    proxyList = proxyScraper()

        soup = BeautifulSoup(urlDoc, 'lxml')

        clSearch(soup, url)
        i += 1
        j += 1
        time.sleep(3)
        if j % 100 == 0:
            os.system('cls')

#function to scrape new proxies
def proxyScraper():
    ua = UserAgent()
    proxyList = [] #will contain proxies[ip, port]
    proxiesReq = Request("https://www.sslproxies.org/")
    proxiesReq.add_header("User-Agent", ua.random)
    proxiesDoc = urlopen(proxiesReq).read().decode("utf8")

    soup = BeautifulSoup(proxiesDoc, "lxml")
    proxiesTbl = soup.find(id = 'proxylisttable')

    for row in proxiesTbl.tbody.find_all("tr"):
        proxyList.append({
            'ip': row.find_all('td')[0].string,
            'port': row.find_all('td')[1].string
        })
    return proxyList

#function to get a random proxy
def randomElem(list):
  return random.randint(0, len(list) - 1)

if __name__ == "__main__":
    main()
