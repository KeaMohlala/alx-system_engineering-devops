# Puppet manife that kills process named 'killmenow'

exec { 'kill_killmenow':
command => 'pkill killmenow',
onlyif  => 'pgrep killmenow',
}
