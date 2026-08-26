# harvest_egp.ps1 v2 — ดึงผลประมูลของกลุ่ม RMN จาก data.go.th (ไม่ต้องใช้ API key) ทีละ dataset
#
# ⚠️ v1 ใช้ค้นด้วย TIN → ได้ 0 แถวในชุดปีเก่า (2558-2565) = false negative
#    เพราะคอลัมน์ TIN ของชุดปีเก่าว่าง/ปิด · ค้นด้วยชื่อได้ผลจริง
# v2 ค้นด้วย "คำสั้น" 3 คำที่ทนการสะกดผิดของรัฐ แล้วให้ฝั่ง python คัดชื่อเป๊ะทีหลัง
#
# ใช้: powershell -File harvest_egp.ps1 -Dataset egp-contact-2568 -Out ...\_tmp_harvest.jsonl
param(
  [Parameter(Mandatory=$true)][string]$Dataset,
  [Parameter(Mandatory=$true)][string]$Out
)
$ProgressPreference='SilentlyContinue'
$queries = @("อาร์เอ็มเอ็น","ตักสิลา","รักดี")
try {
  $p=(Invoke-RestMethod ("https://data.go.th/api/3/action/package_show?id={0}" -f $Dataset) -TimeoutSec 120).result
} catch { "ERR package_show $Dataset : " + $_.Exception.Message; exit 1 }
$rids=@($p.resources | ForEach-Object { $_.id })
$enc=New-Object System.Text.UTF8Encoding($false)
$sw=New-Object System.IO.StreamWriter($Out,$true,$enc)
$n=0
foreach($rid in $rids){
  foreach($q in $queries){
    $off=0
    while($true){
      try{
        $u="https://data.go.th/api/3/action/datastore_search?resource_id={0}&q={1}&limit=1000&offset={2}" -f $rid,[uri]::EscapeDataString($q),$off
        $r=Invoke-RestMethod $u -TimeoutSec 180
      } catch { break }
      $recs=$r.result.records
      if(-not $recs -or $recs.Count -eq 0){ break }
      foreach($rec in $recs){
        $o = $rec | Add-Member -NotePropertyName '__ds' -NotePropertyValue $Dataset -PassThru -Force
        $sw.WriteLine( ($o | ConvertTo-Json -Depth 3 -Compress) )
        $n++
      }
      if($recs.Count -lt 1000){ break }
      $off += 1000
    }
  }
}
$sw.Close()
"{0} : resources={1} rows={2}" -f $Dataset,$rids.Count,$n
