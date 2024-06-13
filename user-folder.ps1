# Import Active Directory Module
Import-Module ActiveDirectory

# Get all users in the domain
$users = Get-ADUser -Filter *

# Loop through each user
foreach ($user in $users) {
    # Define the folder path (assuming each user will have a directory named after their username under D:\Shares)
    $folderPath = "D:\Shares\" + $user.SamAccountName

    # Ensure the user directory exists
    if (-Not (Test-Path $folderPath)) {
        New-Item -Path $folderPath -ItemType Directory
    }
}

