#
# spec file for package python-tryton
#
# Copyright (c) 2016 root.
#

Name:           python-tryton
Version:        3.8.4
Release:        0
Url:            http://www.tryton.org/
Summary:        Tryton client
License:        GPL-3.0
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/t/tryton/tryton-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
Requires:       python-dateutil, python-chardet, python-simplejson, python-GooCalendar, pygtk2, python-six >= 1.5

%description
tryton
======

The client of the Tryton application platform.
A three-tiers  high-level general purpose application platform
written in Python and use Postgresql as database engine.
It is the core base of an Open Source ERP.
It provides modularity, scalability and security.

Installing
----------

See INSTALL

Package Contents
----------------

  bin/
      Script for startup.

  doc/
      sphinx documentation in reStructuredText.
      To generate the HTML:

        python doc/build.py

  tryton/
      tryton sources.

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
%setup -q -n tryton-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/tryton
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
