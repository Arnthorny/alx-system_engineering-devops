# Fix Apache failing to complete requests

$config_file = '/etc/default/nginx'


#This resource removes last line from file
exec { 'fix--for-nginx':
  command => "/bin/sed -i '\$d' ${config_file}"
}
