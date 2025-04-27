# -*- coding: utf-8 -*-            
# @Author : XiangGuangyu
# @Time : 2023/6/18 19:37
from multiprocessing import Pool, cpu_count
def get_current_path():
    import sys,os
    """获取当前环境下的主路径"""
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return base_path

#水印程序
def add_ShuiYin(original_image_folder, font_style="font1.ttf", save_mode="原位置新建", font_size=100, save_position=""):
    import os, sys
    from PIL import Image, ImageDraw, ImageFont
    import random

    count_num=0
    #内部用到的步骤函数
    def screenshot_to_img(path):
        """输入图片路径，对图片文件改名，Screenshot改为IMG"""
        old_names = os.listdir(path)  # 取路径下的文件名，生成列表
        for old_name in old_names:  # 遍历列表下的文件名
            if "Screenshot" in old_name:
                new_name = old_name.replace("Screenshot", "IMG")
                os.rename(os.path.join(path, old_name), os.path.join(path, new_name))

    def get_current_path():
        """获取当前环境下的主路径"""
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath('.')
        return base_path

    def rename_as_time_by_exif(path):
        """输入图片路径，对路径中的图片通过exif信息，按照IMG时间命名（如果有的话）"""
        import re
        import os
        import exifread
        def exif_posess_each(pic_path):
            date = ''
            with open(pic_path, 'rb') as f:
                tags = exifread.process_file(f)
                # 键值对
                for tag, value in tags.items():
                    if re.match('.*Date.*', tag):
                        date = str(value)
            rename_time = date.replace(":", "", 4).replace(" ", "_")
            return {'date': date, "rename_date": rename_time}

        for file in os.listdir(path):
            if (not (file.startswith("IMG"))) and file.endswith(".jpg"):
                full_path = os.path.join(path, file)
                time_name = exif_posess_each(full_path).get("rename_date")
                # 如果不为空
                if time_name:
                    new_filename = "IMG_" + time_name + ".jpg"
                    full_newfilename = os.path.join(path, new_filename)
                    if not os.path.exists(full_newfilename):
                        os.rename(full_path, full_newfilename)

    def get_time_str_from_filename(filename):
        """根据文件名（含时间信息）提取时间字符串，年月日时分 共12个数字"""
        time_list = ""
        for i in filename:
            if i.isdigit():
                time_list += i
                if len(time_list) == 12: break
        return time_list

    def add_text(original_image_folder, font_style="font1.ttf", save_mode="原位置新建", font_size=100, save_position=""):
        #rename
        screenshot_to_img(original_image_folder)
        rename_as_time_by_exif(original_image_folder)
        # 保存位置
        output_path = original_image_folder #初试设置
        if save_mode == "新位置另存":
            output_path = save_position
        elif save_mode == "原位置新建":
            if not os.path.exists(original_image_folder + r"\输出"):
                output_path = os.path.join(original_image_folder, "输出")
                os.mkdir(output_path)
        else:pass
        #遍历图片文件逐个进行操作
        image_file_list = os.listdir(original_image_folder)  # 目录下的文件名列表
        for i in range(len(image_file_list)):
            filename = image_file_list[i]  # 文件名
            file_full_path = os.path.join(original_image_folder, image_file_list[i])  # 完整文件路径
            nonlocal count_num #修改定义函数外部的局部变量
            if (os.path.splitext(filename)[1] == ".jpg" or os.path.splitext(filename)[1] == ".png") and \
                    (filename.startswith("IMG") or \
                     filename.startswith("Screenshot")):
                count_num += 1
                # 获取时间字符串,根据文件名
                time_str = get_time_str_from_filename(filename)
                t_year = time_str[:4]
                t_month = time_str[4:6]
                t_day = time_str[6:8]
                t_hours = time_str[8:10]
                t_minutes = time_str[10:12]
                time_str_to_add_in_image = "%s/%s/%s %s:%s" % (t_year, t_month, t_day, t_hours, t_minutes)

                origin_photo = Image.open(file_full_path)  # 打开原图
                origin_layer = origin_photo.convert("RGBA")  # 原图图层
                text_layer = Image.new('RGBA', origin_layer.size, (255, 255, 255, 0))  # 新文字图层
                text_canvas = ImageDraw.Draw(text_layer)
                font_path = os.path.join(get_current_path(),"Resources_", font_style)
                font_set = ImageFont.truetype(font_path,int(font_size))
                # text_w, text_h = text_canvas.textsize(time_str_to_add_in_image, font=font_set)
                border_box = text_canvas.textbbox((0, 0), time_str_to_add_in_image, font=font_set)# 获取文本的边界框
                text_w = border_box[2] - border_box[0]# 计算文本的宽度和高度
                text_h = border_box[3] - border_box[1]
                text_position = (origin_photo.size[0] - 1.25 * text_w, 0)
                text_canvas.text(text_position, time_str_to_add_in_image, font=font_set,fill=random.choice(["pink", "yellow", "green", "orange","violet"]))  # "pink","yellow","white","green","purple","orange","violet"
                new_image = Image.alpha_composite(origin_layer, text_layer)
                file_save_full_path = os.path.join(output_path, filename)
                new_image.convert("RGB").save(file_save_full_path)
                print(f"成功为第{count_num} 张图片添加水印!\n")
    # data_=[original_image_folder, font_style, save_mode, font_size, save_position]
    # with Pool(processes=cpu_count() // 2) as pool:  # 留一半CPU资源
    #     pool.map(add_text,data_)
    add_text(original_image_folder, font_style, save_mode, font_size, save_position)
    return count_num



if __name__ == '__main__':
    I = input("输入待加水印图片文件夹路径\n")
    # I=r"C:\Users\Elizabeth_X\Desktop\demo9"
    # O = input("输入输出路径")
    # rename_by_time(I)

    # with Pool(processes=cpu_count() // 2) as pool:  # 留一半CPU资源
    #     pool.map(add_ShuiYin,I)
    ccc=add_ShuiYin(I)
    # print(ccc)
    # # print(f"共为 {count} 张图片添加水印!\n")
    # # print(pathfind.find_path(os.path.join("Resources_", "font2")))
    # # print(pathfind.find_path("fjfjfj.jdjjd"))

