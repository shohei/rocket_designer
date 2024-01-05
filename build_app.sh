#/bin/sh
pyinstaller -y --windowed src/RocketDesigner.py --icon=src/image/logo_200px.png \
  --add-data="src/image/logo_100px.png:image" --add-data="src/image/Lstar.png:image" \
  --add-data="src/image/pid_ox.png:image" --add-data="src/image/pid_fuel.png:image" \
  --add-data="src/doc/mission.html:doc" --add-data="src/doc/thermochemical.html:doc" \
  --add-data="src/doc/nozzle.html:doc" --add-data="src/doc/chamber.html:doc" \
  --add-data="src/doc/feed.html:doc" --add-data="src/doc/ignitor.html:doc" \
  --add-data="src/doc/injector.html:doc" --add-data="src/doc/grain.html:doc" 

function get_site_package_path(){
  python -c 'import site; print(site.getsitepackages()[0])'
}
SITE_PACKAGE_PATH=$(get_site_package_path)
echo cp "${SITE_PACKAGE_PATH}/rocketcea/_version.py" dist/RocketDesigner.app/Contents/Resources/rocketcea/
cp "${SITE_PACKAGE_PATH}/rocketcea/_version.py" dist/RocketDesigner.app/Contents/Resources/rocketcea/

open dist/RocketDesigner.app
