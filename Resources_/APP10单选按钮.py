# -*- coding: utf-8 -*-            
# @Author : XiangGuangyu
# @Time : 2023/6/17 20:49
import sys
from PyQt5.Qt import *
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("单选按钮")
        self.resize(500,500)
        self.DXAN()

    def DXAN(self):
        layout=QFormLayout()
        btn=QRadioButton("选项1")
        btn2=QRadioButton("选项2")
        btn.toggled.connect(self.btn_state)
        btn2.toggled.connect(self.btn_state)
        choose_btn = QHBoxLayout()
        choose_btn.addWidget(btn)
        choose_btn.addWidget(btn2)
        layout.addRow(QLabel("选择字体"),choose_btn)
        self.setLayout(layout)

    def btn_state(self):
        radiobtn= self.sender()
        if radiobtn.isChecked():
            print(f"{radiobtn.text()}被选中了")




if __name__ == '__main__':
    app =QApplication(sys.argv)
    app.setWindowIcon(QIcon("../Resources/dragon.ico"))
    main_ = MainWindow()
    # main.screensize()


    main_.show()
    sys.exit(app.exec_())
