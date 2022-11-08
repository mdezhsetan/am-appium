

echo "..........ADB Command.........."
adb forward tcp:13000 tcp:13000

echo "..........Starting Appium.........."
appium --log-no-colors --log-timestamp  --command-timeout 60  > appium.log 2>&1 &
PID=$!
sleep 5

echo "..........Running tests.........."
python -m pytest Tests/*create* -s -v --junitxml=Output/junitxml_report.xml

echo "..........Tests Done.........."


adb kill-server
kill $PID