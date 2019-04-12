#!/bin/bash
_revstr() #@ USAGE: revstr STRING 
{
	var=$1
	_REVSTR=
	while [ -n "$var" ]; do
		temp=${var%?}
		[[ $temp =~ " " ]] && continue
		_REVSTR=${var#"$temp"}
		var=${var%?}
		printf %s $_REVSTR
	done 
	echo
}

is_palindrome() {
	#_is_palindrome $1
	reversed=$(_revstr $1)
	if [[ $reversed =~ $1 ]]; then
		printf "%s\n" "This string is a palindrome!"
	else
		printf "%s\n%s\n" "This string is not a palindrome because" "$reversed is not the same as $1"
	fi
}
