#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Python port of linkify-it: links recognition library with full Unicode support
Summary(pl.UTF-8):	Pythonowy port linkify-it: biblioteka dozpoznająca odnośniki z pełną obsługą Unicode
Name:		python3-linkify-it-py
Version:	2.0.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/linkify-it-py/
Source0:	https://files.pythonhosted.org/packages/source/l/linkify-it-py/linkify-it-py-%{version}.tar.gz
# Source0-md5:	35863cdbd1267332b7a4df500a9ab4e4
URL:		https://pypi.org/project/linkify-it-py/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-uc-micro-py
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python port of linkify-it:
- links recognition library with full Unicode support
- focused on high quality link patterns detection in plain text

%description -l pl.UTF-8
Ten pakiet to pythonowy port projektu linkify-it:
- biblioteka rozpoznająca odnośniki z pełną obsługą Unicode
- skupia się na wysokiej jakości rozpoznawania wzorców odnośników w
  czystym tekście

%prep
%setup -q -n linkify-it-py-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/linkify_it
%{py3_sitescriptdir}/linkify_it_py-%{version}-py*.egg-info
