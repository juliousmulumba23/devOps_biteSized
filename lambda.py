import requests
import bs4
from PIL import Image

result = requests.get("https://example.com/")

print(type(result))

print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)

blue = Image.open("blues.jpg")
blue.putalpha(800)

red = Image.open("reds.png")
red.putalpha(118)

blue.paste(im=red,box=(0,0),mask=red)
blue.show()


print(red.size)
