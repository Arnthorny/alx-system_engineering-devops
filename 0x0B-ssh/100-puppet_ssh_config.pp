# create a manifest that kills a process named killmenow

$file = '/etc/ssh/sshd_config'

file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => $file,
  line   => 'BatchMode yes'
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => $file,
  line   => 'IdentityFile ~/.ssh/school'
}
