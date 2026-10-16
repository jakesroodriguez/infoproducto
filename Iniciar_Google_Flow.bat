@echo off
chcp 65001 >nul
title Iniciar Google Flow Conectado con Antigravity
color 0A

echo ========================================================
echo     INICIAR GOOGLE FLOW CONECTADO A ANTIGRAVITY
echo ========================================================
echo.
echo Selecciona con qué navegador sueles usar Google Flow:
echo.
echo [1] Google Chrome
echo [2] Brave Browser (Recomendado para ti)
echo.
set /p nav="Elige opción (1 o 2, pulsa 2 para Brave): "

if "%nav%"=="1" (
    set BROWSER_EXE="C:\Program Files\Google\Chrome\Application\chrome.exe"
    set BROWSER_NAME=chrome.exe
) else (
    set BROWSER_EXE="C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    set BROWSER_NAME=brave.exe
)

echo.
echo Verificando si %BROWSER_NAME% está en ejecución...
tasklist /fi "imagename eq %BROWSER_NAME%" 2>nul | find /i "%BROWSER_NAME%" >nul
if %ERRORLEVEL% equ 0 (
    echo.
    echo [AVISO] %BROWSER_NAME% ya está abierto.
    echo Para que la conexión de depuración funcione, el navegador
    echo debe cerrarse y reabrirse con el puerto 9222.
    echo.
    echo ¿Quieres cerrar %BROWSER_NAME% y reabrirlo ahora? (S/N)
    set /p rein="> "
    if /i "%rein%"=="S" (
        echo Cerrando %BROWSER_NAME%...
        taskkill /f /im %BROWSER_NAME% >nul 2>&1
        timeout /t 2 >nul
    )
)

echo.
echo Abriendo Google Flow con puerto de conexión 9222...
start "" %BROWSER_EXE% --remote-debugging-port=9222 --remote-allow-origins=* "https://flow.google.com/"

echo.
echo ========================================================
echo  [LISTO] Navegador abierto con el puerto 9222 activo.
echo  Ya puedes pedirle a Antigravity que controle Google Flow.
echo ========================================================
timeout /t 5 >nul
