# -*- coding: utf-8 -*-            
# @Author : XiangGuangyu
# @Time : 2023/6/18 20:59
# -*- coding: utf-8 -*-
# @Author : XiangGuangyu
# @Time : 2023/6/15 22:12
import sys,os
from PyQt5.Qt import *
from modules_for_app import get_current_path

class Multi_window(QTabWidget):
    def __init__(self,parent=None):
        super(Multi_window,self).__init__(parent)
        self.setWindowTitle("MyToolkit")
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.addTab(self.tab1,"图片时间水印")
        self.addTab(self.tab2,"选择")
        self.addTab(self.tab3,"PDF_To_Phtoto")
        self.addTab(self.tab4,"Draw")
        self.addTab(self.tab5,"蓝奏分卷压缩")
        self.addTab(self.tab6,"获取图片的时间和位置信息")
        self.tab1UI()
        self.font_style = "font1.ttf"#默认
        self.save_mode="原位置新建"#默认
        self.save_position=""
        self.Font_Size=100#默认
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.tab6UI()

    def tab1UI(self):
        #可以修改标签名称
        # self.setTabText(0,"图片时间水印")

        #参数选择控件
        self.cb = QComboBox()
        self.cb.setStyleSheet("background-color:pink;color:yellow;font-size:30px;font:bold;")
        self.cb.addItem("font1")
        self.cb.addItem("font2")
        #可以直接加多个，用列表
        # self.cb.addItems(["font_3", "font_4", "font_5"])
        self.cb.currentIndexChanged.connect(self.cb_value_input)

        #保存模式选择
        #selection为一个水平容器
        selection_ = QHBoxLayout()
        btn1 = QRadioButton("新位置另存")
        btn1.setStyleSheet("font-size:30px;font:bold;")
        btn2 = QRadioButton("覆盖原图")
        btn2.setStyleSheet("font-size:30px;font:bold;")
        btn3 = QRadioButton("原位置新建")
        btn3.setChecked(True)#默认选这个
        btn3.setStyleSheet("font-size:30px;font:bold;")
        btn1.toggled.connect(self.btn_state)
        btn2.toggled.connect(self.btn_state)
        btn3.toggled.connect(self.btn_state)
        selection_.addWidget(btn1)
        selection_.addWidget(btn2)
        selection_.addWidget(btn3)

        #字体大小选择
        self.font_size = QLineEdit()
        self.font_size.setPlaceholderText("大致范围100~200,默认100")
        self.font_size.textChanged.connect(self.font_size_input)

        #tab1整体的背景修改
        self.tab1.setStyleSheet("background-color:violet;")
        # self.tab1.setWindowIcon(QIcon(os.path.join(get_current_path(),"Resources_", "dragon.ico")))

        #修改光标
        # pixmap = QPixmap(pathfind_.find_path(os.path.join("Resources_", "bxch.ico")))
        # cursor = QCursor(pixmap)
        # self.tab1.setCursor(cursor)

        # JDT = QProgressBar(window)
        # JDT.setWindowTitle("图片处理中")
        # JDT.setRange(0,0)

        #Tab1的控件

        btn_run = QPushButton(self.tab1)
        btn_run.setIcon(QIcon(os.path.join(get_current_path(),"Resources_", "Tools.ico")))
        btn_run.setIconSize(QSize(150,150))
        # xxoffset = (self.tab1.width() - 300) / 2
        # btn_run.move(xxoffset, (self.tab1.height() - 300) / 2)
        btn_run.clicked.connect(self.SelectFolder)

        self.label_path_show = QTextEdit(self.tab1)
        # label.setText("Add time information to the images")
        self.label_path_show.setStyleSheet("background-color:cyan;color:blue;font-size:30px;font:bold;")
        # label.adjustSize()
        # xoffset = (self.tab1.width() - label.width()) / 2
        # label.move(xoffset, 50)

        #加入布局
        layout_tab1 = QFormLayout()
        layout_tab1.addRow(QLabel("选择图片文件保存方式"))
        layout_tab1.addRow(selection_)
        layout_tab1.addRow(self.label_path_show)
        layout_tab1.addRow(QLabel("选择水印字体"))
        layout_tab1.addRow(self.cb)
        layout_tab1.addRow(QLabel("输入字体大小"))
        layout_tab1.addRow(self.font_size)
        layout_tab1.addRow(QLabel("点击开始处理图片"))
        layout_tab1.addRow(btn_run)
        self.tab1.setLayout(layout_tab1)
    #选择字体的槽函数
    def cb_value_input(self):
        self.font_style = self.cb.currentText() + ".ttf"
        # print(f"选中的字体为{self.cb.currentText()},i={i}")
    #选择保存方式的槽函数
    def btn_state(self):
        radiobtn= self.sender()
        if radiobtn.isChecked():
            self.save_mode = radiobtn.text()
            if  self.save_mode == "新位置另存":
                self.save_position=QFileDialog.getExistingDirectory(self.tab1, "选择图片保存的新位置")
            else:self.save_position=""
        self.label_path_show.setText(self.save_mode+"\n" + self.save_position)
    #输入字体的槽函数
    def font_size_input(self):
        if self.font_size.text():#缺省
            self.Font_Size=int(self.font_size.text())
    #加水印，并且调用多个脚本的主程序槽函数
    def SelectFolder(self):
        from modules_for_app import add_ShuiYin
        filepath = QFileDialog.getExistingDirectory(self.tab1, "选择图片路径")
        select = QMessageBox.question(self.tab1, "再次确认", "确定选好目录？")
        if filepath:
            if select == QMessageBox.Yes:
                # self.status = self.statusBar()
                # self.status.showMessage("正在处理图片......")
                QMessageBox.about(self.tab1, " ", "开始处理图片")
                print(filepath, self.font_style, self.save_mode, self.Font_Size, self.save_position)
                num=add_ShuiYin(filepath, font_style=self.font_style, save_mode=self.save_mode, font_size=self.Font_Size, save_position=self.save_position)#
                if str(num):
                    QMessageBox.about(self.tab1, " ", f"共处理完{num}张图片")

    def tab2UI(self):
        self.tab2.setStyleSheet("background-color:springgreen;")
        layout01 = QFormLayout()
        selection = QHBoxLayout()
        selection.addWidget(QRadioButton("双一流"))
        selection.addWidget(QRadioButton("土木强校"))
        layout01.addRow(QLabel("你的选择"),selection)
        layout01.addRow(QPushButton())
        self.tab2.setLayout(layout01)
        #设置光标
        pixmap = QPixmap(os.path.join(get_current_path(),"Resources_", "bxch.ico"))
        cursor = QCursor(pixmap)
        self.tab2.setCursor(cursor)

    def tab3UI(self):
        self.tab3.setStyleSheet("background-color:cyan;")
        self.btn_pdf_01=QPushButton("点击选择PDF文件")
        self.btn_pdf_02=QPushButton("点击选择提取图片保存位置")
        self.btn_pdf_03=QPushButton("点击获取图片")
        self.btn_pdf_01.setStyleSheet("background-color:gold;color:green;font-size:30px;font:bold;")
        self.btn_pdf_02.setStyleSheet("background-color:gold;color:green;font-size:30px;font:bold;")
        self.btn_pdf_03.setStyleSheet("background-color:gold;color:green;font-size:30px;font:bold;")
        self.btn_pdf_01.clicked.connect(self.get_pdf_path)
        self.btn_pdf_02.clicked.connect(self.choose_pdf_img_save_path)
        self.btn_pdf_03.clicked.connect(self.extract_img_from_pdf)
        layout_for_pdf=QFormLayout()
        layout_for_pdf.addRow(self.btn_pdf_01)
        layout_for_pdf.addRow(self.btn_pdf_02)
        layout_for_pdf.addRow(self.btn_pdf_03)
        self.tab3.setLayout(layout_for_pdf)

    #tabUI的相关槽函数
    def get_pdf_path(self):
        self.pdf_path,_ = QFileDialog.getOpenFileName(self,"选择PDF",".","PDF文档(*.pdf)")
    def choose_pdf_img_save_path(self):
        self.pdf_img_save_path = QFileDialog.getExistingDirectory(self.tab3,"请选择PDF提取图片保存路径")
    def extract_img_from_pdf(self):
        import fitz
        import re
        import os
        def pdf2image1(path, pic_path):
            checkIM = r"/Subtype(?= */Image)"
            pdf = fitz.open(path)
            lenXREF = pdf.xref_length()
            count = 1
            for i in range(1, lenXREF):
                text = pdf.xref_object(i)
                isImage = re.search(checkIM, text)
                if not isImage:
                    continue
                pix = fitz.Pixmap(pdf, i)
                if pix.size < 10000:  # 在这里添加一处判断一个循环
                    continue  # 不符合阈值则跳过至下
                new_name = f"img_{count}.png"
                pix.save(os.path.join(pic_path, new_name))
                count += 1
                pix = None
            return count
        amount=pdf2image1(self.pdf_path,self.pdf_img_save_path)
        QMessageBox.about(self.tab3, " ", f"共获取到{amount}张图片")
        os.startfile(self.pdf_img_save_path)

    def tab4UI(self):
        btn_to_draw = QPushButton()
        btn_to_draw.clicked.connect(self.click_to_draw)
        btn_to_draw.setStyleSheet("background-color:hotpink;color:cornsilk;font-size:30px;font:bold;")
        btn_to_draw.setText("点击绘制")
        layout_tab4ui = QFormLayout()
        layout_tab4ui.addRow(btn_to_draw)
        self.tab4.setLayout(layout_tab4ui)
    def click_to_draw(self):
        desktop_size = QApplication.desktop()
        self.window = QWidget()
        self.window.setWindowTitle("DrawFullscreen")
        self.window.resize(desktop_size.width(),desktop_size.height())
        w_total = 100  # 给定
        w_colum_num = 10  # 给定
        w_sequence = w_total - 1
        row_num_total = w_sequence // w_colum_num + 1  # 总行数：编号 整除 列数 +1
        # colum_count = w_sequence % w_colum_num +1#列号

        # 位置
        per_width = self.window.width() / w_colum_num
        per_height = self.window.height() / row_num_total
        for i in range(w_total):
            w = QWidget(self.window)
            w.resize(per_width, per_height)
            # 位置，第几行，第几列
            x = i % w_colum_num
            y = i // w_colum_num
            w.move(x * per_width, y * per_height)
            if i % 3 == 0:
                w.setStyleSheet("background-color:green;")
            elif i % 3 == 1:
                w.setStyleSheet("background-color:red;")
            else:
                w.setStyleSheet("background-color:violet;")

        # self.window.showMaximized()
        self.window.showFullScreen()
    def tab5UI(self):
        layout = QFormLayout()
        btn_1 = QPushButton("选择主压缩文件")
        btn_2 = QPushButton("to上传")
        btn_3 = QPushButton("to解压缩")
        btn_1.setStyleSheet("background-color:lawngreen;color:deepskyblue;font-size:30px;font:bold;")
        btn_2.setStyleSheet("background-color:lawngreen;color:deepskyblue;font-size:30px;font:bold;")
        btn_3.setStyleSheet("background-color:lawngreen;color:deepskyblue;font-size:30px;font:bold;")
        btn_1.clicked.connect(self.btn1_get_mainzip)
        btn_2.clicked.connect(self.bt2_choose_mode)
        btn_3.clicked.connect(self.bt3_choose_mode)
        layout.addRow(btn_1)
        layout.addRow(btn_2)
        layout.addRow(btn_3)
        self.tab5.setLayout(layout)
    def btn1_get_mainzip(self):
        self.main_zip,_=QFileDialog.getOpenFileName(self, "选择分卷压缩主zip", ".", "分卷压缩文件(*.zip)")
    def bt2_choose_mode(self):
        self.LanZou_mode = "update"
        self.rename_for_LanZou(self.main_zip,self.LanZou_mode)
    def bt3_choose_mode(self):
        self.LanZou_mode = "compress"
        self.rename_for_LanZou(self.main_zip,self.LanZou_mode)

    def rename_for_LanZou(self,main_zip,mode):
        print(main_zip,mode)
        zip_name = os.path.splitext(os.path.basename(main_zip))[0]
        directory = os.path.dirname(main_zip)
        file_list = os.listdir(directory)
        print(zip_name, "\n", directory, "\n", file_list)
        for file in file_list:
            old_full_path = os.path.join(directory, file)
            if mode == "compress" and zip_name in file and file.endswith(".iso"):
                new_full_path = os.path.join(directory, file.replace(".iso", ""))
                os.rename(old_full_path, new_full_path)
            if mode == "update" and zip_name in file and not (file.endswith(".zip")):
                new_full_path01 = os.path.join(directory, file + ".iso")
                os.rename(old_full_path, new_full_path01)

    def tab6UI(self):
        layout=QFormLayout()
        btn_choose_img=QPushButton()
        btn_choose_img.setText("点击选择照片")
        btn_choose_img.clicked.connect(self.btn_get_img_tab6)
        btn_choose_img.setStyleSheet("background-color:greenyellow;color:darkturquoise;font-size:30px;font:bold;")
        self.show_window_tab6=QTextEdit()
        self.show_window_tab6.setStyleSheet("background-color:moccasin;color:tomato;font-size:30px;font:bold;")

        layout.addRow(btn_choose_img)
        layout.addRow(self.show_window_tab6)
        self.tab6.setLayout(layout)
    #tab6按钮槽函数获取图片路径
    def btn_get_img_tab6(self):
        self.img_path_tab6, _ = QFileDialog.getOpenFileName(self, "选择拍摄的照片", ".", "照片(*.jpg)")
        def get_img_info(img_path):
            import re
            import json
            import requests
            import exifread
            # 转换经纬度格式
            def latitude_and_longitude_convert_to_decimal_system(*arg):
                """
                经纬度转为小数, param arg:
                :return: 十进制小数
                """
                return float(arg[0]) + (
                            (float(arg[1]) + (float(arg[2].split('/')[0]) / float(arg[2].split('/')[-1]) / 60)) / 60)

            # 读取照片的GPS经纬度信息
            def find_GPS_image(pic_path):
                GPS = {}
                date = ''
                with open(pic_path, 'rb') as f:
                    tags = exifread.process_file(f)
                    for tag, value in tags.items():
                        # 纬度
                        if re.match('GPS GPSLatitudeRef', tag):
                            GPS['GPSLatitudeRef'] = str(value)
                        # 经度
                        elif re.match('GPS GPSLongitudeRef', tag):
                            GPS['GPSLongitudeRef'] = str(value)
                        # 海拔
                        elif re.match('GPS GPSAltitudeRef', tag):
                            GPS['GPSAltitudeRef'] = str(value)
                        elif re.match('GPS GPSLatitude', tag):
                            try:
                                match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                                GPS['GPSLatitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                            except:
                                deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                                GPS['GPSLatitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
                        elif re.match('GPS GPSLongitude', tag):
                            try:
                                match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                                GPS['GPSLongitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                            except:
                                deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                                GPS['GPSLongitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
                        elif re.match('GPS GPSAltitude', tag):
                            GPS['GPSAltitude'] = str(value)
                        elif re.match('.*Date.*', tag):
                            date = str(value)
                return {'GPS_information': GPS, 'date_information': date}
            # 通过baidu Map的API将GPS信息转换成地址
            def find_address_from_GPS(GPS):
                """
                使用Geocoding API把经纬度坐标转换为结构化地址。
                :param GPS:
                :return:
                """
                # 调用百度API的ak值，这个可以注册一个百度开发者获得
                secret_key = 'zbLsuDDL4CS2U0M4KezOZZbGUY9iWtVf'
                if not GPS['GPS_information']:
                    return "无"
                lat, lng = GPS['GPS_information']['GPSLatitude'], GPS['GPS_information']['GPSLongitude']
                baidu_map_api = "http://api.map.baidu.com/geocoder/v2/?ak={0}&callback=renderReverse&location={1},{2}s&output=json&pois=0".format(
                    secret_key, lat, lng)
                response = requests.get(baidu_map_api)
                content = response.text.replace("renderReverse&&renderReverse(", "")[:-1]
                # print(content)
                baidu_map_address = json.loads(content)
                formatted_address = baidu_map_address["result"]["formatted_address"]
                province = baidu_map_address["result"]["addressComponent"]["province"]
                city = baidu_map_address["result"]["addressComponent"]["city"]
                district = baidu_map_address["result"]["addressComponent"]["district"]
                location = baidu_map_address["result"]["sematic_description"]
                return formatted_address, province, city, district, location
            GPS_info = find_GPS_image(pic_path=img_path)
            address = find_address_from_GPS(GPS=GPS_info)
            a = GPS_info.get("date_information")
            date_info = a.replace(":", "年", 1).replace(":", "月", 1).replace(" ", "日", 1)
            return {"time_info":date_info,"location_info":address[0]}
        if self.img_path_tab6:
            info_dict=get_img_info(self.img_path_tab6)
            time_info=info_dict.get('time_info')
            location_info=info_dict.get('location_info')
            if not time_info:
                time_info="!!所选图片不含时间信息!!"
            if not location_info:
                time_info = "!!所选图片不含位置信息!!"
            self.show_window_tab6.setText(
                f"拍摄时间：\n{time_info}\n\n拍摄地点：\n{location_info}")
            # self.show_window_tab6.adjustSize()
        else:
            QMessageBox.about(self.tab1, " ", "还没有选择照片")
            self.show_window_tab6.setText("!!请选择照片!!")

if __name__ == '__main__':
    app =QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(get_current_path(),"Resources_", "dragon.ico")))
    main_ = Multi_window()
    # main.screensize()


    main_.show()
    sys.exit(app.exec_())
