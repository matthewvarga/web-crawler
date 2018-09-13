import urlparse
import urllib
from bs4 import BeautifulSoup


def crawl(website, fileName):
    url = website

    urlQueue = [url] #starts with the website home page url
    urlHistory = [url] #keeps track of every single url visited

    urlFile = open("{0}.json".format(fileName),"w")
    urlFile.write(url)
    urlFile.write("\n")
    while len(urlQueue) > 0: #while we have links to still visit
        try: #prevents program from crashing if website url is invalid
            htmlText = urllib.urlopen(urlQueue[0]).read() #gets the html text of url at top of queue
        except:#what happens if there is an error trying to open webpage
            print urlQueue[0] #prints url we could not open

        soup = BeautifulSoup(htmlText, "html.parser")

        urlQueue.pop(0) #removes the url at top of queue after we have scraped it
        print len(urlQueue)

        for tag in soup.findAll("a", href=True): #finds the <"a"> tag, and if it has a valid href/link continues
            tag["href"] = urlparse.urljoin(url,tag["href"]) #if the link is missing http://.... this adds it
            if url in tag["href"] and tag["href"] not in urlHistory: #checks if the link is actually part of the site, not fb or twitter or spam, then checks if we have visited link yet or not, if not continues
                urlQueue.append(tag["href"]) #adds the new/unvisited url that we found to the queue
                urlHistory.append(tag["href"]) #stores the new url in history
                urlFile.write(str(tag["href"]))
                urlFile.write("\n")
            

crawl("http://www.example.com", "output_file_name")

        
        
