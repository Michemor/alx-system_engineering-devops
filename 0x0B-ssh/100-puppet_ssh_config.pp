# uses puppet to make changes to local ssh config file
include 'stdlib'

file_line {'Turn off passwd auth':
  ensure => present,
  path   => '/home/.ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line {'Declare identity file':
  ensure => present,
  path   => '/home/.ssh/config',
  line   => 'IdentityFile /home/.ssh/school',
}
