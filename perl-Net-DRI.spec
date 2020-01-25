#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Net
%define		pnam	DRI
Summary:	Net::DRI - Domain Name Registry Interface
Summary(pl.UTF-8):	Net::DRI - interfejs do Domain Name Registry
Name:		perl-Net-DRI
Version:	0.95
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	11690b74f3be516d43bfc6fca761f0b1
URL:		http://www.dotandco.com/services/software/Net-DRI/index.en.xhtml
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Class-Accessor-Chained
BuildRequires:	perl-DateTime
BuildRequires:	perl-DateTime-Format-ISO8601 >= 0.06
BuildRequires:	perl-DateTime-Format-Strptime
BuildRequires:	perl-DateTime-TimeZone
BuildRequires:	perl-Email-Valid
BuildRequires:	perl-IO-Socket-SSL >= 0.90
BuildRequires:	perl-XML-LibXML
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::DRI is a collection of object oriented Perl modules that provides
an abstract and uniform interface to connect to domain name providers,
either registries, registrars or an entity at another level. Thus
Net::DRI can be used by a registrar to establish connections with
various registries, or by a reseller that needs to connect with its
registrar, or by an end client that needs to connect with its
provider, be it a registrar or not, without being forced to use the
specific interface available from the provider!

%description -l pl.UTF-8
Net::DRI to zbiór obiektowo zorientowanych modułów Perla
udostępniających abstrakcyjny i jednolity interfejs do łączenia się z
dostawcami nazw domen - rejestrami (registries), prowadzącymi rejestry
(registrars) lub jednostkami na innym poziomie. W ten sposób Net::DRI
może być używany przez prowadzącego rejestr do nawiązywania połączeń z
różnymi rejestrami lub przez sprzedawcę potrzebującego połączyć się z
prowadzącym jego rejestr, lub przez klienta potrzebującego połączyć
się ze swoim dostawcą - który może być prowadzącym rejestr lub nie -
bez potrzeby używania konkretnego interfejsu dostępnego u dostawcy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install eg/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Net/DRI.pm
%{perl_vendorlib}/Net/DRI
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
