# Change the OS configuration so that it is possible to
# login with the holberton user and open a file without any error message.

# Comment out two lines in the given limits config file
$config_file = '/etc/security/limits.conf'

exec { 'change-os-configuration-for-holberton-user':
  command  => "/bin/sed -i -E \'s/^(holberton.*)$/# \\1/\' ${config_file}"
}
