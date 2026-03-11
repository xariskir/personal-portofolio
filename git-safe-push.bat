@echo off
setlocal enabledelayedexpansion

echo ==========================================
echo        SAFE GIT PUSH SCRIPT (v1.0)
echo ==========================================
echo.

:: Ask for commit message
set /p msg=Enter commit message: 

echo.
echo 🔄 Pulling latest changes with rebase...
git pull --rebase origin main

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ ERROR: Pull failed. Resolve conflicts and try again.
    pause
    exit /b
)

echo.
echo ➕ Adding all changed files...
git add -A

echo.
echo 📝 Committing changes...
git commit -m "%msg%"

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo ⚠️  No changes to commit.
)

echo.
echo 🚀 Pushing to GitHub...
git push origin main

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Push failed!
    pause
    exit /b
)

echo.
echo ✅ SUCCESS! Everything is updated and deployed.
pause
