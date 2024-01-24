# With this manifest, the user 'holberton' can login and open files without the 'too many files to open' error

# increases hard file limit
exec { 'inc-hard-file-limit-for-holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'grep -Pq "holberton\s*hard.*5$" /etc/security/limits.conf'
}

# increases soft file limit
exec { 'inc-soft-file-limit-for-holberton':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'grep -Pq "holberton\s*soft.*4$" /etc/security/limits.conf'
}
