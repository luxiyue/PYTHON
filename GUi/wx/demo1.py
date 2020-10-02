import wx
#继承的是App类
class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None,title="Hello wyPython")
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()