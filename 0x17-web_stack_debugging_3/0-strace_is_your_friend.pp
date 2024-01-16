# A typo was found in the /var/www/html/wp-settings.php (one of the wordpress core configuration files)
# This puppet file fixes it

exec { 'fix-wp-conf':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
