#coding:utf-8
import urllib2
import urllib
import re

username = "学号"
password = "密码"

def check():
    try:
        urllib2.urlopen('http://gw.bnu.edu.cn', timeout=0.02)
        return True
    except urllib2.URLError as err:
        return False

def login():
    posturl = "http://gw.bnu.edu.cn:803/srun_portal_phone.php?ac_id=1&"
    header = {
        "User-Agen": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36",
        "Referer": "http://gw.bnu.edu.cn:803/srun_portal_phone.php?ac_id=1&"
    }
    postData = {
        "action": "login",
        "ac_id": "1",
        "user_ip": "",
        "nas_ip": "",
        "user_mac": "",
        "url": "",
        "username": username,
        "password": password,
        "save_me": "1"
    }
    postData = urllib.urlencode(postData)
    request = urllib2.Request(posturl, postData, header)
    response = urllib2.urlopen(request)
    return response.read()

def force_logout():
    postData_logout = {
        "action": "logout",
        "username": username,
        "password": password,
        "ajax": "1"
    }
    postData_logout = urllib.urlencode(postData_logout)
    posturl_logout = "http://172.16.202.201:802/include/auth_action.php"
    header_logout = {
        "User-Agen": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36",
        "Referer": "http://gw.bnu.edu.cn:803/srun_portal_phone.php?ac_id=1&"
    }
    request_logout = urllib2.Request(posturl_logout, postData_logout, header_logout)
    response_logout = urllib2.urlopen(request_logout)

if check():
    content = login()
    if len(re.findall('成功', content)) == 0:
        force_logout()
        content = login()
        m = re.findall('成功', content)
        if len(m) == 0:
            print '没得救了，充钱吧'
        else:
            print '登陆成功，已全部下线'
    else:
        print "登陆成功"
else:
    print '网络连接失败，请检查网络连接'
