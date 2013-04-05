# $Id$
Name:		mod_whoisng
Version:	0.1
Release:	2
Summary:	Apache WHOIS Server Module
Group:		System Environment/Daemons
URL:		http://sourceforge.net/projects/modwhois
License:	Apache Software License
Source:		http://prdownloads.sourceforge.net/modwhois/%{name}-%{version}.tar.gz
Requires:	httpd
BuildRequires:	httpd-devel
BuildRoot:	%{_tmppath}/root-%{name}-%{version}

%description
mod_whoisng enables Apache (version 2) to receive standard WHOIS queries, and
rewrites them to standard HTTP requests. The request can then be processed by
the usual means (static content, CGIs, PHP, tomcat, whatever).

%prep

%setup

%build
apxs -c %{name}.c

%install
mkdir -p %{buildroot}%{_libdir}/httpd/modules %{buildroot}/etc/httpd/conf.d
install -m 0755 .libs/%{name}.so %{buildroot}%{_libdir}/httpd/modules/
cat <<END > httpd.conf.example
LoadModule whois_module modules/%{name}.so

Listen 43

# example whois virtualhost, assumes a PHP-based setup:
<VirtualHost *:43>
	WhoisProtocol		On
	Alias			/whois /usr/local/whois
	WhoisPrefix		"GET /whois/whois.php?domain="
</VirtualHost>

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc LICENSE README httpd.conf.example
%{_libdir}/httpd/modules/%{name}.so

%changelog
* Fri Apr  5 2013 Gavin Brown <epp@centralnic.com> 0.2-1
- Updated %install section so that install works properly on x86_64
- don't put a config file in /etc/httpd/conf.d

* Mon Mar  4 2013 Gavin Brown <epp@centralnic.com> 0.2-1
- Updated for mod_whoisng

* Fri Oct 13 2006 Gavin Brown <epp@centralnic.com> 0.1-1
- Initial package
