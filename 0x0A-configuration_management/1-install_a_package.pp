#this puppet file installs a package

exec { 'install-flask':
  command => 'pip3 install Flask',
  path    => ['/usr/bin', '/bin'],  # Add any other directories to the path if necessary
  unless  => 'pip3 show Flask',     # Ensure Flask is not already installed
}
