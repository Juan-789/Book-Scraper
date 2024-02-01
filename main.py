import requests
from urllib.request import urlopen
import pydantic
from bs4 import BeautifulSoup
query = input("What are you looking for? ")
query = query.replace(" ", '+')
EBAY: str = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw={query}&_sacat=0"
AMZN: str = f'https://www.amazon.ca/s?k={query}&ref=nb_sb_noss'
BIBLIO: str = f'https://www.biblio.com/search.php?stage=1&keyisbn={query}'
LIBGEN: str = f'https://www.libgen.is/search.php?req={query}&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def'
urls = [EBAY, AMZN, BIBLIO, LIBGEN]
urlsCorps = ["EBAY"," AMZN", "BIBLIO"," LIBGEN"]
file = open('ItemLinks.html', 'w', encoding='utf-8')
queryLinks = []
sourceCounter = 1
linkCounter = 0
for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    if url == EBAY:
        for Ebaytag in soup.find_all('div', class_="s-item__info clearfix"):
            for Ebaylink in Ebaytag.find_all_next('a', class_="s-item__link"):
                linkCounter+=1
                queryLinks.append((f"Ebay link #{linkCounter}", Ebaylink))
    else:
        for link in soup.find_all('a'):
            l = str(link.get('href'))
            if ('ads' in l ) or ('http' not in l) or ('library.bz'  in l) or ('mhut'  in l) or ('onion'  in l):
                continue
            elif (url == LIBGEN) and(( 'phillm'  in l) or ('magzdb'  in l)):
                continue
            else:
                linkCounter+=1
                queryLinks.append((f"{urlsCorps[sourceCounter]} link #{linkCounter}" ,link))

    print(url, r.status_code)


file.write(str(queryLinks))

# <a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/sspa/click?ie=UTF8&amp;spc=MTo2Njg1NDgxODg1NTUzMDI0OjE3MDYxNTE4MzA6c3BfYXRmOjMwMDA0MzQ0NzkyMTcwMjo6MDo6&amp;url=%2FLEGO-Star-Wars-Chancellor-Minifigures%2Fdp%2FB0BXQ5SX82%2Fref%3Dsr_1_3_sspa%3Fcrid%3DKURZDJBAA7DI%26keywords%3Dclone%2Bwars%26qid%3D1706151830%26sprefix%3Dclone%2Bwars%252Caps%252C103%26sr%3D8-3-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1"><span class="a-size-base-plus a-color-base a-text-normal"