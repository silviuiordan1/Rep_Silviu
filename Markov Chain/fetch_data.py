import urllib2
from bs4 import BeautifulSoup

def fetch_data(url_request):
    req = urllib2.Request(url_request)
    try: 
        html_resp = urllib2.urlopen(req)
        html_page = html_resp.read()
    except urllib2.HTTPError as e:
        print e.code
        print e.read()    
    soup = BeautifulSoup(html_page,'html.parser') 
    output_text = soup.get_text().encode('utf-8')
    return output_text

