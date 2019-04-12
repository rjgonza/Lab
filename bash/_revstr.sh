_revstr() #@ USAGE: revstr STRING 
{
	var=$1
	_REVSTR=
	while [ -n "$var" ]; do
		temp=${var%?}
		_REVSTR=${var#"$temp"}
		var=${var%?}
		printf %s $_REVSTR
	done 
	echo
}
