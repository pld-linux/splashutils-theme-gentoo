
%define		theme	gentoo

Summary:	Splashutils - gentoo theme
Summary(pl):	Splashutils - motyw gentoo
Name:		splashutils-theme-%{theme}
Version:	1
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://dev.gentoo.org/~spock/projects/gensplash/current/fbsplash-theme-gentoo.tar.bz2
# Source0-md5:	ea206196d3cee32007ae1e8eab5a0b10
Requires:	splashutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gentoo theme for splashutils.

%description -l pl
Motyw gentoo do splashutils.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

THEME_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/splash/%{theme}

install -d $THEME_DIR/images
install %{theme}/*.cfg $THEME_DIR
install %{theme}/images/* $THEME_DIR/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/splash/%{theme}
