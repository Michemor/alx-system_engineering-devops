# Increase the number of requests handled by nginx server

exec { 'nginx-limit':
  command => 'sed -i "s/15/2048" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

-> exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d'
}
