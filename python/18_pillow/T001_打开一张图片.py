from PIL import Image

# ---------------------------
# @description 
# @author xichengxml
# @date 2020/9/4 上午 08:13
# ---------------------------


img = Image.open('img/img01.jpg')
img.show()
print('格式: ', img.format)
print('尺寸: ', img.size)
print('宽: %s, 高: %s' % (img.width, img.height))
print('像素信息', img.getpixel((100, 100)))
