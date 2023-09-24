#the config puppet file for my cilent
include stdlib

file_line { 'Turn off passwd auth':
  ensure => present,
  line   => '    PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
  replace => true,
}

file_line { 'Delare identity file':
  ensure => present,
  line   => ' IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/ssh_config',
  replace => true,
}
