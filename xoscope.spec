Name:		xoscope
Version:	2.1
Release:	3%{?dist}
Summary:	xoscope is a digital oscilloscope for Linux

License:	GPL
URL:		http://xoscope.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gtk2-devel
BuildRequires:  gtkdatabox-devel
BuildRequires:  fftw3-devel
BuildRequires:  alsa-lib-devel

%description
Xoscope is a digital real-time oscilloscope. It graphically displays signal
amplitude as a function of time. The input is via a sound card and/or a
serial port  connected  to  a Radio  Shack  ProbeScope, Cat.  No. 22-310.
This device is also known as an osziFOX.  Either or  both input  devices
may  be  used at the same time.  Signals may be displayed, saved, recalled,
and manipulated by math functions.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags} CCDEPMODE=depmode=gcc3 LDFLAGS="-Wl,-z,relro"


%install
%make_install


%files
%doc NEWS
%doc README
%license COPYING

%{_bindir}/xoscope
%{_mandir}/man1/xoscope.1.gz
%{_datadir}/pixmaps/xoscope.png

%changelog

* Tue Jan 26 2016 Lars Kellogg-Stedman <lars@oddbit.com> - 2.1-3
- initial package
