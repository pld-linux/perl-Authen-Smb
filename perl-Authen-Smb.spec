#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Authen
%define		pnam	Smb
Summary:	Authen::Smb Perl module
Summary(cs):	Modul Authen::Smb pro Perl
Summary(da):	Perlmodul Authen::Smb
Summary(de):	Authen::Smb Perl Modul
Summary(es):	M�dulo de Perl Authen::Smb
Summary(fr):	Module Perl Authen::Smb
Summary(it):	Modulo di Perl Authen::Smb
Summary(ja):	Authen::Smb Perl �⥸�塼��
Summary(ko):	Authen::Smb �� ����
Summary(no):	Perlmodul Authen::Smb
Summary(pl):	Modu� Perla Authen::Smb
Summary(pt):	M�dulo de Perl Authen::Smb
Summary(pt_BR):	M�dulo Perl Authen::Smb
Summary(ru):	������ ��� Perl Authen::Smb
Summary(sv):	Authen::Smb Perlmodul
Summary(uk):	������ ��� Perl Authen::Smb
Summary(zh_CN):	Authen::Smb Perl ģ��
Name:		perl-Authen-Smb
Version:	0.91
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	97d8aee872160eeabd0c08a7b0985216
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::Smb is a module to authenticate against an SMB server.

%description -l pl
Authen::Smb jest modu�em umo�liwiaj�cym dost�p do serwera SMB.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

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
