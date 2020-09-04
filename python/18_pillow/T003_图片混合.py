from PIL import Image
# ---------------------------
# @description 
# @author xichengxml
# @date 2020/9/4 上午 08:44
# ---------------------------


img = Image.open('img/img01.jpg')
img2 = Image.open('img/img02.jpg')
r, g, b = img2.split()
Image.composite(img, img2, b).show()
