@echo off
title Trabajo_Automatico - Launcher
cd /d "%~dp0"

echo =========================================
echo      INICIANDO PROYECTO AUTOMATICO
echo =========================================
echo.

python main.py
if errorlevel 9009 (
  echo "python" no se reconoce. Probando con "py" del launcher de Python...
  py main.py
)

echo.
echo =========================================
echo   ✅ PROCESO FINALIZADO - REVISA ARRIBA
echo =========================================
pause
