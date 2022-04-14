# Aim:- Generate PDF file of your 3rd Semester Mark-sheet.
# Name:- Meghal Shah
# ID:- 20CS085

from PIL import Image

image_1 = Image.open(r'E:\Practical 10\20CS085.JPG')
im_1 = image_1.convert('RGB')
im_1.save(r'E:\Practical 10\20CS085.pdf', save_all=True)
print("PDF created", end = " ")
