# Install Nginx if not already installed
package { 'nginx':
  ensure => 'installed',
}

# Create necessary directories if they don't exist
file { ['/data', '/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  content => 'Holberton School',
}

file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test'],
}

file { '/data':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/etc/nginx/sites-available/hbnb_static':
  content => "server {
      listen 80;
      server_name mydomainname.tech;

      location /hbnb_static/ {
          alias /data/web_static/current/;
          index index.html;
      }

      location / {
          add_header X-Served-By $hostname;
      }

      error_page 404 /404.html;
      location = /404.html {
          internal;
      }
  }",
  require => Package['nginx'],
}

file { '/etc/nginx/sites-enabled/hbnb_static':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/hbnb_static',
  require => File['/etc/nginx/sites-available/hbnb_static'],
}
