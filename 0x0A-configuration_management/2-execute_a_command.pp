# create a manifest that kills a process named killmenow

$cmd = '/usr/bin/pkill killmenow'

exec { 'Kill processs':
  command => $cmd
}
