#Fix Apache  returning a 500 error
include stdlib

$config_file = '/var/www/html/wp-settings.php'
$replacer = "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );"


#This resource makes required replacement
file_line { 'Load library':
  ensure   => present,
  path     => $config_file,
  line     => $replacer,
  match    => '.*class-wp-locale.phpp.*',
  multiple => false,
}
