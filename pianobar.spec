Name:		pianobar
Version:	2012.04.24
Release:	2
Summary:	Pianobar is a native, CLI client to Pandora.com

Group:		Sound
License:	AS-IS
URL:		http://6xq.net/html/00/17.html
Source0:	http://6xq.net/static/projects/pianobar/%{name}-%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	libao-devel
BuildRequires:	libxml2-devel
BuildRequires:	faad2
BuildRequires:	libmad-devel
BuildRequires:	libfaad2-devel
BuildRequires:	gnutls-devel

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
