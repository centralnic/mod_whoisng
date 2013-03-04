mod_whoisng
===========

mod_whoisng is an Apache 2.x module which implements a Whois/NICNAME (RFC 3912)
service. Whois queries received from clients are converted into internal 
requests which can be handled in the same way as HTTP requests (ie PHP script,
CGI script, static content, etc).


INSTALLATION
============

To install mod_whoisng, type this command:

    apxs -i -a -c mod_whoisng.c

You will need the Apache development headers to be installed.


CONFIGURATION
=============

The simplest possible configuration for mod_whoisng is as follows:

    Listen 43

    <VirtualHost *:43>
        WhoisProtocol On
    </VirtualHost>

With this configuration, inbound whois queries will be mapped to the URI
`/cgi-bin/whois?query=<query>`, with `<query>` properly quoted. `<query>` will
contain the complete string as sent by the whois client, so if the client sends
a query like

    -i admin-c TEST-HANDLE

the CGI will receive the string

    -i%20admin-c%20TEST-HANDLE

in the CGI variable named "query". No parsing of flags is done in the module, 
this is up to script handling the URI.

To change the mapping destination, add to your httpd.conf:

    WhoisPrefix "GET /whois.php?searchstring="

(WhoisPrefix will have the whois query appended). You can not only map
queries to scripts, but also to static content:

    WhoisPrefix "GET /whoisinfo/" 

will make Apache try to retrieve `/whoisinfo/bla` if asked for "bla".
 
Attention: Be aware that if an 404 occurs, the client is presented with an ugly
HTML error message (which will contain the mapped URI). So, if you map to static
content, you may want to add (for example):

    ErrorDocument 404 /whoisinfo/404.txt

which contains appropriate error message to your installation. You may also
want to add an 

    ErrorDocument 500 /whoisinfo/500.txt

in case your CGI fails (e.g. to connect to your backend database).


LICENSE
=======

Please see the LICENSE file in the source distribution.


HISTORY
=======

mod_whoisng is a fork of the mod_whois module, originally written by Alexander
Mayrhofer <axelm@nic.at>. The license used for mod_whois prohibited reuse of
the name "mod_whois" so "mod_whoisng" was chosen as the new name.