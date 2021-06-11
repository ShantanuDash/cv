# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('main.pdf')
def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst
get_concat_v(images[0],images[1]).save('main.png','PNG')

#images[0].save('main.png','PNG')
'''
for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')
'''
