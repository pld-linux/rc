Summary:	rc is a Plan 9 shell
Summary(pl):	rc jest pow³ok± z systemu Plan 9
Name:		rc
Version:	1.6rc6
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://www.star.le.ac.uk/~tjg/rc/beta/%{name}-%{version}.tar.gz
URL:		http://www.star.le.ac.uk/~tjg/rc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rc is a shell from Plan 9 operating system. Although it is a bit
similiar to sh(1), it's syntax is is much closer to C, even than
syntax csh.

%description -l pl
rc jest pow³ok± u¿ytkownika sytemu operacyjnego Plan 9. Jej sk³adnia
jest trochê podobna do sh(1), ale jest znacznie bli¿sza C, nawet w
porównaniu ze sk³adni± csh.

%prep
%setup  -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog AUTHORS EXAMPLES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
