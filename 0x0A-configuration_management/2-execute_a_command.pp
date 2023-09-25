#this executes a command to stop a process in puppet

exec { "pkill":
	command => "pkill -9 ./killmenow",
	path => ['/usr/bin', '/usr/sbin', '/bin']
}
