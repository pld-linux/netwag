Summary:	GUI for netwox
Summary(pl):	Graficzny interfejs do netwoksa
Name:		netwag
Version:	5.26.0
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/Networking
Source0:	http://www.laurentconstantin.com/common/netw/netwag/download/v5/%{name}-%{version}-src.tgz
# Source0-md5:	0b3fc9a9b1ae9f3b5c90cd4be9fab4c2
Source1:	%{name}.desktop
Patch0:		%{name}-config.patch
URL:		http://www.laurentconstantin.com/en/netw/netwag/
BuildRequires:	netwib-devel >= %{version}
BuildRequires:	netwox >= %{version}
BuildRequires:	sed >= 4.0
BuildRequires:	tk
Requires:	netwox >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUI for Netwox (Netwox is a toolbox for network administrators and
network hackers).

%description -l pl
Graficzny interfejs do Netwoksa (Netwox to zestaw narzędzi dla
administratorów sieci i hackerów sieciowych).

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1

%build
cd src
./genemake
sed -i -e 's#444#644#' -e 's#555#755#g' Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_desktopdir},%{_pixmapsdir}}

%{__make} -C src install \
        INSTBIN=$RPM_BUILD_ROOT%{_bindir} \
        INSTMAN1=$RPM_BUILD_ROOT%{_mandir}/man1 \
        INSTUSERGROUP="$(id -u):$(id -g)"

install src/compil/unix/ico/ico_netw-32x32.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_desktopdir}/*
%{_pixmapsdir}/*
