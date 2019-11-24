Summary:	Vertical Ancillary Data (VANC) tools
Summary(pl.UTF-8):	Narzędzia do danych VANC (Vertical Ancillary Data)
Name:		klvanc-tools
Version:	1.0
%define	rel	2
%define	snap	20190911
%define	gitref	887b50247134b077c903ef813527ea33fa13b6c1
Release:	0.%{snap}.%{rel}
License:	LGPL v2.1
Group:		Applications/Multimedia
Source0:	https://github.com/stoth68000/klvanc-tools/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	af886529a958f20fafc537bf78f17cf6
Patch0:		%{name}-am.patch
Patch1:		%{name}-sh.patch
URL:		https://github.com/stoth68000/klvanc-tools
BuildRequires:	libklvanc-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
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
%setup -q -n %{name}-%{gitref}
%patch0 -p1
%patch1 -p1

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
