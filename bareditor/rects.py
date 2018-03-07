from PIL import Image, ImageFont, ImageDraw
from config import ParaDialog

bufferimg = Image.new("RGB", (1,1), "white")

class Rect:
	def __init__(self):
		self.para = {'x':0, 'y':0}

	def setpos(self, x, y):
		self.para['x'], self.para['y'] = x, y

	def getpos(self):
		return self.para['x'], self.para['y']

	def getrect(self):pass

	def show(self, parent):
		self.dialog = ParaDialog(parent, self.title)
		self.dialog.init_view(self.view, self.para, True)
		self.dialog.set_handle(lambda x:parent.update())
		self.dialog.ShowModal()
		self.dialog.Destroy()

class TextObj(Rect):
	title = 'Text'
	def __init__(self, para=None):
		if para is None: para = {'x':0, 'y':0, 'txt':'TEXT', 'size':36, 
			'font':'C:/Windows/Fonts/Microsoft YaHei UI/msyh.ttc'}
		self.para = para
		self.view = [(str, 'text', 'txt', ''),
					 (int, (1,1024), 0, 'X', 'x', 'pix'),
					 (int, (1,1024), 0, 'Y', 'y', 'pix'),
					 (int, (1,200), 0, 'size', 'size', '')]

	def rect(self):
		p = self.para
		truetype=ImageFont.truetype(p['font'], p['size'])
		draw = ImageDraw.Draw(bufferimg)
		size = draw.multiline_textsize(p['txt'], font=truetype)
		del draw
		return (p['x'], -p['y']-size[1]-2), size

	def draw(self, image, para):
		draw = ImageDraw.Draw(image)
		truetype=ImageFont.truetype(self.para['font'], self.para['size'])
		draw.text((para['x'], para['y']), para['txt'], (0,0,0), font=truetype)
		del draw

	def __str__(self):
		return 'TXT>'+str(self.para)

def parserect(cont):
	title, para = cont.split('>')
	if title == 'TXT':
		return TextObj(eval(para))


if __name__ == '__main__':
	txt = TextObj()
	txt.size()