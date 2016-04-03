#
# spec file for package python-trytond_sale
#
# Copyright (c) 2016 root.
#

Name:           trytond_sale
Version:        3.8.0
Release:        0
Url:            http://www.tryton.org/
Summary:        Tryton module for sale
License:        GPL-3.0
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/t/trytond_sale/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
Requires:       python-trytond >= 3.8, python-trytond < 3.9, trytond_account >= 3.8, trytond_account < 3.9, trytond_account_invoice >= 3.8, trytond_account_invoice < 3.9, trytond_account_invoice_stock >= 3.8, trytond_account_invoice_stock < 3.9, trytond_account_product >= 3.8, trytond_account_product < 3.9


%description
trytond_sale
============

The sale module of the Tryton application platform.

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
%setup -q -n trytond_sale-%{version}

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
