Summary:	nexuiz - data files for game
Summary(pl):	nexuiz - pliki danych dla gry
Name:		nexuiz-data
Version:	2.2.3
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/nexuiz/nexuiz-223.zip
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
install data $RPM_BUILD_ROOT%{_datadir}/games/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/%{name}
