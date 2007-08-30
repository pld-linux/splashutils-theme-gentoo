
%define		theme	gentoo

Summary:	Splashutils - gentoo theme
Summary(pl.UTF-8):	Splashutils - motyw gentoo
Name:		splashutils-theme-%{theme}
Version:	2
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://dev.gentoo.org/~spock/projects/gensplash/current/fbsplash-theme-gentoo-r%{version}.tar.bz2
# Source0-md5:	76e9266c8d1dc20afeb443b664f5eb8c
Provides:	fbsplash-theme
Requires:	splashutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/splash

%description
Gentoo theme for splashutils.

%description -l pl.UTF-8
Motyw gentoo do splashutils.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

THEME_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/%{theme}

install -d $THEME_DIR/images
install %{theme}/*.cfg $THEME_DIR
install %{theme}/images/* $THEME_DIR/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/%{theme}
