'''
from PIL import Image
from glob import glob
fs = glob('*.png')
for i in fs:
    im = Image.open(i)
    im = im.resize((48,48))
    im.save(i)
'''

import barcode
bar=barcode.upc.UniversalProductCodeA('889532413997',  make_ean=True)
