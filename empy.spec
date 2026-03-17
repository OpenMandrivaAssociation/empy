%define module empy

Name:		empy
Version:	4.2.1
Release:	1
Summary:	A python templating system for inserting Python code in template text
License:	BSD-3-Clause
Group:		Text tools
URL:		https://pypi.org/project/empy/
Source0:	https://files.pythonhosted.org/packages/source/e/%{module}/%{module}-%{version}.tar.gz

BuildSystem:  python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
%{name} is a powerful, robust and mature templating system for
inserting Python code in template text.

%{name} takes a source document, processes it, and produces output.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%doc README.md
%license LICENSE.md
%{_bindir}/em.py
%{python_sitelib}/{em,emdoc,emhelp,emlib}.py
%{python_sitelib}/%{module}-%{version}*.*-info
