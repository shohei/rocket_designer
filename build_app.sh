#/bin/sh

# 1) Use of pyinstaller: does not work
pyinstaller --windowed RocketDesigner.py --icon=image/logo_200px.png

# 2) Use of py2app: does not work
#py2applet --make-setup main.py
#python setup.py py2app
