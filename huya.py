# 获取虎牙直播的真实流媒体地址。
from typing import List, Any, Union

import requests
import re


def get_real_url(rid):
    room_url = 'https://m.huya.com/' + str(rid)
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36'
    }

    response = requests.get(url=room_url, headers=header)
    response.encoding = 'utf-8'
    pattern = r"hasvedio: '([\s\S]*)2500([\s\S]*.m3u8?[\s\S]*?)'"
    p = r"var videoTitle = '([\s\S]*?)';"
    # title = response.text.var ANTHOR_NICK
    title = re.findall(p, response.text, re.I)
    video_title = title[0]
    #print (video_title)
    result = re.findall(pattern, response.text, re.I)
    if result:
        real_url = '标清:\b'+ result[0][0]+ '2500' + result[0][1] +'\n\n'\
                   '标清:\b'+ result[0][0]+ '3500' + result[0][1] +'\n\n'\
                   '蓝光4M:\b' + result[0][0]+ '4000' + result[0][1]
        # real_url = re.sub(r'_1200[\s\S]*.m3u8', '.m3u8', result[0])
    else:
        real_url = '未开播或直播间不存在'
    return [real_url, video_title]


rid = input('请输入虎牙房间号：\n')
real_url = get_real_url(rid)[0]
video_title = get_real_url(rid)[1]
print('\n' + video_title + '的直播间源地址为：\n' + real_url + '\n')
input('输入任意键退出')
