#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : apipkg
Version  : 2.1.0
Release  : 58
URL      : https://files.pythonhosted.org/packages/46/90/c54454c5f87ae7c754626cdc71499f6c1b3d7cdd13a4a7f27a20e05a1ad3/apipkg-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/46/90/c54454c5f87ae7c754626cdc71499f6c1b3d7cdd13a4a7f27a20e05a1ad3/apipkg-2.1.0.tar.gz
Summary  : apipkg: namespace control and lazy-import mechanism
Group    : Development/Tools
License  : MIT
Requires: apipkg-license = %{version}-%{release}
Requires: apipkg-python = %{version}-%{release}
Requires: apipkg-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Welcome to apipkg !
-------------------
With apipkg you can control the exported namespace of a Python package and
greatly reduce the number of imports for your users.
It is a `small pure Python module`_ that works on CPython 2.7 and 3.4+,
Jython and PyPy. It cooperates well with Python's ``help()`` system,
custom importers (PEP302) and common command-line completion tools.

%package license
Summary: license components for the apipkg package.
Group: Default

%description license
license components for the apipkg package.


%package python
Summary: python components for the apipkg package.
Group: Default
Requires: apipkg-python3 = %{version}-%{release}

%description python
python components for the apipkg package.


%package python3
Summary: python3 components for the apipkg package.
Group: Default
Requires: python3-core
Provides: pypi(apipkg)

%description python3
python3 components for the apipkg package.


%prep
%setup -q -n apipkg-2.1.0
cd %{_builddir}/apipkg-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635703211
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/apipkg
cp %{_builddir}/apipkg-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/apipkg/82dbfd684f7c04da81d4faa852c6317142daa3e7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/apipkg/82dbfd684f7c04da81d4faa852c6317142daa3e7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
