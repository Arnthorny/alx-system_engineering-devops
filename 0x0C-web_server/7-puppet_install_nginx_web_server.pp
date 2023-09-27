#  SSH configuration file so that you can connect to a server without password

include stdlib

$file_root = '/var/www/html'
$index_cnt = "Hello World!\n"
$config_file = '/etc/nginx/sites-available/default'
$redirect_directive="\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n}"



# This exec resource runs the `apt-get update` command
exec { 'apt update':
  command => '/usr/bin/apt-get update'
}

# This package resource installs the `nginx` package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt update']
}

# This file resource provisions an index page html file
file { "${file_root}/index.html":
  ensure  => 'file',
  content => $index_cnt,
  require => Package['nginx']
}

# This service resource declares the nginx service
service { 'nginx':
  ensure => running,
  enable => true
}

# This resource replaces the closing brace with a location context.
file_line { '301 redirect':
  ensure   => present,
  path     => $config_file,
  line     => $redirect_directive,
  match    => '^}$',
  multiple => false,
  require  => Package['nginx'],
  notify   => Service['nginx']
}
