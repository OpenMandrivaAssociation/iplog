Summary:	Logs TCP, UDP, and ICMP connections to syslog
Name:		iplog
Version:	2.2.3
Release:	%mkrel 15
License:	GPL
Group:		Monitoring
URL:		http://ojnk.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}
Source2:	%{name}.conf
Patch0:		%{name}-2.2.3-gcc-3.3.patch
Requires(post): rpm-helper
Requires(preun): rpm-helper
Buildrequires:	libpcap-devel 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
iplog is a TCP/IP traffic logger. Currently, it is capable of logging TCP, UDP
and ICMP traffic. Adding support for other protocols should be relatively easy.
iplog contains a built-in packet filter, allowing for logging or excluding
packets that fit a given set of criteria.

%prep

%setup -q
%patch0 -p1 -b .gcc3.3

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

install -m755 %SOURCE1 -D %{buildroot}/%{_initrddir}/%{name}
install -m644 %SOURCE2 -D %{buildroot}/%{_sysconfdir}/%{name}.conf

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README TODO NEWS
%attr(0755,root,root) %{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sbindir}/*
%{_mandir}/man5/*
%{_mandir}/man8/*


