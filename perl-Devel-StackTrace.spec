#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	StackTrace
Summary:	Devel::StackTrace - Stack trace and stack trace frame objects
Summary(pl):	Devel::StackTrace - ¶ledzenie stosu i ramek obiektów
Name:		perl-%{pdir}-%{pnam}
Version:	1.11
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a5d2088a531ceeec82b989c742f9382e
BuildRequires:	perl-Module-Build
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.46}
BuildRequires:	perl-devel >= 1:5.8.0
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
%{__perl} Build.PL \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE Changes README
%{perl_vendorlib}/Devel/StackTrace.pm
%{_mandir}/man3/*
