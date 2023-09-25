#this puppet file installs a package

exec { 'install-flask':
  command => 'pip3 install Flask',
  path    => ['/usr/bin', '/bin'],
  unless  => 'pip3 show Flask',
}
