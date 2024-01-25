import os
from PIL import Image

def png_to_gif(png_path, gif_name):
    """png合成gif图像"""
    frames = []
    # 返回文件夹内的所有静态图的列表
    png_files = os.listdir(png_path)
    # 打印返回的列表
    print(png_files)
    # 读取文件内的静态图
    for frame_id in range(1, len(png_files) + 1):
        frame = Image.open(os.path.join(png_path, 'image%d.png' % frame_id))
        frames.append(frame)
    # 以第一张图片作为开始，将后续5张图片合并成 gif 动态图
    # 参数说明：
    # save_all 保存图像;transparency 设置透明背景色;duration 单位毫秒，动画持续时间，
    # loop=0 无限循环;disposal=2 恢复原背景颜色。参数详细说明，请参阅官方文档，网址见文章末尾处。
    frames[0].save(gif_name, save_all=True, append_images=frames[1:], transparency=0, duration=1000, loop=0, disposal=2)


# 调用函数，传入对应的参数
png_to_gif(r"D:\tools\image\14", r"D:\tools\image\14\g.gif")