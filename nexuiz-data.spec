%define _ver	%(echo %{version} | tr -d .)
Summary:	nexuiz - data files for game
Summary(pl.UTF-8):	nexuiz - pliki danych dla gry
Name:		nexuiz-data
Version:	2.4.2
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/nexuiz/nexuiz-%{_ver}.zip
# Source0-md5:	2ea51368774ca603fd56faebfeac74d7
URL:		http://nexuiz.com/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nexuiz data files.

%description -l pl.UTF-8
Pliki danych dla gry nexuiz.

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
