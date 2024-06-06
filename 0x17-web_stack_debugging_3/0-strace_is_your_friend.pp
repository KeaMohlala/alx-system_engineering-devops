# this manifest replaces all instances of "phpp" with "php"

exec { 'Fix Typo in wp-settings.php':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin', '/usr/sbin/'],
  onlyif  => 'grep -q "phpp" /var/www/html/wp-settings.php',
}
