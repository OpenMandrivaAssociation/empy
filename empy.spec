%define name	empy
%define version	3.3
%define release	 %mkrel 5

Summary:	System for embedding Python expressions and statements in template text
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Text tools
Source0:	%{name}-%{version}.tar.bz2
URL:		http://www.alcyone.com/pyos/empy/
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

