#
# spec file for package python-trytond_stock
#
# Copyright (c) 2016 root.
#

Name:           trytond_stock
Version:        3.8.1
Release:        0
Url:            http://www.tryton.org/
Summary:        Tryton module for stock and inventory
License:        GPL-3.0
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/t/trytond_stock/trytond_stock-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
Requires:       python-trytond >= 3.8.0, python-trytond < 3.9, trytond_company >= 3.8, trytond_company < 3.9, trytond_currency >= 3.8, trytond_currency < 3.9, trytond_party >= 3.8, trytond_party < 3.9, trytond_product >= 3.8, trytond_product < 3.9


%description
trytond_stock
=============

The stock module of the Tryton application platform.

Installing
----------

See INSTALL

Support
-------

If you encounter any problems with Tryton, please don't hesitate to ask
questions on the Tryton bug tracker, mailing list, wiki or IRC channel:

  http://bugs.tryton.org/
  http://groups.tryton.org/
  http://wiki.tryton.org/
  irc://irc.freenode.net/tryton

License
-------

See LICENSE

Copyright
---------

See COPYRIGHT


For more information please visit the Tryton web site:

  http://www.tryton.org/

%define debug_package %{nil}

%prep
%setup -q -n trytond_stock-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
