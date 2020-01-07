#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Carp-Always
Version  : 0.16
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Carp-Always-0.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Carp-Always-0.16.tar.gz
Summary  : 'Warns and dies noisily with stack backtraces'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Carp-Always-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Spiffy)
BuildRequires : perl(Test::Base)

%description
Carp-Always version 0.16
========================
Carp::Always can be used to make a script complain loudly
with stack traces when warn()ing or die()ing.

%package dev
Summary: dev components for the perl-Carp-Always package.
Group: Development
Provides: perl-Carp-Always-devel = %{version}-%{release}
Requires: perl-Carp-Always = %{version}-%{release}

%description dev
dev components for the perl-Carp-Always package.


%package perl
Summary: perl components for the perl-Carp-Always package.
Group: Default
Requires: perl-Carp-Always = %{version}-%{release}

%description perl
perl components for the perl-Carp-Always package.


%prep
%setup -q -n Carp-Always-0.16
cd %{_builddir}/Carp-Always-0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Carp::Always.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/Carp/Always.pm
