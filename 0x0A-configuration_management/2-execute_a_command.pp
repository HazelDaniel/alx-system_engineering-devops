# this manifest kills a process named killmenow

file { '/usr/bin/pkill':
  ensure => present,
}

exec { 'kill killmenow':
  command => '/usr/bin/pkill killmenow',
  require => File['/usr/bin/pkill']
}
