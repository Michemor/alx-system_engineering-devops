# kills a process named killmenow

exec {'killmenow':
  command => '/usr/bin/pkill killmenow',
  returns => 0,
}
