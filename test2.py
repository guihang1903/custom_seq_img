import tkinter as tk
from tkinter import filedialog, ttk ,messagebox
from PIL import Image, ImageDraw, ImageFont

def generate_images():
    # 获取用户输入的参数
    background_image_path = background_path_entry.get()
    output_folder = output_path_entry.get()
    font_size = int(font_size_entry.get())
    extra_text = extra_text_entry.get()
    start_number = int(start_number_entry.get())
    end_number = int(end_number_entry.get())
    alignment = alignment_combobox.get()

    # 加载背景图片
    background_image = Image.open(background_image_path)

    # 自定义字体和颜色
    font = ImageFont.truetype("arial.ttf", font_size)
    text_color = (0, 0, 0)  # 黑色

    for i in range(start_number, end_number + 1):
        # 创建一个新的背景图像对象，以确保每次循环都是新的
        current_image = background_image.copy()

        # 创建一个可绘制的图像对象
        draw = ImageDraw.Draw(current_image)

        # 格式化序列号
        serial_number = f"{extra_text}{i:02d}"

        # 获取文本边界框，以便根据对齐方式调整位置
        text_bbox = draw.textbbox((0, 0), serial_number, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # 根据对齐方式调整位置
        if alignment == "居中":
            x = (current_image.width - text_width) // 2
            y = (current_image.height - text_height) // 2
        elif alignment == "上":
            x = (current_image.width - text_width) // 2
            y = 0
        elif alignment == "下":
            x = (current_image.width - text_width) // 2
            y = current_image.height - text_height
        elif alignment == "左":
            x = 0
            y = (current_image.height - text_height) // 2
        elif alignment == "右":
            x = current_image.width - text_width
            y = (current_image.height - text_height) // 2
        else:
            # 默认为居中
            x = (current_image.width - text_width) // 2
            y = (current_image.height - text_height) // 2

        # 在图像上添加序列号
        draw.text((x, y), serial_number, font=font, fill=text_color)

        # 关闭绘制对象，以便下一次迭代
        del draw

        # 将图像转换为RGB模式并保存为JPEG
        rgb_image = current_image.convert("RGB")
        output_path = f"{output_folder}image_{extra_text}{i:02d}.jpg"
        rgb_image.save(output_path)
    
    # 生成完成后弹窗提醒
    messagebox.showinfo("完成", "图片生成完成！")

# 用户输入参数的界面
root = tk.Tk()
root.title("图片批量增加文字和序列的工具 By：YuanPeng")

# 添加控件
background_label = tk.Label(root, text="背景图片路径:")
background_label.grid(row=0, column=0, padx=10, pady=5)

background_path_entry = tk.Entry(root, width=50)
background_path_entry.grid(row=0, column=1, padx=10, pady=5)

browse_background_button = tk.Button(root, text="浏览", command=lambda: browse_background_image(background_path_entry))
browse_background_button.grid(row=0, column=2, padx=10, pady=5)

output_label = tk.Label(root, text="输出文件夹路径:")
output_label.grid(row=1, column=0, padx=10, pady=5)

output_path_entry = tk.Entry(root, width=50)
output_path_entry.grid(row=1, column=1, padx=10, pady=5)

browse_output_button = tk.Button(root, text="浏览", command=lambda: browse_output_folder(output_path_entry))
browse_output_button.grid(row=1, column=2, padx=10, pady=5)

font_size_label = tk.Label(root, text="文字大小:")
font_size_label.grid(row=2, column=0, padx=10, pady=5)

font_size_entry = tk.Entry(root, width=10)
font_size_entry.grid(row=2, column=1, padx=10, pady=5)

extra_text_label = tk.Label(root, text="额外文字:")
extra_text_label.grid(row=3, column=0, padx=10, pady=5)

extra_text_entry = tk.Entry(root, width=50)
extra_text_entry.grid(row=3, column=1, padx=10, pady=5)

start_number_label = tk.Label(root, text="序列号开始数字:")
start_number_label.grid(row=4, column=0, padx=10, pady=5)

start_number_entry = tk.Entry(root, width=10)
start_number_entry.grid(row=4, column=1, padx=10, pady=5)

end_number_label = tk.Label(root, text="序列号结束数字:")
end_number_label.grid(row=5, column=0, padx=10, pady=5)

end_number_entry = tk.Entry(root, width=10)
end_number_entry.grid(row=5, column=1, padx=10, pady=5)

alignment_label = tk.Label(root, text="文字对齐方式:")
alignment_label.grid(row=6, column=0, padx=10, pady=5)

alignment_combobox = ttk.Combobox(root, values=["居中", "上", "下", "左", "右"])
alignment_combobox.grid(row=6, column=1, padx=10, pady=5)
alignment_combobox.set("居中")  # 默认为居中

generate_button = tk.Button(root, text="生成图片", command=generate_images)
generate_button.grid(row=7, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=8, column=0, columnspan=2)

# 辅助函数，用于浏览背景图片
def browse_background_image(entry):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

# 辅助函数，用于浏览输出文件夹路径
def browse_output_folder(entry):
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_path+"/")

# 运行主循环
root.mainloop()
