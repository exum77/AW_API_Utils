import Tkinter
from test import *
class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        LW = 10
        EW = 30
        # HOST
        label = Tkinter.Label(self,text="HOST",width=LW).grid(column=0,row=0)
        self.hostVar = Tkinter.StringVar()
        self.host = Tkinter.Entry(self,textvariable=self.hostVar,width=EW).grid(column=1,row=0)
        self.hostVar.set(u"https://as420.awmdm.com")       
        # API KEY
        label = Tkinter.Label(self,text="API KEY",width=LW).grid(column=2,row=0)
        self.keyVar = Tkinter.StringVar()
        self.key = Tkinter.Entry(self,textvariable=self.keyVar,width=EW).grid(column=3,row=0)
        self.keyVar.set(u"A8qzeuhVSLgphAUde2X6Pe+s/Ogi3fNOR69KkMApqTU=")

        # USER
        label = Tkinter.Label(self,text="USER",width=LW).grid(column=0,row=1)
        self.userVar = Tkinter.StringVar()
        self.user = Tkinter.Entry(self,textvariable=self.userVar,width=EW).grid(column=1,row=1)
        self.userVar.set(u"ATLANTAWIFI\TExum")
        # PASSWORD
        label = Tkinter.Label(self,text="PSWD",width=LW).grid(column=2,row=1)
        self.pswdVar = Tkinter.StringVar()
        self.pswd = Tkinter.Entry(self,textvariable=self.pswdVar,width=EW,show='*').grid(column=3,row=1)
        self.pswdVar.set(u"J$1jolly")

        # OG ID
        label = Tkinter.Label(self,text="OG ID",width=LW).grid(column=0,row=2)
        self.ogidVar = Tkinter.StringVar()
        self.ogid = Tkinter.Entry(self,textvariable=self.ogidVar,width=EW).grid(column=1,row=2)
        self.ogidVar.set(u"1244")
        # PIN
        label = Tkinter.Label(self,text="PIN",width=LW).grid(column=2,row=2)
        self.pinVar = Tkinter.StringVar()
        self.pin = Tkinter.Entry(self,textvariable=self.pinVar,width=EW,show='*').grid(column=3,row=2)
        self.pinVar.set(u"1111")

        button = Tkinter.Button(self,text=u"Get " + self.ogidVar.get() + " Structure",command=self.OnOGFetchClick).grid(column=0,row=3)
        self.OGlabelVar = Tkinter.StringVar()
        self.OGlabel = Tkinter.Message(self,textvariable=self.OGlabelVar,width=200).grid(column=0,row=4,columnspan=4,sticky='EW')
        #self.labelVar = Tkinter.StringVar()
        #label = Tkinter.Label(self,textvariable=self.labelVar,anchor="w",fg="white",bg="blue")
        #label.grid(column=0,row=1,columnspan=2,sticky='EW')
        #self.labelVar.set(u"Hello!")

        self.resizable(True,False)

    def OnOGFetchClick(self):
        self.OGlabelVar.set(displayTree(int(self.ogidVar.get())))

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
    
