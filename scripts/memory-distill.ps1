param(
    [string]$Workspace = (Get-Location).Path,
    [string]$Date = (Get-Date).AddDays(-2).ToString('yyyy-MM-dd')
)

$memoryDir = Join-Path $Workspace 'memory'
$artifactDir = Join-Path $Workspace 'artifacts\memory'
$rawDir = Join-Path $artifactDir 'raw'
New-Item -ItemType Directory -Force -Path $artifactDir | Out-Null
New-Item -ItemType Directory -Force -Path $rawDir | Out-Null

$target = Join-Path $memoryDir ("$Date.md")
if (-not (Test-Path $target)) {
    throw "Daily memory file not found: $target"
}

$file = Get-Item $target
$content = Get-Content $target -Raw
$summaryPath = Join-Path $artifactDir ("$Date-distilled-summary.md")
$rawPath = Join-Path $rawDir ("$Date.full.md")

$alreadyDistilled = Test-Path $summaryPath
$needsDistill = $file.Length -gt 12000 -and -not $alreadyDistilled

$result = [pscustomobject]@{
    Date = $Date
    Target = $target
    Bytes = $file.Length
    SummaryPath = $summaryPath
    RawPath = $rawPath
    AlreadyDistilled = $alreadyDistilled
    NeedsDistill = $needsDistill
    Actions = @()
}

if ($needsDistill) {
    if (-not (Test-Path $rawPath)) {
        Copy-Item -Path $target -Destination $rawPath
        $result.Actions += "Copied raw log to $rawPath"
    }
    $result.Actions += 'Manual summary file should be created or refreshed before replacing the active daily log.'
} else {
    $result.Actions += 'No auto-distill action required.'
}

$result | ConvertTo-Json -Depth 5
