%define upstream_name    Log-Dispatchouli
%define upstream_version 1.008

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A simple wrapper around Log::Dispatch
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Log::Dispatch)
BuildRequires: perl(Log::Dispatch::Array)
BuildRequires: perl(Log::Dispatch::File)
BuildRequires: perl(Log::Dispatch::Screen)
BuildRequires: perl(Log::Dispatch::Syslog)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(String::Flogger)
BuildRequires: perl(Sys::Syslog)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Try::Tiny)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
