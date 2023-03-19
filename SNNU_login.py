import requests
import sys
from urllib import request
from http import cookiejar

def Get_cookie(url):
    """ 获取JSESSIONID
    """
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler=request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    # 此处的open方法打开网页
    response = opener.open(url)
    # 打印cookie信息
    for item in cookie:
        if item.name == 'JSESSIONID':
            out = item.value
    
    out = 'JSESSIONID=' + out
    return out

def Login(account, password):
    #登录地址
    post_addr="http://202.117.144.205:8601/snnuportal/login"

    #获取cookie
    cookie = Get_cookie(post_addr)


    post_data = {
            'sourceurl': 'http://www.gstatic.com/generate_204',
            'account': account,
            'password': password,
            'yys': '',
        }

    response = requests.post(post_addr, data=post_data)

    return 'OK'

# 输入自己的学号以及密码
account = '*****'
password = '*****'

result = Login(account, password)
print(result)





