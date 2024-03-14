from PIL import Image

# 读取六张图片

# 获取每张图片的尺寸
width, height = (960,540)
image2 = Image.open("merge_image/1697956416281_2.png").resize((width, height))
image1 = Image.open("merge_image/1697956416181_1.png").resize((width, height))
image3 = Image.open("merge_image/1697956416381_3.png").resize((width, height))
image5 = Image.open("merge_image/1697956416581_5.png").resize((width, height))
image4 = Image.open("merge_image/1697956416480_4.png").resize((width, height))
image6 = Image.open("merge_image/1697956416681_6.png").resize((width, height))

# 获取每张图片的尺寸
width, height = image1.size

# 计算合并后图像的尺寸
merged_width = width * 3
merged_height = height * 2

# 创建一个新的大图像
merged_image = Image.new("RGB", (merged_width, merged_height))

# 将六张图片按照排列顺序粘贴到新的大图像上
merged_image.paste(image2, (0, 0))
merged_image.paste(image1, (width, 0))
merged_image.paste(image3, (2*width, 0))
merged_image.paste(image5, (0, height))
merged_image.paste(image4, (width, height))
merged_image.paste(image6, (2*width, height))

# 显示合并后的图像
merged_image.show()

# 如果需要保存合并后的图像
# merged_image.save("merged_image.png")