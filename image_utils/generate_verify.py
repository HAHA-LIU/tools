# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2021/9/22 17:50
# describe: 生成验证码图片


import os
import random
import base64
from io import BytesIO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter


# def random_color():
#     c1 = random.randint(0, 255)
#     c2 = random.randint(0, 255)
#     c3 = random.randint(0, 255)
#     return c1, c2, c3
#
#
# def generate_picture(width=120, height=35):
#     image = Image.new('RGB', (width, height), random_color())
#     return image
#
#
# def random_str():
#     '''
#     获取一个随机字符, 数字或小写字母
#     :return:
#     '''
#     random_num = str(random.randint(0, 9))
#     random_low_alpha = chr(random.randint(97, 122))
#     random_char = random.choice([random_num, random_low_alpha])
#     return random_char
#
# def draw_str(count, image, font_size):
#     """
#     在图片上写随机字符
#     :param count: 字符数量
#     :param image: 图片对象
#     :param font_size: 字体大小
#     :return:
#     """
#     draw = ImageDraw.Draw(image)
#     # 获取一个font字体对象参数是ttf的字体文件的目录，以及字体的大小
#     font_file = os.path.join('ARIALN.TTF')
#     font = ImageFont.truetype(font=font_file, size=font_size)
#     temp = []
#     for i in range(count):
#         random_char = random_str()
#         draw.text((10+i*30, -2), random_char, random_color(), font=font)
#         temp.append(random_char)
#
#     valid_str = "".join(temp)    # 验证码
#     return valid_str, image
#
#
# def noise(image, width=120, height=35, line_count=3, point_count=20):
#     '''
#
#     :param image: 图片对象
#     :param width: 图片宽度
#     :param height: 图片高度
#     :param line_count: 线条数量
#     :param point_count: 点的数量
#     :return:
#     '''
#     draw = ImageDraw.Draw(image)
#     for i in range(line_count):
#         x1 = random.randint(0, width)
#         x2 = random.randint(0, width)
#         y1 = random.randint(0, height)
#         y2 = random.randint(0, height)
#         draw.line((x1, y1, x2, y2), fill=random_color())
#
#         # 画点
#         for i in range(point_count):
#             draw.point([random.randint(0, width), random.randint(0, height)], fill=random_color())
#             x = random.randint(0, width)
#             y = random.randint(0, height)
#             draw.arc((x, y, x + 4, y + 4), 0, 90, fill=random_color())
#
#     return image
#
#
# def valid_code():
#     """
#     生成图片验证码,并对图片进行base64编码
#     :return:
#     """
#     image = generate_picture()
#     valid_str, image = draw_str(4, image, 35)
#     image = noise(image)
#
#     f = BytesIO()
#     image.save(f, 'png')        # 保存到BytesIO对象中, 格式为png
#     data = f.getvalue()
#     f.close()
#
#     encode_data = base64.b64encode(data)
#     data = str(encode_data, encoding='utf-8')
#     img_data = "data:image/jpeg;base64,{data}".format(data=data)
#     return valid_str, img_data

# if __name__ == '__main__':
#     print(valid_code())

_letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母
_upper_cases = "ABCDEFGHJKLMNPQRSTUVWXY"  # 大写字母
_numbers = "1234567890"  # 数字
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))  # 生成允许的字符集合
# 验证码字体
default_font = os.path.join(os.path.split(
    os.path.realpath(__file__))[0], 'fonts', 'ARIALN.TTF')


# 生成图片验证码接口
def generate_verify_image(size=(120, 30),
                          chars=init_chars,
                          img_type="GIF",
                          mode="RGB",
                          bg_color=(255, 255, 255),
                          fg_color=(0, 0, 255),
                          font_size=18,
                          font_type=default_font,
                          length=4,
                          draw_lines=True,
                          n_line=(1, 2),
                          draw_points=True,
                          point_chance=2,
                          save_img=False):
    """
    生成验证码图片
    :param size: 图片的大小，格式（宽，高），默认为(120, 30)
    :param chars: 允许的字符集合，格式字符串
    :param img_type: 图片保存的格式，默认为GIF，可选的为GIF，JPEG，TIFF，PNG
    :param mode: 图片模式，默认为RGB
    :param bg_color: 背景颜色，默认为白色
    :param fg_color: 前景色，验证码字符颜色，默认为蓝色#0000FF
    :param font_size: 验证码字体大小
    :param font_type: 验证码字体，默认为 DejaVuSans.ttf
    :param length: 验证码字符个数
    :param draw_lines: 是否划干扰线
    :param n_line: 干扰线的条数范围，格式元组，默认为(1, 2)，只有draw_lines为True时有效
    :param draw_points: 是否画干扰点
    :param point_chance: 干扰点出现的概率，大小范围[0, 100]
    :param save_img: 是否保存为图片
    :return: [0]: 验证码字节流, [1]: 验证码图片中的字符串
    """

    width, height = size  # 宽， 高
    img = Image.new(mode, size, bg_color)  # 创建图形
    draw = ImageDraw.Draw(img)  # 创建画笔

    def get_chars():
        """生成给定长度的字符串，返回列表格式"""

        return random.sample(chars, length)

    def create_lines():
        """绘制干扰线"""

        line_num = random.randint(*n_line)  # 干扰线条数

        for i in range(line_num):
            # 起始点
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            # 结束点
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))

    def create_points():
        """绘制干扰点"""

        chance = min(100, max(0, int(point_chance)))  # 大小限制在[0, 100]

        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_strs():
        """绘制验证码字符"""

        c_chars = get_chars()
        strs = ' %s ' % ' '.join(c_chars)  # 每个字符前后以空格隔开

        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)

        draw.text(((width - font_width) / 3, (height - font_height) / 3),
                  strs, font=font, fill=fg_color)

        return ''.join(c_chars)

    if draw_lines:
        create_lines()
    if draw_points:
        create_points()
    strs = create_strs()

    # 图形扭曲参数
    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
    img = img.transform(size, Image.PERSPECTIVE, params)  # 创建扭曲

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强（阈值更大）

    mstream = BytesIO()   # 保存到BytesIO对象中
    img.save(mstream, img_type)
    data = mstream.getvalue()
    mstream.close()

    if save_img:
        img.save("validate.png", img_type)

    encode_data = base64.b64encode(data)
    data = str(encode_data, encoding='utf-8')
    img_data = "data:image/jpeg;base64,{data}".format(data=data)

    return strs, img_data

if __name__ == '__main__':

    print(generate_verify_image())
    print('000')