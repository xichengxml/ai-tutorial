from PIL import Image
# ---------------------------
# @description 
# @author xichengxml
# @date 2020/9/4 上午 09:31
# ---------------------------


img = Image.open('img/img01.jpg')
img_copy = img.copy()
img_copy.thumbnail((192, 108))
img_copy.show()
