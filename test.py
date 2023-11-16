from PIL import Image, ImageDraw, ImageFont

# 背景图片路径
background_image_path = "img1.jpg"

# 输出文件夹路径
output_folder = "custom_images/"

# 序列号起始和结束数字
start_number = 1
end_number = 36

# 加载背景图片
background_image = Image.open(background_image_path)

# 自定义字体、大小和颜色
font_size = 30
font = ImageFont.truetype("arial.ttf", font_size)
text_color = (0, 0, 0)  # 黑色
# 额外的文字
extra_text = "1-2-XD-"

# 加载背景图片
background_image = Image.open(background_image_path)

for i in range(start_number, end_number + 1):
    # 创建一个新的背景图像对象，以确保每次循环都是新的
    current_image = background_image.copy()
    
    # 创建一个可绘制的图像对象
    draw = ImageDraw.Draw(current_image)
    
    # 格式化序列号
    serial_number = f"{extra_text}{i:02d}"
    
    # 获取文本边界框，以便居中显示
    text_bbox = draw.textbbox((0, 0), serial_number, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # 计算位置以居中显示文本
    x = (current_image.width - text_width) // 2
    y = (current_image.height - text_height) // 2
    
    # 在图像上添加序列号
    draw.text((x, y), serial_number, font=font, fill=text_color)
    
    # 关闭绘制对象，以便下一次迭代
    del draw

    # 将图像转换为RGB模式并保存为JPEG
    rgb_image = current_image.convert("RGB")
    output_path = f"{output_folder}image_with_serial_{i:02d}.jpg"
    rgb_image.save(output_path)

print("批量处理完成！")