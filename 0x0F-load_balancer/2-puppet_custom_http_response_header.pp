# automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'usr/bin/env apt-get -y update':
}
package {
    'nginx':
    ensure => installed,
}
file { '/var/www/html/index.html':
    content => 'Hello World'
}

file_line { 'adding header':
    ensure => present,
    line   => '\tadd_header X-Served-By ${hostname};',
    path   => '/etc/nginx/sites-available/default',
    after  => 'server_name _;',
}

service { 'nginx':
    ensure => running,
}
