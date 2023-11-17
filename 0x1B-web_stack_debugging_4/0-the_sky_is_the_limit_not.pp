# Fix Apache failing to complete requests

$config_file = '/etc/default/nginx'


#This resource removes last line from file
exec { 'fix--for-nginx':
  provider => shell,
  command  => "sed -i '\$d' ${config_file} && echo 'ULIMIT=\"-n 4096\"' >> ${config_file}",
  before   => Exec['restart-nginx']
}

# This service resource declares the nginx service
exec { 'restart-nginx':
  provider => shell,
  command  => 'service nginx restart'
}
