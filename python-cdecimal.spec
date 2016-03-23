#
# spec file for package python-cdecimal
#
# Copyright (c) 2016 root.
#

Name:           python-cdecimal
Version:        2.3
Release:        0
Url:            http://www.bytereef.org/mpdecimal/index.html
Summary:        Fast drop-in replacement for decimal.py
License:        BSD License
Group:          Development/Languages/Python
Source:         http://www.bytereef.org/software/mpdecimal/releases/cdecimal-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel, gcc

%description
**Please note**: cdecimal has been integrated into CPython 3.3, where it
supersedes the pure Python version: *import decimal* will automatically
import the C version. Performance has been improved further, so the
cdecimal version shipped with CPython 3.3 is significantly faster for
numerical workload than cdecimal-2.3. If you need maximum decimal
computing performance, you should solely use that Python version.

cdecimal is a fast drop-in replacement for the decimal module in Python's
standard library for Python versions 2.5 up to 3.2. It provides a complete implementation of Mike Cowlishaw/IBM's General Decimal Arithmetic Specification.

Since cdecimal is compatible with decimal, the official documentation is
valid: http://docs.python.org/library/decimal.html

For the few remaining differences, see:
http://www.bytereef.org/mpdecimal/doc/cdecimal/index.html


**NOTE: The safest way to get cdecimal is to use the download URL
and verify the sha256sum:**

d737cbe43ed1f6ad9874fb86c3db1e9bbe20c0c750868fde5be3f379ade83d8b  cdecimal-2.3.tar.gz

Do not necessarily trust the above checksum. Use a search engine to ensure
that it is identical to the one in the release announcement of cdecimal-2.3.


**NOTE: cdecimal is an external package, so the download count below
is incorrect.**

%prep
%setup -q -n cdecimal-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitearch}/*

%changelog
