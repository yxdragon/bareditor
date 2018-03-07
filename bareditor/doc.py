from PIL import Image, ImageFont, ImageDraw

class Doc:
	def __init__(self):
		self.rects = []
		self.para = {'w':256, 'h':100}
		self.cur = None

	def save(self):pass

	def add(self, obj, pos=None):
		if pos is None: pos = (
			self.para['w']//2, self.para['h']//2)
		obj.setpos(*pos)
		self.rects.append(obj)

	def remove(self, obj):
		if self.cur is obj: self.cur = None
		del self.rects[self.rects.index(obj)]

	def img(self):
		size = (self.para['w'], self.para['h'])
		image = Image.new("RGB", size, "white")
		for i in self.rects:
			i.draw(image, i.para)
		draw = ImageDraw.Draw(image)

		#truetype=ImageFont.truetype('C:/Windows/Fonts/Microsoft YaHei UI/msyh.ttc', 36)
		#draw.text((10, 0), 'ABCD', (0,0,0), font=truetype)
		return image

	def pick(self, x, y):
		for r in self.rects:
			p1, p2 = r.rect()
			if x<p1[0] or x>p1[0]+p2[0]: continue
			if y<p1[1] or y>p1[1]+p2[1]: continue
			self.cur = r
			return self.cur
		self.cur = None


if __name__ == '__main__':
	doc = Doc()
	doc.img().show()