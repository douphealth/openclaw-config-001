param(
    [string]$Workspace = (Get-Location).Path,
    [string]$AsOf = (Get-Date -Format 'yyyy-MM-dd')
)

$memoryDir = Join-Path $Workspace 'memory'
$memoryFile = Join-Path $Workspace 'MEMORY.md'
$heartbeatFile = Join-Path $memoryDir 'heartbeat-state.json'
$entityDir = Join-Path $memoryDir 'entities'
$archiveDir = Join-Path $Workspace 'artifacts\memory\placeholder-daily-archive'

$dailyFiles = if (Test-Path $memoryDir) {
    Get-ChildItem $memoryDir -File -Filter '*.md' |
        Where-Object { $_.BaseName -match '^\d{4}-\d{2}-\d{2}$' } |
        Sort-Object Name
} else { @() }

$placeholderFiles = $dailyFiles | Where-Object { $_.Length -le 30 }
$realFiles = $dailyFiles | Where-Object { $_.Length -gt 30 }
$largestFiles = $realFiles | Sort-Object Length -Descending | Select-Object -First 10
$recentReal = $realFiles | Sort-Object LastWriteTime -Descending | Select-Object -First 10
$memoryLines = if (Test-Path $memoryFile) { (Get-Content $memoryFile).Count } else { 0 }
$entityFiles = if (Test-Path $entityDir) { Get-ChildItem $entityDir -File -Filter '*.md' | Sort-Object Name } else { @() }
$archivedPlaceholders = if (Test-Path $archiveDir) { @(Get-ChildItem $archiveDir -File -Filter '*.md').Count } else { 0 }
$heartbeat = if (Test-Path $heartbeatFile) { Get-Content $heartbeatFile -Raw | ConvertFrom-Json } else { $null }
$largestBytes = if ($largestFiles.Count -gt 0) { ($largestFiles | Select-Object -First 1).Length } else { 0 }

$issues = New-Object System.Collections.Generic.List[string]
$warnings = New-Object System.Collections.Generic.List[string]
$score = 100

if (-not (Test-Path $memoryFile)) {
    $issues.Add('MEMORY.md missing')
    $score -= 30
} elseif ($memoryLines -gt 220) {
    $issues.Add("MEMORY.md exceeds healthy size target ($memoryLines lines)")
    $score -= 15
} elseif ($memoryLines -gt 180) {
    $warnings.Add("MEMORY.md is approaching size ceiling ($memoryLines lines)")
    $score -= 5
}

if (-not $heartbeat) {
    $issues.Add('heartbeat-state.json missing')
    $score -= 20
}

if ($placeholderFiles.Count -gt 0) {
    $issues.Add("Active memory still contains placeholder daily stubs ($($placeholderFiles.Count))")
    $score -= 25
} elseif ($archivedPlaceholders -gt 0) {
    $score += 0
}

if ($entityFiles.Count -lt 3) {
    $issues.Add("Too few entity files for durable recall ($($entityFiles.Count))")
    $score -= 15
} elseif ($entityFiles.Count -lt 5) {
    $warnings.Add("Entity layer is present but can be expanded ($($entityFiles.Count) files)")
    $score -= 4
}

if ($realFiles.Count -lt 2) {
    $warnings.Add('Very few real daily logs available')
    $score -= 4
}

if ($largestBytes -gt 20000) {
    $issues.Add('At least one active daily log is oversized (>20KB) and should be distilled')
    $score -= 12
} elseif ($largestBytes -gt 12000) {
    $warnings.Add('Largest daily log is getting bulky (>12KB)')
    $score -= 4
}

$recencyOk = $false
if ($recentReal.Count -gt 0) {
    $latest = $recentReal | Select-Object -First 1
    if ($latest.LastWriteTime -gt (Get-Date).AddDays(-3)) {
        $recencyOk = $true
    }
}
if (-not $recencyOk) {
    $warnings.Add('No recent real daily memory updates in the last 3 days')
    $score -= 6
}

if ($score -lt 0) { $score = 0 }
if ($score -gt 100) { $score = 100 }

$overall = switch ($score) {
    { $_ -ge 90 } { 'ELITE'; break }
    { $_ -ge 75 } { 'HEALTHY'; break }
    { $_ -ge 55 } { 'NEEDS ATTENTION'; break }
    default { 'CRITICAL' }
}

[pscustomobject]@{
    AsOf = $AsOf
    OverallHealth = $overall
    Score = $score
    DailyFiles = $dailyFiles.Count
    PlaceholderFiles = $placeholderFiles.Count
    ArchivedPlaceholderFiles = $archivedPlaceholders
    RealFiles = $realFiles.Count
    MemoryLines = $memoryLines
    EntityFiles = $entityFiles.Count
    RecentRealFilesCount = $recentReal.Count
    Issues = @($issues)
    Warnings = @($warnings)
    LargestFiles = @($largestFiles | ForEach-Object { [pscustomobject]@{ Name = $_.Name; Bytes = $_.Length; LastWriteTime = $_.LastWriteTime } })
    RecentRealFiles = @($recentReal | ForEach-Object { [pscustomobject]@{ Name = $_.Name; Bytes = $_.Length; LastWriteTime = $_.LastWriteTime } })
    EntityFileNames = @($entityFiles | ForEach-Object { $_.Name })
    HeartbeatLast = if ($heartbeat) { $heartbeat.lastHeartbeatTimestamp } else { $null }
    PendingWorkCount = if ($heartbeat -and $heartbeat.pendingWorkQueue) { @($heartbeat.pendingWorkQueue).Count } else { 0 }
} | ConvertTo-Json -Depth 6
