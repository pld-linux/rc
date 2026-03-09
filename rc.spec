Summary:	rc - a Plan 9 shell
Summary(pl.UTF-8):	rc - powłoka z systemu Plan 9
Name:		rc
Version:	1.7.4
Release:	1
License:	Zlib
Group:		Applications/Shells
Source0:	https://github.com/rakitzis/rc/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3b6333d5167d3c2401969663145ec833
# from upstream commit 429f81caf8, originally from Debian (Andreas Beckmann)
Patch0:		%{name}-c23-bool.patch
URL:		https://github.com/rakitzis/rc
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rc is a shell from Plan 9 operating system. Although it is a bit
similiar to sh(1), it's syntax is is much closer to C, even than
syntax csh.

%description -l pl.UTF-8
rc jest powłoką użytkownika systemu operacyjnego Plan 9. Jej składnia
jest trochę podobna do sh(1), ale jest znacznie bliższa C, nawet w
porównaniu ze składnią csh.

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--with-readline
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS EXAMPLES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
