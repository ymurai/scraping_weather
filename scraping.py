# coding: utf-8

import Reference

Reference = Reference.Reference()
result = Reference.scraping()

# 確認
for i, num in enumerate(result):
  for num2, key in enumerate(result[i]):
    print (key, result[i][key])
