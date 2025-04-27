# 照片添加时间信息水印&对应的图形界面程序
## 功能介绍
1. 图片加时间水印
2. 选择，cursor更换图标
3. 提取pdf文件中的所有图片并且存放到指定文件夹
4. 全屏绘图
5. 蓝奏云网盘100m分卷压缩后批量重命名为.iso后方便上传，再次运行改回原来的文件名
6. 根据图片的exif信息获取大致地理位置
## 效果图
![image](https://github.com/user-attachments/assets/05fafb90-a91c-4c77-bb3f-c367b73263e6)
## 项目目录预览图
![image](https://github.com/user-attachments/assets/b4d3530b-b709-4be6-a76b-cb14071511e0)

## 安装运行：
### 通过conda配置虚拟环境:
```python
conda env create -f env_pyqt01.yml
# env_pyqt01.yml中包含本项目需要的各种库及其版本信息
```
### 运行MyToolkit.py即可显示图形界面
## 文件介绍
### 其中MyToolkit.py主要是pyqt5图形界面相关代码
### 而modules_for_app.py主要包含控件连接的槽函数
### Resources_文件夹中包含资源文件，如图标、字体等
## 打包相关
### 单文件
```python
pyinstaller -Fw -i  ./郁金香.ico ./MySoftware/MyToolKit.py --add-data="./MySoftware/Resources_;Resources_"
#分别对应图标、脚本文件、资源文件
```
# 于2023/6/18 20:59考研期间写完，2025年4月27日17:29:31整理后上传

# Photo Watermarking with Time Information & Corresponding GUI Program

## Function Introduction
1. Add time watermarks to pictures.
2. Provide selection options and change the cursor icon.
3. Extract all images from a PDF file and save them to a specified folder.
4. Enable full - screen drawing.
5. Compress files into 100MB volumes for upload to Lanzou Cloud, rename them to .iso for convenience, and revert to their original names when running the program again.
6. Obtain the approximate geographical location based on the EXIF information of pictures.

## Screenshot
![image](https://github.com/user-attachments/assets/05fafb90-a91c-4c77-bb3f-c367b73263e6)

## Project Directory Preview
![image](https://github.com/user-attachments/assets/b4d3530b-b709-4be6-a76b-cb14071511e0)

## Installation and Execution
### Configure a virtual environment via Conda:
```python
conda env create -f env_pyqt01.yml
# env_pyqt01.yml contains various libraries and their version information required for this project.
```
### Run MyToolkit.py to display the graphical user interface.

## File Introduction
### MyToolkit.py mainly contains the PyQt5 GUI - related code.
### modules_for_app.py mainly includes the slot functions connected to the controls.
### The Resources_ folder contains resource files such as icons and fonts.

## Packaging - related
### Single - file packaging
```python
pyinstaller -Fw -i  ./郁金香.ico ./MySoftware/MyToolKit.py --add-data="./MySoftware/Resources_;Resources_"
# Corresponding to the icon, script file, and resource file respectively.
```
# Completed during postgraduate entrance examination preparation on June 18, 2023, at 20:59. Organized and uploaded on April 27, 2025, at 17:29:31. 


