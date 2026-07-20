%global kf_version 6.24.0

Name:           kf6-kjobwidgets
Version: 6.24.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon for KJobs
# The following are in the LICENSES folder, but go unused: LGPL-3.0-only, LicenseRef-KDE-Accepted-LGPL
License:        CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/kjobwidgets

Source0: %{name}-%{version}.tar.bz2

BuildRequires: kf6-extra-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
#BuildRequires:  libX11-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-knotifications-devel
BuildRequires:  kf6-kwidgetsaddons-devel
#BuildRequires:  python3-devel
#BuildRequires:  python3-build
#BuildRequires:  python3-setuptools
#BuildRequires:  python3-wheel
#BuildRequires:  clang-devel

BuildRequires:  pkgconfig(xkbcommon)
#Requires:       kf6-filesystem

%description
%{summary}.

#%%package        -n python3-%{name}
#Summary:        Qt for Python bindings for %{name}
#%%description    -n python3-%{name}
#The package contains the pyside6 bindings library for %%{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       kf6-kcoreaddons-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6 \
  -DWITH_X11:BOOL=OFF \
  -DBUILD_PYTHON_BINDINGS:BOOL=OFF \
  %{nil}
%cmake_build

%install
%cmake_install

%find_lang_kf6 kjobwidgets6_qt


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kjobwidgets6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/kjobwidgets.*
%{_kf6_libdir}/libKF6JobWidgets.so.*

%files devel
%{_kf6_includedir}/KJobWidgets/
%{_kf6_libdir}/libKF6JobWidgets.so
%{_kf6_libdir}/cmake/KF6JobWidgets/
%{_kf6_datadir}/dbus-1/interfaces/*.xml

