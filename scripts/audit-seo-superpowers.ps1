param(
  [string]$RepoRoot = (Get-Location).Path
)

$targets = @(
  'seo-command-center','editorial-post-enhancement','content-strategy-planning','schema-ops','seo-intelligence','seo-competitor-analysis','conversion-copywriting','copy-editing-sweeps','ai-visibility','keyword-research-mastery'
)

$results = foreach($name in $targets){
  $skill = Join-Path $RepoRoot "skills-approved/$name/SKILL.md"
  $raw = if(Test-Path $skill){ Get-Content $skill -Raw } else { '' }
  [pscustomobject]@{
    skill = $name
    exists = (Test-Path $skill)
    hasSharedSuperpowers = $raw -match 'seo-aeo-geo-superpowers\.md'
    hasCitationScorecard = $raw -match 'ai-citation-scorecard\.md'
    hasSerpResearchProtocol = $raw -match 'serp-ai-research-protocol\.md'
    hasSotaLayer = $raw -match 'SOTA'
  }
}

[pscustomobject]@{
  checked = $results.Count
  withSharedSuperpowers = @($results | Where-Object hasSharedSuperpowers).Count
  withCitationScorecard = @($results | Where-Object hasCitationScorecard).Count
  withSerpResearchProtocol = @($results | Where-Object hasSerpResearchProtocol).Count
  withSotaLayer = @($results | Where-Object hasSotaLayer).Count
  missing = @($results | Where-Object { -not $_.hasSotaLayer } | Select-Object -ExpandProperty skill)
  results = @($results)
} | ConvertTo-Json -Depth 4
