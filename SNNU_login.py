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
    response = opener.open(post_addr)
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

    #构造头部信息
    post_header={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '67',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cookie,
            'DNT': '1',
            'Host': '202.117.144.205:8601',
            'Origin': 'http://202.117.144.205:8601',
            'Referer': 'http://202.117.144.205:8601/snnuportal/login.jsp',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }

    post_data = {
            'sourceurl': 'http://www.gstatic.com/generate_204',
            'account': account,
            'password': password,
            'yys': '',
        }

    response = requests.post(post_addr, data=post_data, headers=post_header)

    return 'OK'

# 输入自己的学号以及密码
account = '********'
password = '**********'

result = Login(account, password)
print(result)





