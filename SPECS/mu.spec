Name:           mu
Version:        0.10
Release:        1%{?dist}
Summary:        A collection of utilities for indexing and searching Maildirs

Group:          Applications/Communications
License:        GPL
URL:            http://code.google.com/p/mu0/
Source0:        http://mu0.googlecode.com/files/mu-0.10.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtk2-devel >= 2.0.0
BuildRequires:  xapian-core-devel >= 1.2.3 
BuildRequires:  gmime-devel >= 2.5.1
BuildRequires:  libuuid-devel >= 2.18
Requires:  	xapian-core >= 1.2.3
Requires:  	gtk2 >= 1.2.3
Requires:	gmime >= 2.5.1
Requires:	libuuid >= 2.18
%description
'mu' is a set of command-line tools for Linux/Unix that enable you to quickly find the e-mails you are looking for, assuming that you store your e-mails in Maildirs (if you don't know what 'Maildirs' are, you probably not using them).

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/applications/mug.desktop
%{_datadir}/icons/mug.svg

%changelog
* Sat Dec  4 2010 R. Andrew Bailey <bailey@akamai.com> - 0.9-1
- First Fedora release
