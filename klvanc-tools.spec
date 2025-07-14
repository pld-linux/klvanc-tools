# TODO: libklmonitoring, Nielsen decoder SDK (IMonitorSdkProcessor.h, libMonitorSdk ...)?, Blackmagic SDK
Summary:	Vertical Ancillary Data (VANC) tools
Summary(pl.UTF-8):	Narzędzia do danych VANC (Vertical Ancillary Data)
Name:		klvanc-tools
Version:	1.2.0
Release:	1
License:	LGPL v2.1
Group:		Applications/Multimedia
#Source0Download: https://github.com/stoth68000/klvanc-tools/tags
Source0:	https://github.com/stoth68000/klvanc-tools/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	62efa94c9f70076607da572cf2d42630
Patch0:		%{name}-am.patch
Patch1:		%{name}-sh.patch
URL:		https://github.com/stoth68000/klvanc-tools
BuildRequires:	libklvanc-devel >= 1.2.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel >= 1.2.9
Requires:	libklvanc >= 1.2.0
Requires:	zlib >= 1.2.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libklvanc is a library which can be used for parsing/generation of
Vertical Ancillary Data (VANC) commonly found in the Serial Digital
Interface (SDI) wire protocol.

This package contains tools built against the library.

%description -l pl.UTF-8
Libklvanc to biblioteka służąca do analizy i generowania danych VANC
(Vertical Ancillary Data), używanych generalnbie w protokole Serial
Digital Interface (SDI).

Ten pakiet zawiera narzędzia zbudowane w oparciu o bibliotekę.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/klvanc_capture
%attr(755,root,root) %{_bindir}/klvanc_transmitter
