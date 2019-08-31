import locale
locale.setlocale(locale.LC_ALL,'C')

import tesserocr
from PIL import Image
image=Image.open('3-2.png')
print(tesserocr.image_to_text(image))
print(tesserocr.file_to_text('3-2.png'))