%define name	empy
%define version	3.3
%define release	 7

Summary:	System for embedding Python expressions and statements in template text
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Text tools
Source0:	%{name}-%{version}.tar.bz2
URL:		https://www.alcyone.com/pyos/empy/
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	python

%description
System for embedding Python expressions and statements in template
text.

%prep
%setup -q
perl -p -i -e 's/usr\/local\/bin\/python/usr\/bin\/python/g' em.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install em.py $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc README *.em
%{_bindir}/em.py



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3-6mdv2011.0
+ Revision: 618231
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 3.3-5mdv2010.0
+ Revision: 428623
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.3-4mdv2009.0
+ Revision: 244895
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 3.3-2mdv2008.1
+ Revision: 124628
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import empy


* Fri Jan 27 2006 Austin Acton <austin@mandriva.org> 3.3-2mdk
- Rebuild

* Thu Dec 11 2003 Austin Acton <austin@linux.ca> 3.3-1mdk
- 3.3

* Tue Sep 9 2003 Austin Acton <aacton@yorku.ca> 3.1-1mdk
- 3.1

* Sun Aug 24 2003 Austin Acton <aacton@yorku.ca> 3.0.4-1mdk
- 3.0.4

* Thu Jun 26 2003 Austin Acton <aacton@yorku.ca> 3.0.2-1mdk
- 3.0.2

* Wed Jun 11 2003 Austin Acton <aacton@yorku.ca> 3.0.1-1mdk
- 3.0.1

* Thu Jun 5 2003 Austin Acton <aacton@yokru.ca> 3.0-1mdk
- 3.0

* Thu Feb 20 2003 Austin Acton <aacton@yorku.ca> 2.3-1mdk
- initial package
