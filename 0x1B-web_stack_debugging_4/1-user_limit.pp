# A puppet script taht enable user holberton to login and open files

# This code increases hard file limit for user holberton
exec { 'increase-hard-file-limit-for-holberton-user':
    command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/'
}
