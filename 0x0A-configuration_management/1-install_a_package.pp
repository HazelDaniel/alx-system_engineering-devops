# this puppet manifest installs flask 2.1.0 from pip3

file {'/usr/bin/pip3':
  ensure => present,
}

exec {'flask-install':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  require => File['/usr/bin/pip3'],
  unless  => '/usr/bin/pip3 show Flask'
}
