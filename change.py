from PIL import Image
im = Image.open("ID_RajivMurali.png")
im1 = im.convert('1')
im1.save('bw.png')


