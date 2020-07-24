class BaiduFanyi:
    def __init__(self,trans_str):
        self.trans_str = trans_str
        self.lang_detect_url = "http://fanyi.baidu.com/langdetect"
        self.trans_str = "http://fanyi.baidu.com/basetans"
        pass

    def run(self):
        pass
        #1.获取语言类型
            #1.1准备post的url地址,post_data
            #1.2发送post请求，获取响应
            #1.3提取语言类型
        #2.准备post的数据
        #3.发送请求，获取响应
        #4.提取翻译的结果

if  __name__ == '__main__':
    baidu_fanyi = BaiduFanyi()
    baidu_fanyi.run()