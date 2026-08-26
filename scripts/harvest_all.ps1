# harvest_all.ps1 — ไล่ทุก dataset สัญญา 2558-2568 แล้วเขียนสถานะลง _tmp_harvest.log
$w = Join-Path $env:USERPROFILE "OneDrive\Claude\Projects\RMN-eBidding-Workflow"
$out = Join-Path $w "_tmp_harvest.jsonl"
$log = Join-Path $w "_tmp_harvest.log"
Remove-Item $out,$log -Force -ErrorAction SilentlyContinue
$sets = @(
 'cgd-contract-2558','cgd-contract-2559','cgd-contract-2560','cgd-contract-2561',
 'cgd-contract-2562','cgd-contract-2563','cdg-contract-2564','cdg-contract-2565',
 'cdg-contract-2566','cdg-contract-2567','egp-contact-2568'
)
"START $(Get-Date -Format s)" | Out-File $log -Encoding UTF8
foreach($d in $sets){
  $r = & (Join-Path $w "scripts\harvest_egp.ps1") -Dataset $d -Out $out
  ($r -join ' ') | Out-File $log -Append -Encoding UTF8
}
"DONE $(Get-Date -Format s)" | Out-File $log -Append -Encoding UTF8
