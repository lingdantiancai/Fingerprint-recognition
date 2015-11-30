import wx
import serial
ser = serial.Serial(7)
line = ser.readline()

f = open('d:/tt.txt', 'r')
a = f.read()
b = len(a)
f.close()
def roll():
    # roll the fingerprint and plus per time
    f = open('d:/tt.txt', 'r')
    a = f.read()
    b = len(a)
    f.close()
    b++
    while line: 
        line = ser.readline()
        serialprint.AppendText(line)
        if line.find("IIDD"):
            ser.write(b)
    
    f = open('d:/tt.txt', 'a')
    f.write('a')
    f.close


def recog(event):
    serialprint.AppendText(line)
    print 2

    

app = wx.App()
win = wx.Frame(None, title="Fingerprint Recognize", size=(410, 335))

rollButton = wx.Button(win, label='Roll', pos=(10,5), size=(155,50))
rollButton.Bind(wx.EVT_BUTTON, roll)

recognizeButton = wx.Button(win, label='Recognize' ,pos=(200,5), size=(160,50))
recognizeButton.Bind(wx.EVT_BUTTON, recog)

serialprint = wx.TextCtrl(win, pos=(10,80), size=(350,200), style=wx.TE_MULTILINE | wx.HSCROLL)

serialprint.AppendText("ÄãºÃ")
serialprint.SetDefaultStyle(wx.TextAttr(wx.RED))
serialprint.AppendText("Red text\n")




win.Show()
app.MainLoop()
