@echo off
cd /d "C:\Users\SWAPN\OneDrive\Desktop\DSA\DSA_striver"
git add .
set /p msg="Enter commit message: "
git commit -m "%msg%"
git push
pause
