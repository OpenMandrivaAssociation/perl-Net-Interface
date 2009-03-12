%define module		Net-Interface
%define name		perl-%{module}
%define version		1.010
%define release		%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary: 	Perl extension to access network interfaces
License: 	GPL or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Net::Interface is designed to make the use of ifconfig(1) and friends
unnecessary from within Perl.  It provides methods to get at set all the
attributes of an interface, and even create new logical or physical interfaces
(if your O/S supports it).

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

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

