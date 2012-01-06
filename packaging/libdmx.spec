
Name:       libdmx
Summary:    X.Org X11 libdmx runtime library
Version:    1.1.1
Release:    1
Group:      System/Libraries
License:    MIT/X11
URL:        http://www.x.org
Source0:    ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(dmxproto)
BuildRequires:  pkgconfig


%description
libdmx runtime library


%package devel
Summary:    X.Org X11 libdmx development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
libdmx development package


%prep
%setup -q -n %{name}-%{version}


%build

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
%doc COPYING README ChangeLog
%{_libdir}/libdmx.so.1
%{_libdir}/libdmx.so.1.0.0


%files devel
%defattr(-,root,root,-)
%{_libdir}/libdmx.so
%{_libdir}/pkgconfig/dmx.pc
%{_mandir}/man3/*.3*
%{_includedir}/X11/extensions/dmxext.h

