dnsRedir
========

A small command-line DNS server written in Python

Tim Newsham <tim at isecpartners dot com>
27 Jun 2013


Overview
=======

dnsRedir.py is a small DNS server that will respond to certain
queries with addresses provided on the command line. All other
queries will be proxied to a "real" name server. This program
can be used to redirect a few domain names to test addresses for 
the purpose of security and protocol testing.

Similar programs:
   dnschef: https://thesprawl.org/projects/dnschef/


QUICKSTART
=======

    $ ./dnsRedir.py -p 1053 'A:www\.evil\.com\.:1.2.3.4' &
    $ dig -p 1053 www.evil.com @localhost
    $ dig -p 1053 www.google.com @localhost
    


DEPENDENCIES
=======

dnsRedir.py requires Python 2.5 or greater. It does not require
any other dependencies and can be run from a single source file.


MANUAL
=======

NAME
    dnsRedir.py - A DNS server for redirecting traffic

SYNOPSIS
    dnsRedir.py [opts] [type:name:value ...]
    opts: [-6] [-b bindaddr] [-p port] [-d dnssrever] [-P dnsport] [-t ttl]

DESCRIPTION
    dnsRedir.py is a small DNS server that can answer some requests 
    and proxy other requests to a real DNS server. The server listens 
    for DNS requests on UDP port 53 of all network interfaces. This
    behavior can be altered with the 'd' and 'b' options.
    When a request is received it is answered immediately if it has
    a single query that matches one of the names specified on the 
    command line. Otherwise the request is proxied to the DNS server 
    specified by the 'd' and 'P' options (defaulting to "8.8.8.8" port 53).

    The command arguments provide a list of DNS queries and their answer. 
    Each argument is of the form "type:name:value". The type specifies 
    a supported DNS query type such as "A" for address lookups.
    The name specifies a regular expression used to match incoming
    domain name queries. The pattern must match the entire query,
    including the trailing dot of a domain name.  The value specifies 
    the value to return when an incoming query is received that matches 
    the type and name. The format for the value varies and depends on 
    the type.  The following query types are supported by dnsRedir.py:

        A   - Address lookups. The value must be an IP address
              in dotted-quad format.

    All names are checked in order and the value associated with the
    first matching pattern is used in creating a response.  All
    responses are sent with a TTL of 30 seconds, which can be overriden
    with the 't' option.

    When the '6' option is specified, the server listens to requests
    and proxies requests using IPv6 instead of IPv4. If possible, the
    server will also listen for IPv4 requests (using IPv4-compatibility 
    socket options). Note that any DNS server specified with 'd'
    must be a valid IPv6 address when using this option. To use an
    IPv4 DNS server, it must be specified in IPv6 format such as
    "::ffff:127.0.0.1".

EXAMPLES
    The following command causes the server to listen on port 1053 and
    proxy all requests to the default nameserver ("8.8.8.8"):

       $ ./dnsRedir.py -p 1053 

    The following command causes the server to respond to address queries
    for "www.evil.com" with the address "1.2.3.4". All other queries
    are answered by the default nameserver ("8.8.8.8"). Note that
    dots are escaped so that they are matched literally and not treated
    as a regular expression wildcards:

       $ ./dnsRedir.py 'A:www\.evil\.com\.:1.2.3.4'

    The following command causes the server to respond to address queries
    for any host in "evil.com" with the address "1.2.3.4", address queries
    for any host containing the word "magic" with "1.2.3.5" and to proxy
    all other requests through to the DNS server at "72.235.80.12".  
    Requests are received over IPv6 and IPv4. Note that the DNS server
    is specified as an IPv4-in-IPv6 address to use an IPv4 DNS server
    when using the '-6' option:
    
       $ ./dnsRedir.py -6 -d ::ffff:72.235.80.12 \
                       'A:.*\.evil\.com\.:1.2.3.4' 'A:.*magic.*:1.2.3.5'


BUGS
    The server is not written for performance, robustness or security. 

    Proxied requests use sequential request IDs. This leaves the
    server vulnerable to ID prediction attacks that can be used
    to spoof responses.

    The server will fail if all request IDs are used when proxying
    a large number of requests.
