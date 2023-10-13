# Jacob Muller, jacobmuller@ufl.edu

import urllib.request
import urllib.parse
from lxml import html


def getHeadline():
    print("Get Headline\n")

    # Get URL data, format it, parse it, print value
    url = 'https://news.ufl.edu'
    page_data = urllib.request.urlopen(url).read()
    parsed_content = html.fromstring(page_data)
    headline = parsed_content.xpath('//*[@id="main"]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/span/a/text()')

    print("Source:", url)
    print("Headline:", headline[0])
