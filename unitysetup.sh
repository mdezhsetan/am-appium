
echo "adb command ... "
adb forward tcp:13000 tcp:13000

echo "..........Starting Appium.........."
appium &

echo "..........Running tests.........."
python -m pytest Tests/ -s

echo "Tests done"
