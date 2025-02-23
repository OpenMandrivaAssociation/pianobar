%define debug_package %{nil}
%define libname %mklibname pianobar
%define devname %mklibname -d pianobar

Name:		pianobar
Version:	2024.12.21
Release:	1
Summary:	Native, CLI client to Pandora.com
Group:		Sound
License:	AS-IS
URL:		https://6xq.net/pianobar/
Source0:	https://6xq.net/static/projects/pianobar/%{name}-%{version}.tar.bz2
# GH: https://github.com/PromyLOPh/pianobar/

BuildRequires: make
BuildRequires: pkgconfig(ao)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(mad)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: ffmpeg-devel
BuildRequires: pkgconfig(gnutls)
# Restricted repo
BuildRequires: pkgconfig(faad2)

Requires:	%{libname} = %{EVRD}

%description
 "pianobar" supports all important features pandora has:
 * Create, delete, rename stations and add more music
 * Rate and temporary ban tracks as well as move them to another station
 * "Shared stations"
 * last.fm scrobbling
 * Proxy support for non-americans

%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{EVRD}
Requires:	%{name} = %{EVRD} 

%description -n %{devname}
This package contains development files for %{name}.
 
%prep
%autosetup -p1

%build
%make_build DYNLINK=1 V=1

%install
%make_install DYNLINK=1 PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

# Fix shared library permissions
chmod +x %{buildroot}%{_libdir}/libpiano.so.0.0.0

# Remove static library
rm %{buildroot}%{_libdir}/libpiano.a

%files
%doc COPYING INSTALL
%{_bindir}/%{name}
%{_mandir}/man1/pianobar.1.*

%files -n %{libname}
%{_libdir}/libpiano.so.0*

%files -n %{devname}
%{_includedir}/piano.h
%{_libdir}/libpiano.so
