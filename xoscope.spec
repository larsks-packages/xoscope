Name:		xoscope
Version:	2.1
Release:	1%{?dist}
Summary:	xoscope is a digital oscilloscope for Linux

License:	GPL
URL:		http://xoscope.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	gtk2-devel
BuildRequires:  gtkdatabox-devel
BuildRequires:   fftw3-devel

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
make %{?_smp_mflags}


%install
%make_install


%files
%doc NEWS
%doc README
%license COPYING



%changelog

