from PIL import Image

# 打开PNG
img = Image.open(r"")

# 转换并保存为ICO（建议多尺寸）
img.save("icon.ico", format="ICO", sizes=[(256,256), (128,128), (64,64), (32,32), (16,16)])

print("转换完成！")