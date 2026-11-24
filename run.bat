@echo off
chcp 65001 > nul
python src/main.py tests/script1.txt result.bin --test
pause