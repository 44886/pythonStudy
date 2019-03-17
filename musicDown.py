# coding=utf-8
# 44886
'''
这是一个强大的功能，用来下载音乐
目前支持下载的平台有：酷狗
'''
from urllib import parse
import requests
import os
from contextlib import closing


def kugou(url):
    # 三个模板
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    hash_url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash={}'
    header = {
        'User-Agent': ua
    }
    # 获取url中的hash
    if url.index(url) == -1:
        print('请输入正确的酷狗音乐地址！')
        sys.exit()

    hash1 = url[url.index("hash")+5:url.index("hash")+37]
    get(hash_url.format(hash1), header)


def get(foo, header):
    res = requests.get(foo, headers=header, stream=False, verify=False)
    audio = {'name': res.json()['data']['audio_name'], 'size': (res.json(
    )['data']['filesize']/1024*1024), 'downUrl': res.json()['data']['play_url']}
    down(audio['downUrl'], header, audio)


def down(foo, header, audio):
    savepath = "./"
    savename = audio['name'] + '.mp3'
    print('正在下载:%s' % savename.split('.')[0])
    r = requests.get(foo, headers=header, stream=True, verify=False)
    f = open(savepath+savename, "wb")
    temp_size = 0
    # chunk是指定每次写入的大小，每次只写了512byte

    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
            temp_size = temp_size+len(chunk)

            #############花哨的下载进度部分###############
            done = int(50 * temp_size / audio['size'])
            print("\r[%s%s]%d%%" % ("█"*done, " "*(50-done),
                                    100 * temp_size / audio['size']), end=" ")

    print('\n下载完成!')
    start()


def start():
    os.system("cls")
    print()
    print(' '*5, '+',  '-'*48, '+')
    print(' '*5, '|',  ' '*16, '万能音乐下载器', ' '*16, '|')
    print(' '*5, '|',  ' '*2, '支持平台：', ' '*34, '|')
    print(' '*5, '|',  ' '*4, '酷狗', ' '*38, '|')
    print(' '*5, '|',  ' '*48, '|')
    print(' '*5, '|',  ' '*2, '作者：陈建生 2019.03.17', ' '*21, '|')
    print(' '*5, '+',  '-'*48, '+')
    print()
    url = input('请复制音乐的试听地址,并按下回车:\n')
    urlList = list(parse.urlsplit(url))
    print(urlList)
    if urlList[0] == "http" or urlList[0] == "https":
        if urlList[1] == "www.kugou.com":
            kugou(url)
    else:
        print('请输入正确的音乐地址!')
    return False


start()
