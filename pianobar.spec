%define debug_package %{nil}

Name:		pianobar
Version:	2024.12.21
Release:	1
Summary:	Native, CLI client to Pandora.com
Group:		Sound
License:	AS-IS
URL:		https://6xq.net/html/00/17.html
Source0:	https://6xq.net/static/projects/pianobar/%{name}-%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(libcurl)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires:	ffmpeg-devel
# Restricted repo
#BuildRequires:	faad2-devel
BuildRequires:	gnutls-devel

%description
 "pianobar" supports all important features pandora has:
 * Create, delete, rename stations and add more music
 * Rate and temporary ban tracks as well as move them to another station
 * "Shared stations"
 * last.fm scrobbling
 * Proxy support for non-americans
 
%prep
%autosetup -p1

%build
%make_build

%install
%make_install

%files
%doc COPYING INSTALL README.md
#{_bindir}/*
#{_mandir}/man1/*
