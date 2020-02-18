import requests
import re
import urllib.request

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"

#获取cookie
def Get_Cookie(url):
    session = requests.Session()
    headers = {
        'user-agent': userAgent
    }
    session.get(url, headers=headers)
    Cookie_dic= dict(session.cookies)
    Cookie_str= "JSESSIONID" + "=" + Cookie_dic['JSESSIONID']
    return Cookie_str

def get_image(url,stuNum):
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        get_img = response.read()
        with open(str(stuNum)+".jpg","wb") as fp:
            fp.write(get_img)
        print("第"+ str(stuNum) +"张图片下载完成")
    except:
        print("第"+ str(stuNum) +"张图片下载失败")

url_page = "http://learn.upc.edu.cn/meol/common/script/preview/download_preview.jsp?fileid=1064539&resid=337995&lid=21198"
url_frame = "http://learn.upc.edu.cn/meol/common/script/preview/preview.jsp?fileid=1064539&resid=337995&lid=21198"
cookie = Get_Cookie(url_page)
headers = {
    "Cookie": cookie,
    "User-Agent": userAgent,
    }

#获取网页框架源码
frame_str = requests.get(url=url_frame, headers=headers)
frame_str = str(frame_str.text)

#提取并分割图片链接
picture_url_list = re.findall(r'var converbodyHtml = "(.*?)";',frame_str,re.S)
picture_url_str = "".join(picture_url_list)
picture_url_str = picture_url_str.split(",")

#下载图片
for i in range(len(picture_url_str)):
    get_image(picture_url_str[i],i)