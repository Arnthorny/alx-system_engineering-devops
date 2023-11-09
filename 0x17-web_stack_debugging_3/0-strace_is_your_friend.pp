#Fix Apache  returning a 500 error

$config_file = '/var/www/html/wp-settings.php'


#This resource makes required replacement
exec { 'fix-wordpress':
  command => "/bin/sed -E -i 's/.phpp/.php/' ${config_file}"
}
