#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Authen
%define		pnam	Smb
Summary:	Authen::Smb - Perl extension to authenticate against an SMB server
Summary(pl):	Authen::Smb - rozszerzenie Perla do uwierzytelniania za po¶rednictwem serwera SMB
Name:		perl-Authen-Smb
Version:	0.91
Release:	7
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	97d8aee872160eeabd0c08a7b0985216
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::Smb Perl module allows you to authenticate a user against an
NT domain.  You can specify both a primary and a backup server to use
for authentication.  The NT names of the machines should be used for
specifying servers.

%description -l pl
Modu³ Perla Authen::Smb umo¿liwia uwierzytelnianie u¿ytkownika za
po¶rednictwem domeny NT. Daje mo¿liwo¶æ okre¶lenia zarówno serwera
podstawowego, jak i zapasowego, które bed± u¿ywane do
uwierzytelniania. Do okre¶lenia serwerów nale¿y u¿ywaæ nazw NT. 

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
