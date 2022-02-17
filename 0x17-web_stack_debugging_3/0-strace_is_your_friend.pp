# fixes Apache 500 error by fixing typo in wordpress

exec { 'Changing word to fix 500 server error':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => shell,
}
