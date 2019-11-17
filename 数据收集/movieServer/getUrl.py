import requests
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

def check_ip(ip):
    options = Options()
    options.headless = True
    options.add_argument('--proxy-server=http://' + ip)
    driver = webdriver.Firefox(options=options)
    driver.get('https://movie.douban.com')
    try:
        element = driver.find_element_by_name('search_text')
    except NoSuchElementException as e:
        return False
    else:
        return True



city_list = ['广东', '江苏', '山东', '浙江', '福建', '上海', '北京', '天津', '海南', '河北',
       '南京', '镇江', '常州', '无锡', '苏州', '徐州', '连云港', '淮安', '盐城', '扬州',
       '泰州', '南通', '宿迁','济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁',
       '泰安', '威海', '日照','杭州', '嘉兴', '湖州', '宁波', '金华', '温州', '丽水', '绍兴',
       '衢州', '舟山', '台州','广州', '深圳', '汕头', '惠州', '珠海', '揭阳', '佛山', '河源',
       '阳江', '茂名']


for city in city_list:
    print('*'*15+'\n正在处理{}的ip'.format(city))
    APIurl='http://lab.crossincode.com/proxy/get/' + '?num=20&v_num=1&loc={}'.format(city)
    response = requests.post(APIurl)
    with open('url.txt', 'a') as f:
        for dict_ip in response.json()['proxies']:
            ip = dict_ip['http']
            f.write(ip)
            # if check_ip(ip):
            #     print(ip+"可用")
            #     f.write(ip + '\n')
            # else:
            #     print(ip+'不可用')
    sleep(30)
