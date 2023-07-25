#create a script that scrapes and downloads pdf files from this page: https://kingcounty.gov/council/legislation/kc_code.aspx
#
#The script should create a folder called kingcounty and download all the pdfs from the page into that folder.
#
#The script should also print out the names of the pdfs it is downloading.
#
#The script should also print out the number of pdfs it downloaded.
#
#The script should also print out the total file size of all the pdfs it downloaded.
#

import requests, os, bs4
#url = 'https://www.lrl.mn.gov/mndocs/mandates_detail?orderid=7861'
url = 'https://www.lrl.mn.gov/mndocs/mandates_detail?orderid=7861'
os.makedirs('Minnesota', exist_ok=True)
print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
# Find the URL of the pdf file
pdfElems = soup.select('a[href$=".pdf"]')
pdfCount = 0
pdfSize = 0
for pdf in pdfElems:
    pdfUrl = pdf.get('href')
    print('Downloading %s...' % (pdfUrl))
    res = requests.get(pdfUrl)
    res.raise_for_status()
    pdfCount += 1
    pdfSize += len(res.content)
    # Save the pdf to ./Minnesota
    pdfFile = open(os.path.join('Downloaded', os.path.basename(pdfUrl)), 'wb')
    for chunk in res.iter_content(100000):
        pdfFile.write(chunk)
    pdfFile.close()
print('Done.')
print('Downloaded %s pdfs totaling %s bytes.' % (pdfCount, pdfSize))
