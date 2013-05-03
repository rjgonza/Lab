#!/usr/bin/python
import wx
import sys
def load(event):
	if not filename.GetValue():
		popup()
		sys.exit(1)
	file = open(filename.GetValue())
	contents.SetValue(file.read())
	file.close()

def save(event):
	file = open(filename.GetValue(), 'w')
	confirm()
	file.write(contents.GetValue())
	file.close()

def popup():
	wx.MessageBox("There is no file specified you fool!\nShutting down...", "ERROR",
		wx.OK | wx.ICON_ERROR)

def confirm():
	dlg = wx.SingleChoiceDialog(
	self, "Confirmation", "Are you sure you want to overwrite the file " + file,
	['Yes', 'No'],
	wx.CHOICEDLG_STYLE
	)
	
	if flg.ShowModal() == wx.ID_OK:
		self.log.WriteText("You selected: %s\n" % dlg.GetStringSelection())
	dlg.Destroy()	

app = wx.App()
win = wx.Frame(None, title="Config Editor", size=(410, 335))

bkg = wx.Panel(win)

loadButton = wx.Button(bkg, label='Open')
loadButton.Bind(wx.EVT_BUTTON, load)

saveButton = wx.Button(bkg, label='Save')
saveButton.Bind(wx.EVT_BUTTON, save)

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1,
	flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()
