from PIL import Image
# ---------------------------
# @description 
# @author xichengxml
# @date 2020/9/4 上午 09:39
# ---------------------------


img = Image.open("img/img01.jpg")

# 复制
copy01 = img.copy()
copy02 = img.copy()

# 剪切
crop = copy01.crop((0, 0, 120, 120))

# 粘贴
copy02.paste(crop, (0, 80))

copy02.show()
