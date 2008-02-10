#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Authen
%define		pnam	Smb
Summary:	Authen::Smb - Perl extension to authenticate against an SMB server
Summary(pl.UTF-8):	Authen::Smb - rozszerzenie Perla do uwierzytelniania za pośrednictwem serwera SMB
Name:		perl-Authen-Smb
Version:	0.91
Release:	9
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	97d8aee872160eeabd0c08a7b0985216
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::Smb Perl module allows you to authenticate a user against an
NT domain. You can specify both a primary and a backup server to use
for authentication. The NT names of the machines should be used for
specifying servers.

%description -l pl.UTF-8
Moduł Perla Authen::Smb umożliwia uwierzytelnianie użytkownika za
pośrednictwem domeny NT. Daje możliwość określenia zarówno serwera
podstawowego, jak i zapasowego, które bedą używane do
uwierzytelniania. Do określenia serwerów należy używać nazw NT. 

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Authen/Smb.pm
%dir %{perl_vendorarch}/auto/Authen/Smb
%{perl_vendorarch}/auto/Authen/Smb/autosplit.ix
%{perl_vendorarch}/auto/Authen/Smb/Smb.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Authen/Smb/Smb.so
%{_mandir}/man3/*
