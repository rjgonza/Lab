#!/bin/bash

#BAD_FILES=()

get_files() {
	FILE_LOCATION=""
	cd $FILE_LOCATION
	echo "Checking the files that have been downloaded for viruses, if they are clean they will be copied over" | tee logger
	for file in $(ls); do
		scan_file $file
		if [[ $? -ne 0 ]]; then
			#BAD_FILES=( ${BAD_FILES[@]} $file )
			echo "File: $file
		else
			copy_file $file
		fi
	done
}

scan_file() {
	SCAN_COMMAND=""
	if [[ $SCAN_COMMAND $1 ]]; then
		echo "Scanned $1 and it is clean!" | tee logger
		return 0
	else
		echo "Scanned $1 and it is infected" | tee logger
		return 1
		fi
}

copy_file() {
	
}

check_mount() {
}

mount_shared_drive(){
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
