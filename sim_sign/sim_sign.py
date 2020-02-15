import requests
import urllib.request
import time
import re
import numpy
import os
from PIL import Image

#获取cookie
def Get_Cookie(url):
    session = requests.Session()
    headers = {
        'user-agent': userAgent
    }
   
    session.get(url, headers=headers)
    
    #获取当前的Cookie
    Cookie_dic= dict(session.cookies)
    #print(Cookie_dic)
    Cookie_str= "JSESSIONID" + "=" + Cookie_dic['JSESSIONID'] + ";" + "SERVERID" + "=" + Cookie_dic['SERVERID']
    #print(Cookie_str)

    return Cookie_str


#部分参数
main_url = "http://jwxt.wust.edu.cn/whkjdx/"
verify_image_url ="http://jwxt.wust.edu.cn/whkjdx/verifycode.servlet"  #验证码图片地址
userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
#获取cookie
verify_cookie = Get_Cookie(main_url)
header = {
    "Accept":"text/html, application/xhtml+xml, image/jxr, */*",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN",
    "Content-Length":"94",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": verify_cookie,
    "Host":"jwxt.wust.edu.cn",
    "Pragma":"no-cache",
    "Proxy-Connection":"Keep-Alive",
    "Referer":"http://jwxt.wust.edu.cn/whkjdx/",
    'User-Agent':userAgent,
}


#下载处理验证码图片
def download_img(img_url):
    header = {  
        "Accept": "image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN",
        "Cookie": verify_cookie,
        "Host": "jwxt.wust.edu.cn",
        "Proxy-Connection": "Keep-Alive",
        "Referer": "http://jwxt.wust.edu.cn/whkjdx/",
        "User-Agent": userAgent,
    } # 设置http header
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        img_name = "verify_image.jpg"
        filename = img_name
        print("验证码图片获取成功")
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read()) # 将内容写入图片
            return filename
    except:
        print("验证码图片获取错误")
        return "failed"


#模仿登录

def mafengwoLogin(account, password):
    print ("开始模拟登录")
    verify_image_filename = download_img(verify_image_url)
    verify_image = Image.open(verify_image_filename)
    verify_image.show()
    verify_code = input('请输入验证码：')

    postUrl = "http://jwxt.wust.edu.cn/whkjdx/Logon.do?method=logon"
    postData = {
        "PASSWORD":password, 
        "RANDOMCODE":verify_code, 
        "useDogCode":"",
        "useDogCode":"", 
        "USERNAME":account,
        "x":"1",
        "y":"13",
    }
    responseRes = requests.post(postUrl, data = postData, headers = header)
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    #以上为登录部分

    print("登陆成功")
    
    #下面我也不知道为什么这样处理。。。
    url_bz = "http://jwxt.wust.edu.cn/whkjdx/Logon.do?method=logonBySSO"
    header_bz = {
        "Accept-Encoding": "gzip",
        "User-Agent": userAgent,
        "Cookie": verify_cookie,
        "Host": "jwxt.wust.edu.cn",
        "Connection": "Keep-Alive",
    }
    requests.get(url=url_bz, headers=header_bz)
    #response_bz = requests.get(url=url_bz, headers=header_bz)
    # print(f"statusCode = {response_bz.status_code}")
    # print(f"text = {response_bz.text}")

    #获取成绩页源码

    url_grade = "http://jwxt.wust.edu.cn/whkjdx/xszqcjglAction.do?method=queryxscj"
    header_grade = {
        "Accept-Encoding": "gzip",
        "User-Agent": userAgent,
        "Cookie": verify_cookie,
        "Host": "jwxt.wust.edu.cn",
        "Connection": "Keep-Alive",
    }
    response_grade = requests.get(url=url_grade, headers=header_grade)
    print(f"statusCode = {response_grade.status_code}")
    print(f"text = {response_grade.text}")

    #从源码中提取成绩信息

    str_grade = response_grade.text
    grade_person_name = re.findall(r'" >([\u4E00-\u9FA5]+)</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="120" title="',str_grade,re.S)[0]
    grade_mess_list = re.findall(r'<td  width="45" height="23" style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" >&nbsp;(\d+)</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*?" >.*?</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*?" >.*?</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*?" >(.*?)</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*?" >(.*?)</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*?" >(.*?)</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" (.*?)</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*?" >(.*?)</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*?" >(.*?)</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*?" >(.*?)</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title="[\d+\.]+" >([\d+\.]+)</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title="[\u4E00-\u9FA5]+" >([\u4E00-\u9FA5]+)</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" (.*?)</td><td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*?" >(.*?)</td></tr>',str_grade,re.S)
    x = numpy.array(grade_mess_list)

    header_grade_text = "共查询到" + grade_person_name + "的成绩信息" + str(x.shape[0]) + "条："

     #将成绩信息写入grade.txt文件
    fb = open('grade.txt','w',encoding='utf-8')
    fb.write(header_grade_text)

    print(header_grade_text)

    for i in range(len(grade_mess_list)):
        print(grade_mess_list[i])
        grade_mess_str = "".join(grade_mess_list[i])
        fb.write("\n")
        fb.write(grade_mess_str)
    
    os.system("pause")

        

if __name__ == "__main__":
    self_username = input("请输入账号：")
    self_password = input("请输入密码：")
    mafengwoLogin(self_username, self_password)
    