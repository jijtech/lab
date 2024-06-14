Get-WinEvent -LogName Setup | ForEach-Object {
    "`t* $($_.TimeCreated) - $($_.LevelDisplayName) - $($_.Message)" | Out-File "SetupLogs.txt" -Append
}
