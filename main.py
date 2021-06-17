import requests
from bs4 import BeautifulSoup
import uuid

url = 'https://icanhas.cheezburger.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img', attrs='resp-media')

for image in images:
    name = (uuid.uuid1())
    link = image['src']

    try:
        with open(str(name) + '.jpg', "wb") as f:
            img = requests.get(link)
            f.write(img.content)
    except Exception:
        pass
        print('bad url')

def generateLink():
    new_url = 'https://icanhas.cheezburger.com/page/'
    return new_url

count = 1
new_pages = []

i=0
while (i <= 10):
    new_pages.append(generateLink() + str(i))
    i += 1
new_pages.pop(0)
new_pages.pop(0)
print(new_pages)

x = 0
soup_list = []
while (x <= 8):
    response = requests.get(new_pages[x])
    # print(response)
    x += 1
    for html in new_pages:
        html = BeautifulSoup(response.text, 'html.parser')
        new_images = html.find_all('img', attrs='resp-media')
        soup_list.append(html)
    for new_image in new_images:
        name = (uuid.uuid1())
        link = new_image['src']

        try:
            with open(str(name) + '.jpg', "wb") as f:
                img = requests.get(link)
                f.write(img.content)
        except Exception:
            pass
            print('bad url')


# url = 'https://icanhas.cheezburger.com'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# images = soup.find_all('img', attrs='resp-media')