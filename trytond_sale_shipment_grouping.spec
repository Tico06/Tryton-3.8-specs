#
# spec file for package python-trytond_sale_shipment_grouping
#
# Copyright (c) 2016 root.
#

Name:           python-trytond_sale_shipment_grouping
Version:        3.8.0
Release:        0
Url:            http://www.tryton.org/
Summary:        Tryton module to group sale stock moves
License:        GPL-3.0
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/t/trytond_sale_shipment_grouping/trytond_sale_shipment_grouping-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel

%description
sale_shipment_grouping
======================

The sale_shipment_grouping module of the Tryton application platform.

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

%prep
%setup -q -n trytond_sale_shipment_grouping-%{version}

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
