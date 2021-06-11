# import module
from pdf2image import convert_from_path
from PIL import Image
from PIL import ImageChops

# Store Pdf with convert_from_path function
images = convert_from_path('main.pdf')

#function to concat pages
def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

#removing white spaces
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
images[0] = trim(images[0])
images[1] = trim(images[1])

get_concat_v(images[0],images[1]).save('main.png','PNG')

#images[0].save('main.png','PNG')
'''
for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')
'''
