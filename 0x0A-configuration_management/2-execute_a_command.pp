# this manifest kills a process named killmenow

file { '/usr/bin/pkill':
  ensure => present,
}

exec { 'kill killmenow':
  command => '/usr/bin/pkill -f killmenow',
  require => File['/usr/bin/pkill']
}
