#!/bin/bash

FILE_LOCATION="/home/rgonzalez/Downloads"
FILE_DESTINATION="/mnt/portal/INCOMMING"
SCAN_COMMAND="clamscan"
SHARE_NAME="Donwloads"

get_files() {
	cd $FILE_LOCATION
	echo "Checking the files that have been downloaded for viruses, if they are clean they will be copied over" | tee logger
	for file in $(ls); do
		scan_file $file
		if [[ $? -ne 0 ]]; then
			echo "File: $file did not pass the virus check, it will not be copied" | tee logger
		else
			echo "File: $file passed" | tee logger
			cp $file $FILE_DESTINATION
		fi
	done
}

scan_file() {
	if [[ $SCAN_COMMAND $1 ]]; then
		echo "Scanned $1 and it is clean!" | tee logger
		return 0
	else
		echo "Scanned $1 and it is infected" | tee logger
		return 1
		fi
}

check_mount() {
	mount | grep -q vboxsf | grep -q ${FILE_DESTINATION}
	if [[ $? -eq 0 ]]; then
		echo "Found the mount" | tee logger
		return 0
	else
		echo "Need to mount the share" | tee logger
		return 1
	fi
	
}

mount_shared_drive(){
	mount -t vboxfs $SHARE_NAME $FILE_DESTINATION
	[[ $? -eq 0 ]] && echo "Mounting was successful" | tee logger
}

check_mount
[[ $? -ne 0 ]] && mount_shared_drive

get_files

if [[ ${BAD_FILES[#]} -gt 0 ]]; then
	echo "Some files were bad and will not be copied over!" | tee logger
	for((i=0; i<${#BAD_FILES[@]}; i++)); do
		echo "File: ${BAD_FILES[$i]} did not pass the virus scan and will no be copied over" | tee logger
	done
fi
