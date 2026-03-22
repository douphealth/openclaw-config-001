param(
    [string]$Workspace = (Get-Location).Path,
    [switch]$WhatIfMode
)

$memoryDir = Join-Path $Workspace 'memory'
$archiveDir = Join-Path $Workspace 'artifacts\memory\placeholder-daily-archive'
New-Item -ItemType Directory -Force -Path $archiveDir | Out-Null

$today = (Get-Date).ToString('yyyy-MM-dd')
$yesterday = (Get-Date).AddDays(-1).ToString('yyyy-MM-dd')

$files = Get-ChildItem $memoryDir -File -Filter '*.md' |
    Where-Object { $_.BaseName -match '^\d{4}-\d{2}-\d{2}$' -and $_.Length -le 30 -and $_.BaseName -notin @($today, $yesterday) }

$moved = @()
foreach ($file in $files) {
    $dest = Join-Path $archiveDir $file.Name
    if (-not $WhatIfMode) {
        Move-Item -Force -Path $file.FullName -Destination $dest
    }
    $moved += [pscustomobject]@{
        Name = $file.Name
        Bytes = $file.Length
        Destination = $dest
    }
}

[pscustomobject]@{
    MovedCount = $moved.Count
    ArchiveDir = $archiveDir
    KeptToday = $today
    KeptYesterday = $yesterday
    Sample = @($moved | Select-Object -First 10)
} | ConvertTo-Json -Depth 4
