import requests
from bs4 import BeautifulSoup
import pandas
import connect


ox_url = "https://www.ox.ac.uk/?page="
scraped_info_list = []
connect.connect(ox_url)

req = requests.get(ox_url)
content = req.content

print(content)
soup = BeautifulSoup(content, "html.parser")
discovers = soup.find_all("div", {"class": "link-block-bgimage-wrapper"})

for discover in discovers:
    discover_dict = {}
    discover_dict["name"] = discover.find("h2").text

    scraped_info_list.append(discover_dict)
    connect.insert_into_table(ox_url, tuple(discover_dict.values()))

dataFrame = pandas.DataFrame(scraped_info_list)
print("Creating csv file...")
dataFrame.to_csv("ox.csv")
connect.get_oxford_info(ox_url)