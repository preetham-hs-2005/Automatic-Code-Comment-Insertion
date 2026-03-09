$ErrorActionPreference = "Stop"

Write-Host "Cleaning up old processes on port 8001..." -ForegroundColor Yellow
$processId = (Get-NetTCPConnection -LocalPort 8001 -ErrorAction SilentlyContinue).OwningProcess
if ($processId) {
    Stop-Process -Id $processId -Force -ErrorAction SilentlyContinue
    Write-Host "Killed process on port 8001." -ForegroundColor Green
}

Write-Host "Setting up backend..." -ForegroundColor Yellow
Set-Location "$PSScriptRoot\backend"
& "..\venv\Scripts\python.exe" -m pip install -r requirements.txt -q

Write-Host "Starting FastAPI Backend..." -ForegroundColor Green
Start-Process -NoNewWindow -FilePath "..\venv\Scripts\python.exe" -ArgumentList "-m", "uvicorn", "main:app", "--port", "8001"

Write-Host "Waiting for backend to initialize..." -ForegroundColor Yellow
Start-Sleep -Seconds 4

Write-Host "Opening Frontend in default browser..." -ForegroundColor Green
Set-Location "$PSScriptRoot\frontend"
Start-Process "index.html"

Write-Host "Project is running!" -ForegroundColor Cyan
