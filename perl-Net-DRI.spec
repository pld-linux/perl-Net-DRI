#
# Conditional build:
%bcond_without	tests 		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	DRI
Summary:	Net::DRI - Domain Name Registry Interface
Name:		perl-Net-DRI
Version:	0.17
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	70bc62448ad31c0a6b23c4f4690dfa76
URL:		http://www.dotandco.com/services/software/Net-DRI/index.en.xhtml
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
# FIXME
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
%doc Changes README SUPPORT TODO
%{perl_vendorlib}/Net/DRI.pm
%{perl_vendorlib}/Net/DRI
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
