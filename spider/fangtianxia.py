#!usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup


def get_data(city):
    """获取数据"""

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    }
    url = "http://newhouse.cd.fang.com/house/s/piduqu/b1pa/?ctm=1.cd.xf_search.list_type.4"
    url2 = "http://newhouse.cd.fang.com/house/s/piduqu/b1pd/?ctm=2.cd.xf_search.list_type.4"
    url3 = "http://newhouse.cd.fang.com/house/s/piduqu/b1pd-b92/?ctm=1.cd.xf_search.page.2"
    url4 = "http://newhouse.cd.fang.com/house/s/piduqu/b1pd-b93/?ctm=1.cd.xf_search.page.4"
    url5 = "http://newhouse.cd.fang.com/house/s/piduqu/b1pd-b94/?ctm=1.cd.xf_search.page.6"
    house = []
    res = requests.get(url3, headers=headers)
    res = res.text.encode("ISO-8859-1")
    soup = BeautifulSoup(res, "html5lib")
    for i in soup.find_all(attrs={"class": "nlc_details"}):
        # house.append({i.text.strip("\t\n"): {}})
        print(i.text)
    # for i in soup.find_all(attrs={"class": "nhouse_price"}):
    #     if
    #     print("price: ", (i.text.strip("\t\n")))
    # for i in soup.find_all(attrs={"class": "address"}):
    #     print("address: ", (i.text.replace("\n", "").replace("\t", "")))



if __name__ == "__main__":
    print(get_data("piduqu"))