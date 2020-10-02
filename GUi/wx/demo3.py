import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title = "创建StaticText类",pos=(100,100),size=(600,400))
        panel = wx.Panel(self)#创建画板
        title = wx.StaticText(panel,label="Python之禅———Tim Peters",pos=(100,20))#创建标题
        font = wx.Font(16,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)#并设置字体
        title.SetFont(font)
        #创建文本
        wx.StaticText(panel,label="优美胜于丑陋",pos=(50,50))
        wx.StaticText(panel, label="12312313", pos=(50, 70))
        wx.StaticText(panel, label="2425252245235", pos=(50, 90))

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()