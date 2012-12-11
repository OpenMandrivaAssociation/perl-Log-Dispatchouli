%define upstream_name    Log-Dispatchouli
%define upstream_version 2.005

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A simple wrapper around Log::Dispatch
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Log::Dispatch)
BuildRequires:	perl(Log::Dispatch::Array)
BuildRequires:	perl(Log::Dispatch::File)
BuildRequires:	perl(Log::Dispatch::Screen)
BuildRequires:	perl(Log::Dispatch::Syslog)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(String::Flogger)
BuildRequires:	perl(Sub::Exporter::GlobExporter)
BuildRequires:	perl(Sys::Syslog)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Try::Tiny)

BuildArch:	noarch

Requires:	perl(Log::Dispatch::Array)

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.5.0-1mdv2011.0
+ Revision: 654094
- update to new version 2.005

* Tue Feb 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.0-1
+ Revision: 634687
- update to new version 2.004

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-1mdv2011.0
+ Revision: 602096
- new version

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.102.350-1mdv2011.0
+ Revision: 572705
- update to 1.102350

* Sat Aug 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.102.220-1mdv2011.0
+ Revision: 569745
- update to 1.102220

* Sun Mar 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.712-2mdv2011.0
+ Revision: 518983
- adding missing requires:

* Sat Mar 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.712-1mdv2010.1
+ Revision: 518660
- update to 1.100712

* Thu Mar 11 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.691-1mdv2010.1
+ Revision: 518077
- update to 1.100691

* Wed Mar 10 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.681-1mdv2010.1
+ Revision: 517303
- update to 1.100681

* Tue Mar 09 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.670-1mdv2010.1
+ Revision: 517115
- update to 1.100670

* Mon Mar 08 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.660-1mdv2010.1
+ Revision: 515662
- update to 1.100660

* Fri Mar 05 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.630-1mdv2010.1
+ Revision: 514397
- update to 1.100630
- buildrequires: is not a requires of this package, but of one of the requires: of its buildreq:

* Thu Mar 04 2010 Jérôme Quelin <jquelin@mandriva.org> 1.8.0-1mdv2010.1
+ Revision: 514206
- yet another missing buildrequires:
- adding missing buildrequires:
- import perl-Log-Dispatchouli


* Thu Mar 04 2010 cpan2dist 1.008-1mdv
- initial mdv release, generated with cpan2dist
