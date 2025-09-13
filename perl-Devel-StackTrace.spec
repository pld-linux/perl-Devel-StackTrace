#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Devel
%define		pnam	StackTrace
Summary:	Devel::StackTrace - stack trace and stack trace frame objects
Summary(pl.UTF-8):	Devel::StackTrace - śledzenie stosu i ramek obiektów
Name:		perl-Devel-StackTrace
Version:	2.05
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b8ca19bb4c76e98a04373618db9c7c3c
URL:		https://metacpan.org/dist/Devel-StackTrace
BuildRequires:	perl-ExtUtils-MakeMaker
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.96}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Devel::StackTrace module contains two classes, Devel::StackTrace
and Devel::StackTraceFrame. The goal of this object is to encapsulate
the information that can found through using the caller() function, as
well as providing a simple interface to this data.

%description -l pl.UTF-8
Moduł Devel::StackTrace zawiera dwie klasy: Devel::StackTrace i
Devel::StackTraceFrame. Zadaniem tego obiektu jest obudowanie
znalezionej przy użyciu funkcji caller() informacji, oraz
udostępnienie prostego interfejsu do tych danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README.md
%{perl_vendorlib}/Devel/StackTrace.pm
%{perl_vendorlib}/Devel/StackTrace
%{_mandir}/man3/Devel::StackTrace*.3pm*
