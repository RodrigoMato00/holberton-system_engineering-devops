#make changes to our configuration file

exec { 'echo':
  path    => '/bin/',
  command => 'echo "IdentityFile ~/.ssh/school\n PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
