# automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'update':
    command => 'usr/bin/env apt-get -y update',
}
package {
    'nginx':
    ensure => installed,
}
file { '/var/www/html/index.html':
    content => 'Hello World!'
}

file_line { 'adding header':
    line  => '\tadd_header X-Served-By $HOSTNAME;',
    path  => '/etc/nginx/sites-available/default',
    after => 'listen 80 default_server;',
}

service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}
