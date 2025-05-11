@echo off
SET "gitPath=C:\Program Files\Git\cmd"
echo Adding Git path to system environment PATH...
setx /M PATH "%PATH%;%gitPath%"
echo Done! Please restart CMD.
pause
