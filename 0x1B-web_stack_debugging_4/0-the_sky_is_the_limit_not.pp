# A puppet script to increase Nginx traffic

#This code increases ULIMIT of default file
exec { 'fix--for-nginx':
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/usr/local/bin/:bin/'
}
# code to restart Nginx
exec { 'nginx restart':
    command => 'nginx restart'
    path    => '/etc/init.d/'
}
