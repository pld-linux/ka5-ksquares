%define		kdeappsver	21.04.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		ksquares
Summary:	ksquares
Name:		ka5-%{kaname}
Version:	21.04.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	c0e9f99dd33adc4bd6bd64f74865d983
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

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
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
