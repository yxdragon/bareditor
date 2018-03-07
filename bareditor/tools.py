from config import ParaDialog
from doc import Doc
from rects import *
import wx

class Tool:
	title = 'title'
	para = None
	view = None

	def preview(self, parent, doc, para=None):
		self.run(parent, doc, para)
		parent.update()

	def show(self, parent, doc):
		self.dialog = ParaDialog(parent, self.title)
		self.dialog.init_view(self.view, self.para, True)
		self.dialog.set_handle(lambda x:self.preview(parent,  doc, self.para))

		if self.dialog.ShowModal() == wx.ID_OK:
			self.run(parent, doc, self.para)
			parent.update()
		self.dialog.Destroy()

	def start(self, parent, doc):
		if self.para is None:
			self.run(parent, doc, None)
			parent.update()
		else:
			self.show(parent, doc)

class NewTool(Tool):
	para = {'w':256, 'h':256}
	view = [(int, (100,1000), 0, 'width', 'w', 'pix'),
			(int, (100,1000), 0, 'height', 'h', 'pix')]
	img = 'imgdata/new.png'
	title = 'New'

	def run(self, parent, doc, para):
		parent.doc = Doc()
		parent.doc.para = {'w':para['w'], 'h':para['h']}

class OpenTool(Tool):
	img = 'imgdata/open.png'
	title = 'Open'
	def run(self, parent, doc, para):pass

class SetTool(Tool):
	para = {'w':256, 'h':256}
	view = [(int, (100,1000), 0, 'width', 'w', 'pix'),
			(int, (100,1000), 0, 'height', 'h', 'pix')]
	img = 'imgdata/set.png'
	title = 'Set'
	def run(self, parent, doc, para):
		doc.para = {'w':para['w'], 'h':para['h']}

class AddText(Tool):
	img = 'imgdata/text.png'
	title = 'Text'

	def run(self, parent, doc, para):
		doc.add(TextObj())
		print('ddd')

class ZoomIn(Tool):
	img = 'imgdata/zoomin.png'
	title = 'ZoomIn'

class ZoomOut(Tool):
	img = 'imgdata/zoomout.png'
	title = 'ZoomOut'
	
tools = [NewTool, OpenTool, SetTool, AddText, ZoomIn, ZoomOut]