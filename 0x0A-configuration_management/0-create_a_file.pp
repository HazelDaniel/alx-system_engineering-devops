# this is a puppet manifest responsible for creating a file called "school" in the /tmp directory

file { '/tmp/school':
  ensure  => file,
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet',
}
