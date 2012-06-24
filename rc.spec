
Summary:	rc is a Plan 9 shell
Summary(pl):	rc jest pow�ok� z systemu Plan 9
Name:		rc
Version:	1.7.1
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://www.star.le.ac.uk/~tjg/rc/release/%{name}-%{version}.tar.gz
# Source0-md5:	7253e1c853824cf27edb2166214f0511
URL:		http://www.star.le.ac.uk/~tjg/rc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rc is a shell from Plan 9 operating system. Although it is a bit
similiar to sh(1), it's syntax is is much closer to C, even than
syntax csh.

%description -l pl
rc jest pow�ok� u�ytkownika sytemu operacyjnego Plan 9. Jej sk�adnia
jest troch� podobna do sh(1), ale jest znacznie bli�sza C, nawet w
por�wnaniu ze sk�adni� csh.

%prep
%setup  -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS EXAMPLES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
