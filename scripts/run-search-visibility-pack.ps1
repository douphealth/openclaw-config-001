param(
  [string]$Manifest = "C:\Users\User\.openclaw\workspace\.secrets\search\sites.json",
  [string]$StartDate,
  [string]$EndDate,
  [string]$ServiceAccount = $env:GSC_SERVICE_ACCOUNT_JSON,
  [string]$BingApiKey = $env:BING_WEBMASTER_API_KEY,
  [string]$OutRoot = "C:\Users\User\.openclaw\workspace\ops\search-data"
)

if (-not $StartDate -or -not $EndDate) {
  Write-Error "Usage: .\run-search-visibility-pack.ps1 -StartDate YYYY-MM-DD -EndDate YYYY-MM-DD [-Manifest path]"
  exit 2
}

$script = "C:\Users\User\.openclaw\workspace\skills\api-integration-builder\scripts\run_search_visibility_pack.py"
if (-not (Test-Path $script)) {
  Write-Error "Runner script not found: $script"
  exit 2
}

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
  Write-Error "python not found on PATH. Install Python or run the runner with a full interpreter path."
  exit 2
}

& python $script `
  --manifest $Manifest `
  --start-date $StartDate `
  --end-date $EndDate `
  --service-account $ServiceAccount `
  --bing-api-key $BingApiKey `
  --outroot $OutRoot

exit $LASTEXITCODE
