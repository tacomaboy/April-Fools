@echo off
echo Starting Rivian April Fools local server...
echo.
echo Open your browser to: http://localhost:8080
echo Press Ctrl+C to stop the server.
echo.
cd /d "%~dp0"
python -m http.server 8080
pause
