#/bin/sh
pyuic5 -x ui/rocket_designer.ui -o src/ui.py
pyuic5 -x ui/about.ui -o src/about_ui.py
pyuic5 -x ui/cheatsheet.ui -o src/cs_ui.py
pyuic5 -x ui/example.ui -o src/example_ui.py
