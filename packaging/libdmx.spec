Summary: X.Org X11 DMX runtime library
Name: libdmx
Version: 1.1.2
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(xorg-macros)
BuildRequires: pkgconfig(dmxproto)
BuildRequires: pkgconfig(xext)

%description
The X.Org X11 DMX (Distributed Multihead X) runtime library.

%package devel
Summary: X.Org X11 DMX development files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The X.Org X11 DMX (Distributed Multihead X) development files.

%prep
%setup -q

%build
%reconfigure --disable-static \
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
#%doc COPYING ChangeLog
%{_libdir}/libdmx.so.1
%{_libdir}/libdmx.so.1.0.0

%files devel
%defattr(-,root,root,-)
%{_libdir}/libdmx.so
%{_libdir}/pkgconfig/dmx.pc
#%{_mandir}/man3/*.3*
%{_includedir}/X11/extensions/dmxext.h
