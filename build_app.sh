#/bin/sh
pyinstaller -y --windowed src/RocketDesigner.py --icon=src/image/logo_200px.png \
  --add-data="src/image/logo_100px.png:image" --add-data="src/image/Lstar.png:image" \
  --add-data="src/image/pid_ox.png:image" --add-data="src/image/pid_fuel.png:image"

cp /opt/homebrew/lib/python3.9/site-packages/rocketcea/_version.py dist/RocketDesigner.app/Contents/Resources/rocketcea/
