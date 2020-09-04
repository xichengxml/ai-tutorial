from PIL import Image
# ---------------------------
# @description 逆时针
# @author xichengxml
# @date 2020/9/4 上午 09:44
# ---------------------------


img = Image.open('img/img01.jpg')
img.rotate(90).show()
