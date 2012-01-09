Name:		pianobar
Version:	2011.12.11
Release:	1
Summary:	Pianobar is a native, CLI client to Pandora.com

Group:		Sound
License:	AS-IS
URL:		http://6xq.net/html/00/17.html
Source0:	http://6xq.net/static/projects/pianobar/pianobar-%{version}.tar.bz2

BuildRequires:	make libao-devel libxml2-devel faad2 libmad-devel
BuildRequires:	libfaad2-devel gnutls-devel

%description
 "pianobar" supports all important features pandora has:
 * Create, delete, rename stations and add more music
 * Rate and temporary ban tracks as well as move them to another station
 * "Shared stations"
 * last.fm scrobbling
 * Proxy support for non-americans
%prep
%setup -q

%build
gmake
gmake VERBOSE=1 %{?_smp_mflags}

%install
gmake install PREFIX=usr DESTDIR=$RPM_BUILD_ROOT

%check

%files
%doc COPYING INSTALL README
%{_bindir}/*
%{_mandir}/man1/*
