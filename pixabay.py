import requests
import re
import random
import time
import os

"""
本文原创：pk哥，公众号：Python知识圈（id：PythonCircle），如需转载，请关注公众号，联系pk哥授权。
「Python知识圈」公众号定时分享大量有趣有料的 Python 爬虫和实战项目，值得你的关注，关注后回复1024有惊喜哦！
"""


def get_urls(url):
    headers = {
             'User-Agent':
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
             '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    html = requests.get(url, headers=headers).text
    urls = re.compile(r'data-lazy-srcset="(.*?)"')
    res = re.findall(urls, html)
    img_urls = []
    for u in res:
        img_url = str(u).split(',')[0].strip(' 1x')
        img_urls.append(img_url)
    return img_urls


# 创建不同的文件夹储存图片
def mkdir(directory):
    isExists = os.path.exists(r'/Users/brucepk/Pictures/素材图片/{}'.format(directory))
    if not isExists:
        print('创建 %s 目录' % directory)
        os.makedirs(r'/Users/brucepk/Pictures/素材图片/{}'.format(directory))   # 创建目录
        os.chdir(r'/Users/brucepk/Pictures/素材图片/{}'.format(directory))      # 切换到创建的文件夹
        return True
    else:
        print('目录 %s 已存在，即将保存！' % directory)
        return False


def download(filename, url):
    with open(filename, 'wb+') as f:
        try:
            f.write(requests.get(url).content)
            print('成功下载图片：', filename)
        except:
            print('下载失败：', filename)
            
"""
本文原创：pk哥，公众号：Python知识圈（id：PythonCircle），如需转载，请关注公众号，联系pk哥授权。
「Python知识圈」公众号定时分享大量有趣有料的 Python 爬虫和实战项目，值得你的关注，关注后回复1024有惊喜哦！
"""

if __name__ == '__main__':
    directory = input('输出你要下载的图片的英文关键字：')
    for num in range(1, 6):
        search_url = 'https://pixabay.com/images/search/{}/?pagi={}'.format(directory, num)  # 拼接每页的链接
        mkdir(directory)
        for url in get_urls(search_url):
            filename = r'/Users/brucepk/Pictures/素材图片/{}/'.format(directory) + url.split('/')[-1]  # 图片的路径
            download(filename, url)
        print('第%s页已爬取' % num)
        time.sleep(int(format(random.randint(3, 10))))     # 随机等待时间
        
 
"""
查看更多有趣的项目请关注公众号「Python知识圈」
或者访问链接：https://github.com/Brucepk/download-no-copyright-image
"""









