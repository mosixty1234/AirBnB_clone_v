# install and configure an Nginx server using Puppet
package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

file { ['/data', '/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
}

file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test'],
}

file { '/data/web_static/releases/test/index.html':
  ensure   => 'file',
  content  => 'Holberton School',
  require  => Pachage['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
    listen 80 default_server;
    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location /hbnb_static/ {
                alias /data/web_static/current/;
                index index.html;
    }

    location / {
        root /var/www/html;
        index index.html;
    }
}",
  require => Package['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
