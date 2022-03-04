%define		kdeappsver	21.12.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		akonadi-calendar
Summary:	Akonadi Calendar
Name:		ka5-%{kaname}
Version:	21.12.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	b67c74f378f5c9e63ece42a11cd38cfb
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Test-devel >= 5.9.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcalendarcore-devel >= %{kframever}
BuildRequires:	kf5-kcodecs-devel >= %{kframever}
BuildRequires:	kf5-kcontacts-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Akonadi Calendar is a library that effectively bridges the
type-agnostic API of the Akonadi client libraries and the
domain-specific KCalCore library. It provides jobs, models and other
helpers to make working with events and calendars through Akonadi
easier.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF5AkonadiCalendar.so.5
%attr(755,root,root) %{_libdir}/libKF5AkonadiCalendar.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi_serializer_kcalcore.so
%{_datadir}/akonadi/plugins/serializer/akonadi_serializer_kcalcore.desktop
%{_datadir}/qlogging-categories5/akonadi-calendar.categories
%{_datadir}/qlogging-categories5/akonadi-calendar.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/Akonadi/Calendar
%{_includedir}/KF5/akonadi-calendar_version.h
%{_includedir}/KF5/akonadi/calendar
%{_libdir}/cmake/KF5AkonadiCalendar
%{_libdir}/libKF5AkonadiCalendar.so
%{_libdir}/qt5/mkspecs/modules/qt_AkonadiCalendar.pri
