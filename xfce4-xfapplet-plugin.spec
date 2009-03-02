Summary:	XfApplet plugin allows to use GNOME panel applets inside the Xfce panel
Summary(pl.UTF-8):	Wtyczka XfApplet pozwalająca na używanie apletów panelu GNOME wewnątrz panelu Xfce
Name:		xfce4-xfapplet-plugin
Version:	0.1.0
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-xfapplet-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	6a06c44b18a97626f44a240ad3bc3244
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xfapplet-plugin
BuildRequires:	ORBit2-devel >= 1:2.12.5
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	gnome-panel-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XfApplet is a plugin for the Xfce panel which allows to use applets
designed for the GNOME panel. It is a tiny GNOME panel which lives
inside the Xfce panel and allows you to show the same applets that the
GNOME panel is capable of showing.

%description -l pl.UTF-8
XfApplet jest wtyczką panelu Xfce, która umożliwia używanie apletów
stworzonych dla panelu GNOME. Jest malutkim panelem GNOME żyjącym
wewnątrz panelu Xfce i umożliwiającym pokazanie takich samych apletów,
jakie jest w stanie pokazać panel GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-xfapplet-plugin
%{_datadir}/xfce4/panel-plugins/xfapplet.desktop
%{_datadir}/xfce4-xfapplet-plugin
%{_pixmapsdir}/xfapplet?.svg
