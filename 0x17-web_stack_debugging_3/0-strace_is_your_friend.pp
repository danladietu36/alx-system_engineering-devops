# A puppet script that replaces a line of code in a file on a server

$file = "/var/html/wp-settings.php"

#code to replace the line

exec { 'replace_line':
    command => "sed -i 's/phpp/php/g' ${file}",
    path => ['/bin', '/usr/bin']
}
