#!usr/bin/env python
# _*_ coding:utf-8 _*_

import json
import requests
from math import ceil
from bs4 import BeautifulSoup


def get_data(city):
    """获取数据"""

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    }
    # # 郫都区
    # url2 = "http://newhouse.cd.fang.com/house/s/piduqu/b1pd/?ctm=2.cd.xf_search.list_type.4"
    # url3 = "http://newhouse.cd.fang.com/house/s/piduqu/b1pd-b92/?ctm=1.cd.xf_search.page.2"
    # url4 = "http://newhouse.cd.fang.com/house/s/piduqu/b1pd-b93/?ctm=1.cd.xf_search.page.4"
    # # url5 = "http://newhouse.cd.fang.com/house/s/piduqu/b1pd-b94/?ctm=1.cd.xf_search.page.6"
    # # 温江
    # urlw1 = "http://newhouse.cd.fang.com/house/s/wenjiang/b1pd/?ctm=1.cd.xf_search.list_type.4"
    # urlw2 = "http://newhouse.cd.fang.com/house/s/wenjiang/b1pd-b92/"
    url = "http://newhouse.cd.fang.com/house/s/{}/b1pd-b91/".format(city)
    house = {}
    res = requests.get(url, headers=headers)
    res = res.text.encode("ISO-8859-1")
    soup = BeautifulSoup(res, "html5lib")
    n = ceil(int(soup.find(attrs={"class": "page"}).strong.text)/20)
    print(n, type(n))
    page = 1
    while page < n:
        url = "http://newhouse.cd.fang.com/house/s/{}/b1pd-b9{}/".format(city, page)
        res = requests.get(url, headers=headers)
        res = res.text.encode("ISO-8859-1")
        soup = BeautifulSoup(res, "html5lib")
        for i in soup.find_all(attrs={"class": "nlc_details"}):
            # house.append({i.text.strip("\t\n"): {}})
            name = i.find(attrs={"class": "nlcd_name"}).text.strip("\t\n")
            address = i.find(attrs={"class": "address"}).a["title"]
            price = i.find(attrs={"class": "nhouse_price"}).text.strip("\t\n")
            if name in house:
                if house.get(name).get("price") == price:
                    pass
                else:
                    house[name]["price"] = price
            else:
                house.update(
                    {name: {
                        "price": price,
                        "address": address
                    }})
        page += 1
    print(len(house))
    return json.dumps(house)
    # for i in soup.find_all(attrs={"class": "nhouse_price"}):
    #     if
    #     print("price: ", (i.text.strip("\t\n")))
    # for i in soup.find_all(attrs={"class": "address"}):
    #     print("address: ", (i.text.replace("\n", "").replace("\t", "")))
    
    
def cdlr(year=2017):
    """成都市国土资源局土地出让结果"""

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }
    url = "http://www.cdlr.gov.cn/second/zpggg.aspx"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html5lib")
    url_pool = []
    for i in soup.find_all(attrs={"style": "padding-left:5px;"}):
        if "一览表" in i.a["title"]:
            url_node = "http://www.cdlr.gov.cn" + i.a["href"][2:]
            url_pool.append(url_node)
    # print(url_pool)
    data = {}
    for url in url_pool:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html5lib")
        s = soup.find_all("td")
        for i in range(len(s)):
            if (i-1) % 7 == 0:
                # print(url)
                data.update({
                    s[i].text: [s[i+1].text, s[i+2].text, s[i+3].text, s[i+3].text, s[i+4].text, s[i+5].text]
                })
    print(json.dumps(data))

if __name__ == "__main__":
    print(get_data("wuhou"))
