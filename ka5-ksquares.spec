#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		ksquares
Summary:	ksquares
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ce889ec090251b63a3cc614eb5ac884e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSquares is a game modeled after the well known pen and paper based
game of Dots and Boxes. Each player takes it in turns to draw a line
between two adjacent dots on the board. The objective is to complete
more squares than your opponents.

%description -l pl.UTF-8
KSquares jest grą wzorowaną na dobrze znanej grze rozgrywanej na
kartce w kropki i kwadraty. Każdy z graczy przy swojej kolejce rysuje
linię między dwoma sąsiadującymi kropkami na planszy. Celem gry jest
zakończyć więcej kwadratów niż rywal.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksquares
%{_desktopdir}/org.kde.ksquares.desktop
%{_datadir}/config.kcfg/ksquares.kcfg
%{_iconsdir}/hicolor/128x128/apps/ksquares.png
%{_iconsdir}/hicolor/16x16/apps/ksquares.png
%{_iconsdir}/hicolor/22x22/apps/ksquares.png
%{_iconsdir}/hicolor/32x32/apps/ksquares.png
%{_iconsdir}/hicolor/48x48/apps/ksquares.png
%{_iconsdir}/hicolor/64x64/apps/ksquares.png
%{_datadir}/metainfo/org.kde.ksquares.appdata.xml
