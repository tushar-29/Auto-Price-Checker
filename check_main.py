import requests
from bs4 import BeautifulSoup
import lxml


url = 'https://www.amazon.in/ASUS-GTX-1650-Graphics-Windows-FA506IH-AL047T/dp/B088R54S2R'
header_para = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                        "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(url=url, headers=header_para)
response.raise_for_status()
soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())
html_check = soup.find(name="div", id="availability")
print(html_check)
