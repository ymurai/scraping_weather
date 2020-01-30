# coding: utf-8

import requests
from bs4 import BeautifulSoup

class Reference:

  URL = "https://weather.yahoo.co.jp/weather/"
  
  # スクレイピングして結果を取得
  # 戻り値：結果をレコードにして返す
  def scraping(self):

    # HTMLの取得
    r = requests.get(self.URL)
    soup = BeautifulSoup(r.content, "html.parser")

    # タグの解析
    data = soup.find("div", "mapJp").findAll("li", "point")

    result = {}
    for i, value in enumerate(data):
      name = value.find("dt").text
      weather = value.find("p", "icon").find("img")["alt"] # altをとりたい
      temp_high = value.find("p", "temp").find("em", "high").text
      temp_low = value.find("p", "temp").find("em", "low").text
      precip = value.find("p", "precip").text

      result[i] = {
          'name':       name,
          'weather':    weather,
          'temp_high':  temp_high,
          'temp_low':   temp_low,
          'precip':     precip
      }

    return result
