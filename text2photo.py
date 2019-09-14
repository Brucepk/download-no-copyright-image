from PIL import Image, ImageDraw, ImageFont
import os


def text2pic(file_dir):
    for root, dirs, files in os.walk(file_dir):  # 列出目录下所有的文件
        for file in files:
            pic_dirs = file_dir + '/' + file
            image = Image.open(pic_dirs)

            # 设置需要显示的字体，# Mac os字体路径 /System/Library/Fonts/ windows系统字体路径一般为C:\Windows\Fonts
            fontpath = "/System/Library/Fonts/STHeiti Medium.ttc"
            font = ImageFont.truetype(fontpath, 14)       # 设置字体和字体大小
            draw = ImageDraw.Draw(image)

            # 获取图片尺寸
            width, height = image.size

            ## 添加水印
            draw.text((1/30*width, 9/10*height),  u'@Python知识圈', font=font, fill=(255, 255, 255))
            image.save(file_dir + '/' + "watermark{}".format(file), 'png')


if __name__ == '__main__':
    file_dir = r'/Users/brucepk/Pictures/beautiful girl'
    text2pic(file_dir)