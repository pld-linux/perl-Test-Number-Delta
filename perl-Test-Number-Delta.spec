#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Number-Delta
Summary:	Test::Number::Delta - Compare the difference between numbers agains given tolerance
Summary(pl.UTF-8):	Test::Number::Delta - porównywanie różnicy między liczbami do podanej tolerancji
Name:		perl-Test-Number-Delta
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	17d3eec2d5bbe012c4a797af8e75ae39
URL:		http://search.cpan.org/dist/Test-Number-Delta/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.45
BuildRequires:	perl(Test::Builder) >= 0.32
BuildRequires:	perl(Test::Builder::Tester) >= 1.02
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
At some point or another, most programmers find they need to compare
floating-point numbers for equality. The typical idiom is to test if
the absolute value of the difference of the numbers is within a
desired tolerance, usually called epsilon. This module provides such
functions (delta_within and delta_ok) for use with Test::Harness.
Usage is similar to other test functions described in Test::More.

%description -l pl.UTF-8
W pewnych sytuacjach wielu programistów potrzebuje porównania liczb
zmiennoprzecinkowych pod kątem równości. Zwykle wykonuje się to
sprawdzając czy wartość bezwzględną różnicy liczb mieści się w zadanej
tolerancji, zwykle nazywanej epsilonem. Ten moduł udostępnia takie
funkcje (delta_within i delta_ok) do używania w Test::Harness.
Składnia jest podobna do innych funkcji testowych opisanych w
Test::More.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo
%dir %{perl_vendorlib}/Test/Number
%{perl_vendorlib}/Test/Number/Delta.pm
%{_mandir}/man3/Test::Number::Delta.3pm*
