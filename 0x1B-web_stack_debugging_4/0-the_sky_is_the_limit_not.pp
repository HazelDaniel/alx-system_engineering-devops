# This manifest file changes the amount of traffic an Nginx server can handle from 15 to 4096

# change the ULIMIT in the default
exec { 'nginx-fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'grep -q "15" /etc/default/nginx'
}

# Restart nginx daemon
-> exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
  after   => Exec['nginx-fix']
}
