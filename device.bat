@echo off
echo Disconnecting all devices...
adb disconnect

echo Killing and restarting ADB server...
adb kill-server
adb start-server

echo Setting device to TCP mode on port 5555...
adb tcpip 5555

echo Waiting for device to reconnect...
timeout /t 3 > nul

echo Connecting to device at 192.168.43.1:5555...
adb connect 192.168.43.1:5555

echo Connection attempt finished.
pause
