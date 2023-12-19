#/bin/sh

# 1) Use of pyinstaller: does not work
#pyinstaller --windowed main.py

# 2) Use of py2app
py2applet --make-setup main.py
python setup.py py2app
