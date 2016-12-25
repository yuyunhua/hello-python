# 使用说明
* 安装python
* 安装pillow库，pip install Pillow
* 打开AR红包后，对线索图截图（目前只支持1080*1920，1242*2208手机分辨率的图片）
* 存放到电脑指定目录下
* 运行一下命令，会在当前目录下得到target/target.png图片
* 手机对着图片扫描即可

命令：
python get_scannable_image.py . 4 2

* para #1. 存放截图AR红包截图的目录，默认当前目录
* para #2. N 用黑色条纹前第N行替换黑色条纹，默认4
* para #2. M 替换黑色条纹前后M行，默认2

成功率 1/4 ~ 1/3