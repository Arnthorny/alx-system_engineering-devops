# install flask from pip3.

$pckg = 'flask'
package { 'Flask':
  ensure   => '2.1.0',
  name     => $pckg,
  provider => 'pip3'
}
