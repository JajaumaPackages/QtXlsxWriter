%global commit  6895d8b
%global vermagic 0.3.0
%global snapshot .git20170624.%{commit}

Name:           QtXlsxWriter
Version:        %{vermagic}
Release:        1%{snapshot}%{?dist}
Summary:        .xlsx file reader and writer for Qt5

License:        MIT
URL:            https://github.com/VSRonin/QtXlsxWriter

# git clone https://github.com/VSRonin/QtXlsxWriter
# cd QtXlsxWriter
# git archive --prefix=QtXlsxWriter/ master | bzip2 >../QtXlsxWriter.tar.bz2
Source0:        QtXlsxWriter.tar.bz2
Patch0:         QtXlsxWriter-LIB_SUFFIX-support.patch
Patch1:         QtXlsxWriter-SOVERSION-support.patch

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
%setup -q -n QtXlsxWriter
%patch0 -p1
%patch1 -p1


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
* Sat Jun 24 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.2.2-1.git20170624.6895d8b
- Initial release
