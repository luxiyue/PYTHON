# class EX(object):
#     def pdd(self):
#         try:
#             a = int(input("请输入一个整数"))
#             return 1
#         except ValueError:
#             print("你输入的不是整数，请重新输入！！")
#             return 0
#
# if __name__ == '__main__':
#     ex = EX()
#     while True:
#         b = ex.pdd()
#         if b == 1:
#             break

import datetime
def talker():
    print("这是一个陪你聊天的小程序！！")
    i = 0  # 记录对话次数
    while True:
        print(datetime.datetime.now())
        message = input("卢泽龙：")
        if message.lower().find("hi") != -1 or message.lower().find("hello") != -1 :
            print("lulu:Hi~,龙龙今天过得愉快吗？")
        elif message.find("不愉快") != -1 or message.find("不开心") != -1:
            print("lulu:别难过鸭！龙龙你是最棒的！，lulu可以永远陪你哦~嘻嘻")
        elif message.find("愉快") != -1 or message.find("开心") != -1:
            print("lulu:emmmmm~~~开心就好")
        elif message.find("喜欢你") != -1 or message.find("爱你") != -1:
            print("lulu:mua~我也超级喜欢你，【/害羞】")
        elif message.find("喜欢我什么") != -1:
            print("lulu:你高大威猛，英俊潇洒，这世界上所有好的词汇都可以形容你，所以我对你欲罢不能~")
        elif message.find("嘿")!=-1 or message.find("哈")!=-1 or message.find("ha")!=-1 or message.find("hei")!=-1 or message.find("嘻")!=-1:
            print("lulu:你在笑啥呀宝贝？是不是觉得我很说话很好听~")
        elif message.find("嗯")!=-1:
            print("lulu:那是必须的，hhhhh")
        else:
            print("人工智能还未完善")
        if i==5 :
            print("不好意思，我先去洗个澡~，待会再聊")
            break
        i += 1

talker()