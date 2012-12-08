Summary:	Logs TCP, UDP, and ICMP connections to syslog
Name:		iplog
Version:	2.2.3
Release:	%mkrel 21
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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.3-20mdv2011.0
+ Revision: 665515
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.3-19mdv2011.0
+ Revision: 605978
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.3-18mdv2010.1
+ Revision: 520131
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.2.3-17mdv2010.0
+ Revision: 425362
- rebuild

* Sun Mar 08 2009 Oden Eriksson <oeriksson@mandriva.com> 2.2.3-16mdv2009.1
+ Revision: 352829
- fix #31386 (Please provide LSB tags for the iplog initscript)

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.3-15mdv2009.1
+ Revision: 316782
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.3-14mdv2009.1
+ Revision: 298261
- rebuilt against libpcap-1.0.0

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.2.3-13mdv2009.0
+ Revision: 221633
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 2.2.3-12mdv2008.1
+ Revision: 150291
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 2.2.3-11mdv2007.1
+ Revision: 145452
- use the %%mkrel macro
- bunzip the patches

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.2.3-10mdk
- Rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.2.3-9mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Wed Aug 25 2004 Pablo Saratxaga <pablo@mandrakelinux.com> 2.2.3-8mdk
- cleaned initscript i18n

