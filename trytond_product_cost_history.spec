#
# spec file for package python-trytond_product_cost_history
#
# Copyright (c) 2016 root.
#

Name:           python-trytond_product_cost_history
Version:        3.8.0
Release:        0
Url:            http://www.tryton.org/
Summary:        Tryton module to historize product cost
License:        GPL-3.0
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/t/trytond_product_cost_history/trytond_product_cost_history-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel

%description
trytond_product_cost_history
============================

The product_cost_history module of the Tryton application platform.

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
%setup -q -n trytond_product_cost_history-%{version}

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
