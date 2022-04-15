# coding=utf-8
import unittest
from imp import reload
from time import sleep

from selenium.webdriver.common.by import By

'''
python3.0
可以直接用webdriver_manager自动安装驱动
python 2.7
环境配置参考：https://zhuanlan.zhihu.com/p/61312218
需要安装Chrome驱动，并且去除与webdriver_manager有关的代码
改为driver = webdriver.Chrome()
并且加上sys.setdefaultencoding('utf-8')
'''
import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys
print (sys.path)
'''
# 谷歌浏览器驱动的代码
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# 火狐浏览器驱动的代码

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# edge浏览器驱动的代码
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())

'''

from webdriver_manager.chrome import ChromeDriverManager


reload(sys)


def get_content():
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    title_list = []
    temp_data = []
    out_pd = pandas.DataFrame()
    for page in range(3):
        page = page + 1
        driver.get("http://fz.people.com.cn/skygb/sk/index.php/Index/index/" + str(page) + "?p=1")
        title = driver.find_elements(by=By.TAG_NAME, value='th')
        if page == 1:
            for i in title:
                if (i.text != ""):
                    print (i.text)
                    title_list.append(i.text)
            print(title)
            data = pandas.DataFrame(columns=title_list)
            out_pd=data

        content = driver.find_element(by=By.CLASS_NAME, value="jc_a").find_element(by=By.TAG_NAME, value="tbody").find_elements(by=By.TAG_NAME, value="tr")
        for i in content:
            temp = []
            span=i.find_elements(by=By.TAG_NAME, value="span")
            for n in range(7):
                if (span[n].text == ""):
                    temp.append(" ")
                    continue
                print(span[n].text)
                temp.append(span[n].text)
            size=out_pd.index.size
            out_pd.loc[size]=temp
        print(out_pd)
    driver.close()
    out_pd.to_csv("result.csv", sep=',',index="false")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        get_content()
        print("爬取成功")
    except:
        print("爬取失败")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
