# automate the task of creating a custom HTTP header response, but with Puppet.

$custom_header = "add_header X-Served-By ${hostname};"

exec { 'update':
    command => 'usr/bin/apt-get update',
}
-> package {'nginx':
    ensure  => installed,
    require => Exec['update']
}

-> file_line { 'adding header':
    ensure => 'present',
    line   => $custom_header,
    path   => '/etc/nginx/sites-available/default',
    after  => 'listen 80 default_server;',
}

-> file_line { 'Add redirection, 301':
    ensure => 'present',
    path   => '/etc/nginx/sites-available/default',
    after  => 'listen 80 default_server;',
    line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

-> file { '/var/www/html/index.html':
    content => 'Hello World',
}

-> service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}
