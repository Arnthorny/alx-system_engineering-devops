#  SSH configuration file so that you can connect to a server without password

include stdlib

$file = '/etc/ssh/ssh_config'

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => $file,
  line   => 'PasswordAuthentication no'
}

file_line { 'Declare identity file':
  ensure => present,
  path   => $file,
  line   => 'IdentityFile ~/.ssh/school'
}
