#/bin/sh
pyinstaller -y --windowed RocketDesigner.py --icon=image/logo_200px.png \
  --add-data="image/logo_100px.png:image" --add-data="image/Lstar.png:image" \
  --add-data="image/pid_ox.png:image" --add-data="image/pid_fuel.png:image"

cp /opt/homebrew/lib/python3.9/site-packages/rocketcea/_version.py dist/RocketDesigner.app/Contents/Resources/rocketcea/
