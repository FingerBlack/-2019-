import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time, re

water_army = {}
oid_dict = {}
usr_dict = {}

def login():
    wd.get("https://www.weibo.com")
    print("Please login in, and input YES after that")
    waiter = input()
    #wd.refresh()
    print("login finished")


def getFansList(useroid):
    final = []
    for page in range(1, 6):
        url = 'https://weibo.com/p/' + useroid + '/follow?relate=fans&page=' + str(page) + '#Pl_Official_HisRelation__59'
        wd.get(url)
        time.sleep(3)
        fansList = wd.find_elements_by_css_selector('#Pl_Official_HisRelation__59 > div > div > div > div.follow_box > div.follow_inner > ul > li')
        print(fansList)
        regexp = re.compile(r'uid=([0-9]*?)&fnick=(.*?)&')
        for i in fansList:
            action_data = i.get_attribute('action-data')
            res = regexp.findall(action_data)
            for ele in res:
                final.append(list(ele))
            print(action_data)
        print(final)
    return final


if __name__ == "__main__":
    wd = webdriver.Chrome()
    wd.maximize_window()
    wd.set_page_load_timeout(5)
    login()
    water_army['用户3334557273'] = 1
    usr_dict['用户3334557273'] = '1005056867108671'
    oid_dict['1005056867108671'] = '用户3334557273'
    cur_oid = '1005056867108671'
    result = ['用户3334557273']
    cnt = int(input("Please input the number you need:"))
    cnt -= 1
    while cnt > 0:
        fans = getFansList(cur_oid)
        for i in fans:
            if i[1] in water_army:
                water_army[i[1]] += 1
            else:
                water_army[i[1]] = 1
                oid_dict[i[0]] = i[1]
                usr_dict[i[1]] = i[0]
        maxUser = ""
        for i in water_army.keys():
            if (not (i in result)) and (maxUser == "" or water_army[i] > water_army[maxUser]):
                maxUser = i
        result.append(i)
        cur_oid = usr_dict[maxUser]
        cnt -= 1
    print(result)


# 1005056867108671