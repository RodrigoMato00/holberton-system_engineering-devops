# login with the holberton user and open a file without any error message.

exec { 'soft' :
        command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 3000/g" /etc/security/limits.conf',
        path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}

exec { 'hard' :
        command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile unlimited/g" /etc/security/limits.conf',
        path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
