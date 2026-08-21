@echo off
title J.A.R.V.I.S - Sistemas Online
chcp 65001 >nul
color 0B
mode con: cols=115 lines=45
cd /d "%~dp0"
python main.py %*
pause