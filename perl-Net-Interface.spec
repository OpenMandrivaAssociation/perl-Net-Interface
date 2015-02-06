%define upstream_name	 Net-Interface
%define upstream_version 1.012

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.12.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.12.0-2mdv2011.0
+ Revision: 556029
- rebuild for perl 5.12

* Tue Mar 09 2010 Jérôme Quelin <jquelin@mandriva.org> 1.12.0-1mdv2010.1
+ Revision: 517119
- update to 1.012

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.011-1mdv2010.0
+ Revision: 370137
- update to new version 1.011

* Thu Mar 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.010-1mdv2009.1
+ Revision: 354159
- update to new version 1.010

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.008-1mdv2009.1
+ Revision: 347690
- update to new version 1.008

* Mon Mar 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.007-1mdv2009.1
+ Revision: 346960
- update to new version 1.007

* Sat Feb 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.004-1mdv2009.1
+ Revision: 345920
- update to new version 1.004

* Thu Feb 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.003-1mdv2009.1
+ Revision: 345104
- update to new version 1.003

* Mon Feb 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.001-1mdv2009.1
+ Revision: 344038
- new version
- drop patch, seems to be useless now

* Tue Oct 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.1
+ Revision: 295992
- new version
  drop undocumented patch 0

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
+ Revision: 277963
- update to new version 0.09

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.08-6mdv2009.0
+ Revision: 258014
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.08-5mdv2009.0
+ Revision: 246121
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.08-3mdv2008.1
+ Revision: 152219
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.08-2mdv2008.0
+ Revision: 25274
- rebuild


* Thu Apr 20 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.08-1mdk
- New release 0.08
- Change Source url

* Fri Mar 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdk
- New release 0.06
- spec cleanup

* Tue Nov 16 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.04_2.1-8mdk
- Rebuild for new perl

* Tue Nov 04 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04_2.1-7mdk
- patch 2: on Linux, just ask the number of interfaces and allocate needed space

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 0.04_2.1-6mdk
- Use %%makeinstall_std now that it works on klama

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 0.04_2.1-5mdk
- Use %%make and %%makeinstall

* Fri Aug 01 2003 Ben Reser <ben@reser.org> 0.04_2.1-4mdk
- macroification, specifically for the perl stuff so it will build across
  changing perl versions.
- Fix ownership of man3 dir

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04_2.1-3mdk
- rebuild for new auto{prov,req}

* Wed May 07 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.04_2.1-2mdk
- use vendor_perl
- from Peter Chen <petechen@netilla.com> :
	- 0.04_2.1
	- Added a patch to provide an additional method, irq().  This patch
  	has been submitted to the author.

