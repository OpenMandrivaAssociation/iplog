Summary:	Logs TCP, UDP, and ICMP connections to syslog
Name:		iplog
Version:	2.2.3
Release:	32
License:	GPL
Group:		Monitoring
URL:		http://ojnk.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.service
Source2:	%{name}.conf
Patch0:		%{name}-2.2.3-gcc-3.3.patch
BuildRequires:	pcap-devel

%description
iplog is a TCP/IP traffic logger. Currently, it is capable of logging TCP, UDP
and ICMP traffic. Adding support for other protocols should be relatively easy.
iplog contains a built-in packet filter, allowing for logging or excluding
packets that fit a given set of criteria.

%prep

%setup -q
%autopatch -p1

%build
%configure
%make

%install
%makeinstall

install -m0644 %{SOURCE1} -D %{buildroot}%{_unitdir}/%{name}.service
install -m0644 %{SOURCE2} -D %{buildroot}/%{_sysconfdir}/%{name}.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc AUTHORS COPYING README TODO NEWS
%attr(0644,root,root) %{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sbindir}/*
%{_mandir}/man5/*
%{_mandir}/man8/*
