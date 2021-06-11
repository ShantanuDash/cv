# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('main.pdf')
images.save('main.png','PNG')
'''
for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')
'''
