from PIL import Image
# ---------------------------
# @description 
# @author xichengxml
# @date 2020/9/4 上午 08:52
# ---------------------------


img = Image.open('img/img01.jpg')
Image.eval(img, lambda i:i * 2).show()
