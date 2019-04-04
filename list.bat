set YYYYmmdd=%date:~0,4%%date:~5,2%%date:~8,2%
set hhmiss=%time:~0,2%%time:~3,2%%time:~6,2%
set "filename=softwarelist%YYYYmmdd%_%hhmiss%.log"

hostname >>%filename%
powershell  "Get-WmiObject -class Win32_Product | Select-Object -Property name,vendor,version" >>%filename%
