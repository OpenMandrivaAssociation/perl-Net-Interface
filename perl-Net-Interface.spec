%define upstream_name	 Net-Interface
%define upstream_version 1.012

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary: 	Perl extension to access network interfaces
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Net::Interface is designed to make the use of ifconfig(1) and friends
unnecessary from within Perl.  It provides methods to get at set all the
attributes of an interface, and even create new logical or physical interfaces
(if your O/S supports it).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README*
%{_mandir}/man3/*
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/Net
