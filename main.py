import pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep

sql_img = []
sql_link = []
sql_title = []
sql_address = []
sql_metro = []
sql_rooms = []
sql_area = []
sql_floor = []
sql_price = []
sql_comment = []

df_aparts = pandas.DataFrame(
    {'img': [], 'link': [], 'title': [], 'address': [], 'metro': [], 'rooms': [], 'area': [], 'floor': [],
     'comment': []})


def getApats(town, metro, type):
    url = f"https://realt.by/sale/flats/?page=1"
    data = requests.get(url)
    soup = BeautifulSoup(data.text, features="html.parser")
    maxPage = soup.find('div', class_='paging-list').findAll('a')
    maxPage = maxPage[len(maxPage) - 1].text.strip()

    print(maxPage)

    for p in range(1, int(4) + 1):
        print(p)
        url = f"https://realt.by/sale/flats/?page={p}"
        data = requests.get(url)
        soup = BeautifulSoup(data.text, features="html.parser")
        sleep(3)
        aparts = soup.findAll('div', class_='listing-item')
        allAparts = []

        for apart in aparts:
            try:
                link = apart.find('a', class_='teaser-title').get('href')
            except AttributeError:
                continue

            img = apart.find('img').get('data-original')
            title = apart.find('a', class_='teaser-title').get('title')
            address = apart.find('div', class_='location color-graydark').text.strip()

            try:
                metro = apart.find('div', class_='metro-green').text.strip()
            except:
                try:
                    metro = apart.find('div', class_='metro-blue').text.strip()
                except:
                    try:
                        metro = apart.find('div', class_='metro-red').text.strip()
                    except:
                        metro = "None"

            try:
                rooms = apart.find('div', class_='info-large').findAll('span')[0].text.strip()
                area = apart.find('div', class_='info-large').findAll('span')[1].text.strip()
                floor = apart.find('div', class_='info-large').findAll('span')[2].text.strip()
            except IndexError:
                rooms = "No info"
                area = "No info"
                floor = "No info"

            comment = apart.find('div', class_='info-text info-more').find('div',
                                                                           class_='fs-small color-dark').text.strip()

            try:
                price = apart.find('div', class_='col-auto text-truncate').text.strip()
            except AttributeError:
                price = "Договорная цена"

            sql_img.append(img)
            sql_link.append(link)
            sql_title.append(title)
            sql_address.append(address)
            sql_metro.append(metro)
            sql_rooms.append(rooms)
            sql_area.append(area)
            sql_floor.append(floor)
            sql_price.append(price)
            sql_comment.append(comment)
            allAparts.append([img, link, title, address, metro, rooms, area, floor, price, comment])

    print(allAparts)

    # To csv
    # header = ['img', 'link', 'title', 'address', 'metro', 'rooms', 'area', 'floor', 'comment']
    # df = pandas.DataFrame(allAparts, columns=header)
    # df.to_csv('/Users/karat/Desktop/Aparts.csv', sep=',', encoding='utf-8')

    df_aparts = pandas.DataFrame(
         {'img': sql_img, 'link': sql_link, 'title': sql_title, 'address': sql_address, 'metro': sql_metro,
          'rooms': sql_rooms, 'area': sql_area, 'floor': sql_floor, 'price': sql_price, 'comment': sql_comment})

    # To excel
    writer = pd.ExcelWriter('output.xlsx')
    df_aparts.to_excel(writer)
    writer.save()

if __name__ == '__main__':

    getApats(0, 0, 0)
