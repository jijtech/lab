# Define the path to save the backup files
$backupPath = "C:\Backup"

# Ensure the backup directory exists
if (-Not (Test-Path $backupPath)) {
    New-Item -Path $backupPath -ItemType Directory
}

# Import Active Directory Module
Import-Module ActiveDirectory

# Get all users in the domain
$users = Get-ADUser -Filter *

# Loop through each user
foreach ($user in $users) {
    # Define the source path (assuming each user has a directory named after their username under C:\Users)
    $sourcePath = "C:\Users\" + $user.SamAccountName

    # Define the destination path for the backup
    $destinationPath = $backupPath + "\" + $user.SamAccountName + "_backup_" + (Get-Date -Format "yyyyMMdd")

    # Check if the source directory exists
    if (Test-Path $sourcePath) {
        # Copy the user's files to the backup directory
        Copy-Item -Path $sourcePath -Destination $destinationPath -Recurse -Force
    }
}
# Define the partitions to be backed up
$partitions = @("B:", "D:")

# Loop through each partition
foreach ($partition in $partitions) {
    # Define the source path for the partition
    $sourcePath = $partition

    # Define the destination path for the backup
    $destinationPath = $backupPath + "\" + $partition.TrimEnd(':') + "_backup_" + (Get-Date -Format "yyyyMMdd")

    # Check if the source directory exists
    if (Test-Path $sourcePath) {
        # Copy the partition's files to the backup directory
        Copy-Item -Path $sourcePath -Destination $destinationPath -Recurse -Force
    }
}
