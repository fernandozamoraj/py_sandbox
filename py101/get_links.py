import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

def getLinks(siteUrl, targetWord):

   links = []
   http = httplib2.Http()

   status, response = http.request(siteUrl)

   index = 0

   for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):

      href = link.get('href')

      print "link found"
      if not href:
         pass
      else:
         if targetWord in href:

             print href
             #prepend the link with the domain name (e.g. theverge.com/...
             if href[0] == '/':
                href = siteUrl + href
             print href
             links.append(href)

   return links
   
def writeToFile(filePath, links):

   fileWriter = open(filePath, "w")

   for link in links:
      fileWriter.write(link)
      fileWriter.write("\n")

   fileWriter.close()

def getSites():
   sites = []
   sites.append('http://www.theverge.com')
   sites.append('http://www.techcrunch.com')
   sites.append('http://www.livescience.com')

   return sites

masterList = []

for site in getSites():
   links = getLinks(site, '-')
   if len(links) > 0:
      masterList.extend(links)


writeToFile('links43.html', masterList) 