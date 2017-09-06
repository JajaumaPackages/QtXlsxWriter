Name:           QtXlsxWriter
Version:        0.5
Release:        1%{?dist}
Summary:        .xlsx file reader and writer for Qt5

License:        MIT
URL:            https://github.com/rbulygin/QtXlsxWriter
Source0:        https://github.com/rbulygin/QtXlsxWriter/archive/v%{version}.tar.gz

BuildRequires:  cmake >= 3.2
BuildRequires:  qt5-qtbase-devel

%description
The Qt Xlsx Module provides a set of classes to read and write Excel files. It
doesn't require Microsoft Excel and can be used in any platform that Qt5
supported. The library can be used to

* Generate a new .xlsx file from scratch
* Extract data from an existing .xlsx file
* Edit an existing .xlsx file


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
mkdir build
pushd build
%cmake ..
make %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
pushd build
%make_install
popd


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/QtXlsxWriter/QtXlsxWriterConfig.cmake


%changelog
* Wed Sep 06 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.5-1
- Update to latest release from rbulygin/QtXlsxWriter
- Drop upstreamed pacthes

* Sat Jun 24 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.2.2-1.git20170624.6895d8b
- Initial release
