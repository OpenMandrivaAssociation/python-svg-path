%define oname svg.path
%bcond_without tests

Name:		python-svg-path
Version:	6.3
Release:	1
Summary:	SVG path objects and parser
URL:		https://github.com/regebro/svg.path
License:	MIT
Group:		Development/Python
Source0:	https://github.com/regebro/svg.path/archive/%{version}/%{oname}-%{version}.tar.gz
# test failure issue repoted https://github.com/regebro/svg.path/issues/103
# fixed upstream in merged https://github.com/regebro/svg.path/pull/105
# with https://github.com/regebro/svg.path/pull/105/commits/a17ed35e490a99a7dfab9833f6f3be86f004f699
Patch0:		https://github.com/regebro/svg.path/pull/105/commits/a17ed35e490a99a7dfab9833f6f3be86f004f699.patch

BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pillow)
%endif

%description
SVG path objects and parser.

svg.path is a collection of objects that implement the different path
commands in SVG, and a parser for SVG path definitions.

%prep
%autosetup -n %{oname}-%{version} -p1

# remove prebuilt egg-info
rm -rf src/%{oname}.egg-info

%build
%py_build

%install
%py_install

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
%{__python} -m pytest -v
%endif

%files
%{py_sitedir}/svg
%{py_sitedir}/%{oname}-%{version}*.*-info
%doc README.rst
%doc CHANGES.txt
%license LICENSE.txt
