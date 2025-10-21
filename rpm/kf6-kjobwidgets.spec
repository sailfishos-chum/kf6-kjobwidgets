%global kf6_version 6.18.0
%global qt_version 6.8.3

Name:       kf6-kjobwidgets
Version:    6.18.0
Release:    1%{?dist}
Summary:    KDE Frameworks 6 Tier 2 addon for KJobs

License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/kjobwidgets
Source0: %{name}-%{version}.tar.bz2

%{?opt_kf6_default_filter}

BuildRequires: kf6-extra-cmake-modules
BuildRequires: kf6-kcoreaddons-devel >= %{kf6_version}
BuildRequires: kf6-kwidgetsaddons-devel >= %{kf6_version}
BuildRequires: kf6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{qt_version}
BuildRequires: qt6-qttools-devel

%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
Requires: qt6-qtbase-gui
Requires: kf6-kcoreaddons >= %{kf6_version}
Requires: kf6-kwidgetsaddons >= %{kf6_version}

%description
KDE Frameworks 6 Tier 2 addon for KJobs

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel
Requires: kf6-kcoreaddons-devel >= %{version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang_kf6 kjobwidgets6_qt


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kjobwidgets6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_opt_kf6_datadir}/qlogging-categories6/kjobwidgets.*
%{_opt_kf6_libdir}/libKF6JobWidgets.so.*

%files devel

%{_opt_kf6_includedir}/KF6/KJobWidgets/
%{_opt_kf6_libdir}/libKF6JobWidgets.so
%{_opt_kf6_libdir}/cmake/KF6JobWidgets/
%{_opt_kf6_datadir}/dbus-1/interfaces/*.xml
%{_opt_kf6_archdatadir}/mkspecs/modules/qt_KJobWidgets.pri
