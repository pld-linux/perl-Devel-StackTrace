#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	StackTrace
Summary:	Devel::StackTrace - Stack trace and stack trace frame objects
Summary(pl):	Devel::StackTrace - ¶ledzenie stosu i ramek obiektów
Name:		perl-%{pdir}-%{pnam}
Version:	1.04
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	43066b259f702369f0bfbc0e6363566b
BuildRequires:	perl-devel >= 5.005
%if %{!?_without_tests:1}0
BuildRequires:	perl(fields)
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Devel::StackTrace module contains two classes, Devel::StackTrace
and Devel::StackTraceFrame.  The goal of this object is to encapsulate
the information that can found through using the caller() function,
as well as providing a simple interface to this data.

%description -l pl
Modu³ Devel::StackTrace zawiera dwie klasy: Devel::StackTrace
i Devel::StackTraceFrame.  Zadaniem tego obiektu jest obudowanie
znalezionej przy u¿yciu funkcji caller() informacji, oraz udostêpnienie
prostego interfejsu do tych danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE Changes README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
