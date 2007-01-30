%define _ver	%(echo %{version} |tr -d .)
Summary:	nexuiz - data files for game
Summary(pl):	nexuiz - pliki danych dla gry
Name:		nexuiz-data
Version:	2.2.3
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/nexuiz/nexuiz-%{_ver}.zip
# Source0-md5:	953fda1555fc1f9ca040bdbb797eb0fd
URL:		http://nexuiz.com/
BuildRequires:	unzip
Requires:	nexuiz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nexuiz data files

%description -l pl
Pliki danych dla nexuiz.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/nexuiz
cd $RPM_BUILD_ROOT%{_datadir}/games
%{__unzip} -qq %{SOURCE0}
mv -f Nexuiz/data nexuiz
rm -rf Nexuiz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/games/nexuiz
%{_datadir}/games/nexuiz/data
