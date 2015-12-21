%define debug_package %{nil}

Name:		pianobar
Version:	2015.11.22
Release:	1
Summary:	Native, CLI client to Pandora.com
Group:		Sound
License:	AS-IS
URL:		http://6xq.net/html/00/17.html
Source0:	http://6xq.net/static/projects/pianobar/%{name}-%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(json)
BuildRequires:	ffmpeg-devel
BuildRequires:	faad2-devel
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
gmake install PREFIX=/usr DESTDIR=%{buildroot}

%check

%files
%doc COPYING INSTALL README.md
%{_bindir}/*
%{_mandir}/man1/*
