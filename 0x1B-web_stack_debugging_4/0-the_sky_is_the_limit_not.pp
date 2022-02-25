#Fix limit connections 

exec { 'fix limit connections':
        command => 'sed -i s/15/4069/ /etc/default/nginx; sudo service nginx restart',
        path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
