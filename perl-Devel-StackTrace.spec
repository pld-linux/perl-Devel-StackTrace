#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	StackTrace
Summary:	Devel::StackTrace - stack trace and stack trace frame objects
Summary(pl.UTF-8):	Devel::StackTrace - śledzenie stosu i ramek obiektów
Name:		perl-Devel-StackTrace
Version:	2.02
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bcc49dc2744d1fae906de0de3df07cca
URL:		http://search.cpan.org/dist/Devel-StackTrace/
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.96}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
