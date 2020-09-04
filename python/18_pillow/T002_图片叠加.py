from PIL import Image
# ---------------------------
# @description 
# @author xichengxml
# @date 2020/9/4 上午 08:36
# ---------------------------


img = Image.open('img/img01.jpg').convert(mode='RGB')
img2 = Image.new('RGB', img.size, 'GREEN')
Image.blend(img, img2, alpha=0.5).show()

