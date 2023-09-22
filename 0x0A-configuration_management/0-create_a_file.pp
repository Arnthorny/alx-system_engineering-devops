#Creating a file with puppet with given permissions and content

$cnt = 'I love Puppet'

file { '/tmp/school/':
  ensure  => 'file',
  content => $cnt,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}
