# Automate the task of creating a custom HTTP header response, but with Puppet.
# The value of the custom HTTP header must be the hostname of the server Nginx is running on

include stdlib

$repl_dir="\t\tadd_header X-Served-By \$hostname;\n\t}"
$config_file = '/etc/nginx/sites-available/default'



# This exec resource runs the `apt-get update` command
exec { 'apt update':
  command => '/usr/bin/apt-get update'
}

# This package resource installs the `nginx` package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt update']
}

# This service resource declares the nginx service
service { 'nginx':
  ensure => running,
  enable => true
}

# This resource replaces the closing brace with a location context.
file_line { 'Custom header':
  ensure   => present,
  path     => $config_file,
  line     => $repl_dir,
  match    => "^\t}$",
  multiple => false,
  require  => Package['nginx'],
  notify   => Service['nginx']
}
