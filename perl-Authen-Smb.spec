%define	pdir	Authen
%define	pnam	Smb
%include	/usr/lib/rpm/macros.perl
Summary:	Authen-Smb perl module
Summary(pl):	Modu� perla Authen-Smb
Name:		perl-Authen-Smb
Version:	0.91
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen-Smb is a module to authenticate against an SMB server.

%description -l pl
Authen-Smb jest modu�em umo�liwiaj�cym dost�p do serwera SMB.

%prep
%setup -q -n Authen-Smb-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Authen/Smb.pm
%dir %{perl_sitearch}/auto/Authen/Smb
%attr(755,root,root) %{perl_sitearch}/auto/Authen/Smb/Smb.so
%{_mandir}/man3/*
