from PIL import Image, ImageFont, ImageDraw
from config import ParaDialog
import barcode
import numpy as np

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

def draw_bar(img,code,x,y,w, h,dh, dtxt, fs):
    bar=barcode.upc.UniversalProductCodeA(code.replace(' ',''),make_ean=True).to_ascii()
    bar=bar.replace('|','1').replace('|','1')
    d = ImageDraw.Draw(img)
    index=np.linspace(0,w,96)
    j=0

    for i in bar:
        if i=='1':fill='black'
        else : fill ='white'
        if j<11 or (j>44 and j<50) or j>84: d.rectangle([x+index[j],y,x+index[j+1],y+h+dh],fill)
        else: d.rectangle([x+index[j],y,x+index[j+1],y+h],fill)
        j+=1

    truetype=ImageFont.truetype('simfang.ttf',fs)
    fw = d.multiline_textsize(text=code,font=truetype)[0]
    d.text((x+(w-fw)/2,y+h+dh+dtxt), code, (0,0,0), font=truetype)
    del d

class BarObj(Rect):
	title = 'Barcode'
	def __init__(self, para=None):
		# code,x,y,w, h,dh, dtxt, fs
		if para is None: para = {'x':0, 'y':0, 'code':'123456789012', 
			'w':100, 'h':50, 'dh':10, 'mar':10, 'size':36,
			'font':'C:/Windows/Fonts/Microsoft YaHei UI/msyh.ttc'}
		self.para = para
		self.view = [(str, 'code', 'code', ''),
					 (int, (1,1024), 0, 'X', 'x', 'pix'),
					 (int, (1,1024), 0, 'Y', 'y', 'pix'),
					 (int, (1,1024), 0, 'width', 'w', 'pix'),
					 (int, (1,1024), 0, 'height', 'h', 'pix'),
					 (int, (1,1024), 0, 'dh', 'dh', 'pix'),
					 (int, (1,1024), 0, 'margin', 'mar', 'pix'),
					 (int, (1,200), 0, 'size', 'size', '')]

	def rect(self):
		p = self.para
		return (p['x']-2, -p['y']-p['h']-p['dh']-2), (p['w']+4, p['h']+p['dh']+4)

	def draw(self, image, para):
		draw_bar(image, para['code'], para['x'], para['y'], para['w'], 
			para['h'], para['dh'], para['mar'], para['size'])

	def __str__(self):
		return 'BAR>'+str(self.para)

def parserect(cont):
	title, para = cont.split('>')
	if title == 'TXT':
		return TextObj(eval(para))
	if title == 'BAR':
		return BarObj(eval(para))


if __name__ == '__main__':
	txt = TextObj()
	txt.size()