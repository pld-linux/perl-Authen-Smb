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
Summary(es):	Módulo de Perl Authen::Smb
Summary(fr):	Module Perl Authen::Smb
Summary(it):	Modulo di Perl Authen::Smb
Summary(ja):	Authen::Smb Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Authen::Smb ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Authen::Smb
Summary(pl):	Modu³ Perla Authen::Smb
Summary(pt):	Módulo de Perl Authen::Smb
Summary(pt_BR):	Módulo Perl Authen::Smb
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Authen::Smb
Summary(sv):	Authen::Smb Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Authen::Smb
Summary(zh_CN):	Authen::Smb Perl Ä£¿é
Name:		perl-Authen-Smb
Version:	0.91
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::Smb is a module to authenticate against an SMB server.

%description -l pl
Authen::Smb jest modu³em umo¿liwiaj±cym dostêp do serwera SMB.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
%{perl_sitearch}/Authen/Smb.pm
%dir %{perl_sitearch}/auto/Authen/Smb
%{perl_sitearch}/auto/Authen/Smb/autosplit.ix
%{perl_sitearch}/auto/Authen/Smb/Smb.bs
%attr(755,root,root) %{perl_sitearch}/auto/Authen/Smb/Smb.so
%{_mandir}/man3/*
