#
# spec file for package python-trytond
#
# Copyright (c) 2016 root.
#

Name:           python-trytond
Version:        3.8.3
Release:        0
Url:            http://www.tryton.org/
Summary:        Tryton server
License:        GPL-3.0
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/t/trytond/trytond-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
#Requires:       python-sqlite3dbm
Requires:       python-lxml >= 2.0, python-relatorio >= 0.2.0, python-genshi, python-dateutil, python-polib, python2-sql >= 0.4, py-bcrypt, python-Levenshtein, pywebdav >= 0.9.8, python-simplejson, pydot, python-simplejson, python-cdecimal

%description
trytond
=======

The server of the Tryton application platform.
A three-tiers  high-level general purpose application platform
written in Python and use Postgresql as main database engine.
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
      To generate the HTML (trytond module must be in PYTHONPATH):

        sphinx-build doc/ doc/

  etc/
      Configuration files.

  trytond/
      trytond sources.

Database Backends
-----------------

Tryton is mainly developed for PostgreSQL (8.2 or later) but there are other 
backends available. Here are some warnings about using other backends:

  * MySQL

    * The lock implementation of MySQL requires that Tryton locks all tables.

    * There are problems with floating-point comparisons.
      See: http://dev.mysql.com/doc/refman/5.5/en/problems-with-float.html

    * Tryton uses a VARCHAR(255) for Char, Selection and Reference fields.

    * MySQL can not create indexes containing text or blob fields.

    * Timestamp has a precision of second which is used for optimistic lock.

    * Tryton uses a DECIMAL(65, 30) for Decimal fields and DOUBLE(255, 30) for
      Float fields.

    * MySQL version should be 5.0 or later.

  * SQLite

    * SQLite can not alter column definitions nor create foreign keys.

    * SQL constraints are validated by Tryton instead of database.

    * Timestamp has a precision of second which is used for optimistic lock.

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
%setup -q -n trytond-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/trytond
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
