#
# spec file for package python-proteus
#
# Copyright (c) 2016 root.
#

Name:           python-proteus
Version:        3.8.1
Release:        0
Url:            http://www.tryton.org/
Summary:        Library to access Tryton server as a client
License:        LGPL-3
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/p/proteus/proteus-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
Requires:       python-trytond >= 3.8, python-trytond < 3.9

%description
proteus
=======

A library to access Tryton's models like a client.

Installing
----------

See INSTALL

Example of usage
----------------

    >>> from proteus import config, Model, Wizard, Report

Configuration
~~~~~~~~~~~~~

Configuration to connect to a sqlite memory database using trytond as module.

    >>> config = config.set_trytond('sqlite:///:memory:')

Installing a module
~~~~~~~~~~~~~~~~~~~

Find the module, call the install button and run the install wizard.

    >>> Module = Model.get('ir.module')
    >>> party_module, = Module.find([('name', '=', 'party')])
    >>> party_module.click('install')
    >>> Wizard('ir.module.install_upgrade').execute('upgrade')

Creating a party
~~~~~~~~~~~~~~~~

First instanciate a new Party:

    >>> Party = Model.get('party.party')
    >>> party = Party()
    >>> party.id < 0
    True

Fill the fields:

    >>> party.name = 'ham'

Save the instance into the server:

    >>> party.save()
    >>> party.name
    u'ham'
    >>> party.id > 0
    True

Setting the language of the party
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The language on party is a `Many2One` relation field. So it requires to get a
`Model` instance as value.

    >>> Lang = Model.get('ir.lang')
    >>> (en,) = Lang.find([('code', '=', 'en_US')])
    >>> party.lang = en
    >>> party.save()
    >>> party.lang.code
    u'en_US'

Creating an address for the party
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Addresses are store on party with a `One2Many` field. So the new address just
needs to be appended to the list `addresses`.

    >>> address = party.addresses.new(zip='42')
    >>> party.save()
    >>> party.addresses #doctest: +ELLIPSIS
    [proteus.Model.get('party.address')(...)]

Adding category to the party
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Categories are linked to party with a `Many2Many` field.

So first create a category

    >>> Category = Model.get('party.category')
    >>> category = Category()
    >>> category.name = 'spam'
    >>> category.save()

Append it to categories of the party

    >>> party.categories.append(category)
    >>> party.save()
    >>> party.categories #doctest: +ELLIPSIS
    [proteus.Model.get('party.category')(...)]

Print party label
~~~~~~~~~~~~~~~~~

There is a label report on `Party`.

    >>> label = Report('party.label')

The report is executed with a list of records and some extra data.

    >>> type_, data, print_, name = label.execute([party], {})

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
%setup -q -n proteus-%{version}

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
