%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		ksquares
Summary:	ksquares
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	f0618bc936532e402e11488098516592
URL:		http://www.kde.org/
BuildRequires:	Qt5Core
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.30.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
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
