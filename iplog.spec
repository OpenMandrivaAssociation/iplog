Summary:	Logs TCP, UDP, and ICMP connections to syslog
Name:		iplog
Version:	2.2.3
Release:	27
License:	GPLv2
Group:		Monitoring
URL:		http://ojnk.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}
Source2:	%{name}.conf
Patch0:		%{name}-2.2.3-gcc-3.3.patch
Buildrequires:	pcap-devel 
Requires(post,preun):	rpm-helper

%description
iplog is a TCP/IP traffic logger. Currently, it is capable of logging TCP, UDP
and ICMP traffic. Adding support for other protocols should be relatively easy.
iplog contains a built-in packet filter, allowing for logging or excluding
packets that fit a given set of criteria.

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall

install -m755 %SOURCE1 -D %{buildroot}/%{_initrddir}/%{name}
install -m644 %SOURCE2 -D %{buildroot}/%{_sysconfdir}/%{name}.conf

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%doc AUTHORS COPYING README TODO NEWS
%attr(0755,root,root) %{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sbindir}/*
%{_mandir}/man5/*
%{_mandir}/man8/*

