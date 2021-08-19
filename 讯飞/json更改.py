import time
from pyaudio import PyAudio,paInt16
from urllib.request import urlopen,Request    #专门处理http协议的模块
import json
import base64


def record_audio():  #输入音频
    pa = PyAudio() #设备实例化
    equip = pa.open(
        format=paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=1024,
    ) #打开设备，并且支持输入
    data = [] #存储未来的语音输入
        #一截一截的语音数据  [b'1',b'2',]
    times = 0 #用来控制用户输入语音长度的
    start = time.time()
    while times < 50: #3S
        data.append(equip.read(1024)) #读取设备中此时的语音数据
        times += 1
    end = time.time()
    print('[TALK] %.2f' % (end - start)) #%.2f 保留2位小数点有效位数字
    data = b''.join(data) #完整的音频流数据
    equip.close()
    pa.terminate() #关闭设备实例
    return data

def baidu_token():
    API_Key = 'oAcBP47GDDpj6XIHWmcSkeRi'
    Secret_Key = 'ba2EKROswCy6KXzLdTpnGqPnPhHSFHU7'
    grant_type = 'client_credentials'
    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=%s&client_id=%s&client_secret=%s'
    response = json.loads(urlopen(url % (grant_type,API_Key,Secret_Key)).read().decode())
    access_token = response['access_token']
    return access_token

def baidu_fenxi(data):
    url = 'http://vop.baidu.com/server_api'
    data_len = len(data)
    audio_data = base64.b64encode(data).decode()
    access_token = baidu_token()
    post_data = json.dumps({
        "format":"wav",
        "rate":16000,
        "dev_pid":1536,
        "channel":1,
        "token":access_token,
        "cuid":"00-50-56-C0-00-08",
        "len":data_len,
        "speech":audio_data,
    }).encode() #变为json的二进制
    headers = {'Content-Type':'application/json'}
    req = Request(url=url,headers=headers,data=post_data)
    result = json.loads(urlopen(req).read().decode()).get('result')
    if result:
        return result[0]
    else:
        return None

def main():
    print("语音识别开始，请在三秒后开始说话!")
    time.sleep(1)
    print("3！")
    time.sleep(1)
    print("2！")
    time.sleep(1)
    print("1!")
    time.sleep(1)
    print("开始说话！！！")

    data = record_audio()
    res = baidu_fenxi(data)
    print(res)

if __name__ == '__main__':
    #程序入口
    main()