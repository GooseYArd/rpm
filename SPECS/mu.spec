Name:           mu
Version:        0.9.1
Release:        1%{?dist}
Summary:        A collection of utilities for indexing and searching Maildirs

Group:          Applications/Communications
License:        GPL
URL:            http://code.google.com/p/mu0/
Source0:        http://mu0.googlecode.com/files/mu-0.9.1.tar.gz
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
mu is a set of tools for dealing with Maildirs and the e-mail messages in them.

%prep
%setup -q

%build
sed -i -r 's/(hardcode_into_libs)=.*$/\1=no/' configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' configure

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
* Sat Dec  4 2010 R. Andrew Bailey <bailey@akamai.com> - 0.9.1-1
- First Fedora release
