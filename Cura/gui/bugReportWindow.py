__copyright__ = "Copyright (C) 2013 David Braam - Released under terms of the AGPLv3 License"

import wx
from Cura.util import resources

class bugReportWindow(wx.Frame):
	def __init__(self, parent):
		super(bugReportWindow, self).__init__(parent, title=_("Report a bug"), style = wx.DEFAULT_DIALOG_STYLE|wx.FRAME_FLOAT_ON_PARENT)

		frameicon = wx.Icon(resources.getPathForImage('cura.ico'), wx.BITMAP_TYPE_ICO)
		self.SetIcon(frameicon)

		self.Bind(wx.EVT_CLOSE, self.OnClose)

		p = wx.Panel(self)
		self.panel = p
		s = wx.BoxSizer()
		self.SetSizer(s)
		s.Add(p)
		s = wx.BoxSizer(wx.VERTICAL)
		p.SetSizer(s)

		title = wx.StaticText(p, -1, _("How to report a problem ?"))
		title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
		s.Add(title, flag=wx.ALIGN_CENTRE|wx.BOTTOM|wx.TOP|wx.LEFT|wx.RIGHT, border=5)
		s.Add(wx.StaticText(p, -1, _("If you have noticed a problem, please first ensure you are using the latest version of Cura By Dagoma.")), flag=wx.ALIGN_CENTER|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=5)
		s.Add(wx.StaticText(p, -1, _("To report the problem to the staff, please follow the following link to create an Issue on GitHub.")), flag=wx.ALIGN_CENTER|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=5)


		self.Fit()

	def OnClose(self, e):
		self.Destroy()