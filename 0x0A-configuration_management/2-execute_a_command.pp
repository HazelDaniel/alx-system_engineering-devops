#this executes a command to stop a process in puppet

exec { 'kill killmenow':
  command => 'pkill -9 -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
