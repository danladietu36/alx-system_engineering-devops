# This puppet script increases the amount of traffic Nginx server can handle

# This code increass the ULIMIT the default file
exec { 'fix--nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# This code restarts Nginx
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
