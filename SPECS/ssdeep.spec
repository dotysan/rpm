%define libbase fuzzy
%define libname lib%{libbase}

Name:       ssdeep
Version:    2.10
Release:    0%{?dist}

Summary:    a program for computing context triggered piecewise hashes
Group:      Applications/Engineering
License:    GPLv2

URL:        http://%{name}.sf.net
Source00:   %{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Also called fuzzy hashes, context triggered piecewise hashes (CTPH) can
match inputs that have homologies. Such inputs have sequences of
identical bytes in the same order, although bytes in between these
sequences may be different in both content and length.

Developers build with the %{libname}-devel package and deploy with the
%{libname} package.

%package -n %{libname}
Summary:    Libraries for packages built against %{name}-devel.
Group:      System Environment/Libraries

%description -n %{libname}
This package contains the library files necessary for programs that
dynamically link to %{libname} from %{name}.

%package -n %{libname}-devel
Summary:    Libraries and header files for %{name} development
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description -n %{libname}-devel
This package contains the header and library files necessary for
developing programs using %{libname} from %{name}.

%prep
%setup -q

%build
%configure
%{__make} %{?_smp_mflags}

%clean
%{__rm} -rf $RPM_BUILD_ROOT
%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog AUTHORS COPYING INSTALL README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%files -n %{libname}
%{_libdir}/%{libname}.so.*

%files -n %{libname}-devel
%{_includedir}/%{libbase}.h
%{_libdir}/%{libname}.*a
%{_libdir}/%{libname}.so

%changelog
* Sat Jan  4 2014 Curtis Doty <Curtis@GreenKey.net>
- initial rpm [2.10]
