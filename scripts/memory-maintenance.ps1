param(
    [string]$Workspace = (Get-Location).Path
)

$root = $Workspace
$archiveScript = Join-Path $root 'scripts\archive-placeholder-memory.ps1'
$healthScript = Join-Path $root 'scripts\memory-health-check.ps1'
$distillScript = Join-Path $root 'scripts\memory-distill.ps1'
$artifactDir = Join-Path $root 'artifacts\memory'
New-Item -ItemType Directory -Force -Path $artifactDir | Out-Null
$today = Get-Date -Format 'yyyy-MM-dd'
$dashboardPath = Join-Path $artifactDir ("$today-memory-dashboard.json")

$actions = @()

if (Test-Path $archiveScript) {
    $archiveResult = & $archiveScript -Workspace $root | ConvertFrom-Json
    if ($archiveResult.MovedCount -gt 0) {
        $actions += "Archived $($archiveResult.MovedCount) placeholder daily files"
    }
}

if (Test-Path $distillScript) {
    $datesToCheck = @((Get-Date).AddDays(-1), (Get-Date).AddDays(-2), (Get-Date).AddDays(-3)) | ForEach-Object { $_.ToString('yyyy-MM-dd') }
    foreach ($d in $datesToCheck) {
        try {
            $distillResult = & $distillScript -Workspace $root -Date $d | ConvertFrom-Json
            if ($distillResult.NeedsDistill) {
                $actions += "Distill needed for $d"
            }
        } catch {
            $actions += "Distill check failed for ${d}: $($_.Exception.Message)"
        }
    }
}

$health = & $healthScript -Workspace $root | ConvertFrom-Json

if ($health.Score -lt 90) {
    $actions += "Memory score below elite threshold: $($health.Score)"
}
if ($health.PlaceholderFiles -gt 0) {
    $actions += "Active placeholder files remain: $($health.PlaceholderFiles)"
}
if ($health.Warnings.Count -gt 0) {
    foreach ($warning in $health.Warnings) { $actions += "Warning: $warning" }
}
if ($health.Issues.Count -gt 0) {
    foreach ($issue in $health.Issues) { $actions += "Issue: $issue" }
}

$dashboard = [pscustomobject]@{
    Date = $today
    Score = $health.Score
    OverallHealth = $health.OverallHealth
    PlaceholderFiles = $health.PlaceholderFiles
    ArchivedPlaceholderFiles = $health.ArchivedPlaceholderFiles
    EntityFiles = $health.EntityFiles
    MemoryLines = $health.MemoryLines
    Issues = @($health.Issues)
    Warnings = @($health.Warnings)
    Actions = @($actions)
    LargestFiles = @($health.LargestFiles)
}

$dashboard | ConvertTo-Json -Depth 6 | Set-Content -Path $dashboardPath -Encoding UTF8
$dashboard | ConvertTo-Json -Depth 6
