Name:           global
Version:        5.9.2
Release:	1%{?dist}

Summary:        Source code tag system

Group:          Development/Tools
License:        GPLv2+ and BSD
URL:            http://www.gnu.org/software/global
Source:         http://tamacom.com/global/global-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch0: global-5.9.2-localstatedir.patch
%description
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

%prep
%setup -q

%patch0 -p1

%build
automake
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -fr $RPM_BUILD_ROOT%{_datadir}/emacs
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info \
    %{_infodir}/dir 2>/dev/null || :
fi

%files
%defattr(-,root,root,-)
%doc README THANKS LICENSE AUTHORS COPYING FAQ globash/globash.rc gtags.el
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man*/*
%{_datadir}/gtags/*
%{_libdir}/gtags/*
%{_localstatedir}/gtags/*

%changelog
* Sat Dec  4 2010 R. Andrew Bailey <gemi@bluewin.ch> - 5.9.2-1
- new release 5.9.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Gerard Milmeister <gemi@bluewin.ch> - 5.7.5-1
- new release 5.7.5

* Fri Nov 21 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.7.3-1
- new release 5.7.3

* Sun Oct 19 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.7.2-1
- new release 5.7.2

* Sat Aug  2 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.7.1-1
- new release 5.7.1

* Mon Jul 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.4-3
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.4-2
- Autorebuild for GCC 4.3

* Sat Feb 24 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.4-1
- new version 5.4

* Sat Dec  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.3-1
- new version 5.3

* Wed Aug 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.2-1
- new version 5.2

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.0-2
- Rebuild for FE6

* Sun Apr 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.0-1
- new version 5.0

* Fri Feb 17 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.8.7-3
- Rebuild for Fedora Extras 5

* Wed Oct  5 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.7-2
- Remove dir in /usr/share/info

* Sat Oct  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.7-1
- New Version 4.8.7

* Tue Jul  5 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.6-1
- New Version 4.8.6

* Wed May 25 2005 Jeremy Katz <katzj@redhat.com> - 4.8.4-4
- fix build with gcc4 (#156212)

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 4.8.4-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Mar  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.4-1
- New Version 4.8.4

* Mon Dec 27 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.8.2-0.fdr.1
- New Version 4.8.2

* Sat Oct 23 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.8.1-0.fdr.1
- New Version 4.8.1

* Sat Jul 17 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.7.2-0.fdr.1
- New Version 4.7.2

* Fri Mar 19 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.7-0.fdr.1
- New Version 4.7

* Thu Nov 27 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:4.6.1-0.fdr.1
- First Fedora release

