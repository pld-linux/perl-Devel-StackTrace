%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	StackTrace
Summary:	%{pdir}::%{pnam} perl module
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Name:		perl-%{pdir}-%{pnam}
Version:	0.9
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005
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
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE Changes README
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
