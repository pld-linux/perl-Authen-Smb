%include	/usr/lib/rpm/macros.perl
Summary:	Authen-Smb perl module
Summary(pl):	Modu³ perla Authen-Smb
Name:		perl-Authen-Smb
Version:	0.91
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Authen/Authen-Smb-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen-Smb is a module to authenticate against an SMB server.

%description -l pl
Authen-Smb jest modu³em umo¿liwiaj±cym dostêp do serwera SMB.

%prep
%setup -q -n Authen-Smb-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Authen/Smb/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Authen/Smb
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitearch}/Authen/Smb.pm

%dir %{perl_sitearch}/auto/Authen/Smb
%{perl_sitearch}/auto/Authen/Smb/.packlist
%{perl_sitearch}/auto/Authen/Smb/Smb.bs
%{perl_sitearch}/auto/Authen/Smb/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Authen/Smb/Smb.so

%{_mandir}/man3/*
