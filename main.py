import requests
from urllib.request import urlopen
import pydantic
from bs4 import BeautifulSoup
query = input("What are you looking for? ")
query = query.replace(" ", '+')
URL: str = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw={query}&_sacat=0"
URL1: str = f'https://www.amazon.ca/s?k={query}&ref=nb_sb_noss'
URL2: str = f'https://www.biblio.com/search.php?stage=1&keyisbn={query}'
URL3: str = f'https://www.libgen.is/search.php?req={query}&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def'
urls = [URL, URL1, URL2, URL3]
for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    for link in soup.find_all('a'):
        l = str(link.get('href'))
        if 'ads' in l:
            continue
        else:
            print(link.get('href'))

    print(url, r.status_code)


# <a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/sspa/click?ie=UTF8&amp;spc=MTo2Njg1NDgxODg1NTUzMDI0OjE3MDYxNTE4MzA6c3BfYXRmOjMwMDA0MzQ0NzkyMTcwMjo6MDo6&amp;url=%2FLEGO-Star-Wars-Chancellor-Minifigures%2Fdp%2FB0BXQ5SX82%2Fref%3Dsr_1_3_sspa%3Fcrid%3DKURZDJBAA7DI%26keywords%3Dclone%2Bwars%26qid%3D1706151830%26sprefix%3Dclone%2Bwars%252Caps%252C103%26sr%3D8-3-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1"><span class="a-size-base-plus a-color-base a-text-normal"