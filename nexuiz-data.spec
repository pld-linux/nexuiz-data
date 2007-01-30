%define _ver	%(echo %{version} |tr -d .)
Summary:	nexuiz - data files for game
Summary(pl):	nexuiz - pliki danych dla gry
Name:		nexuiz-data
Version:	2.2.3
Release:	1
License:	GPL v2
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
%setup -q -n Nexuiz

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/%{name}/data
cp -rf data $RPM_BUILD_ROOT%{_datadir}/games/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/%{name}
