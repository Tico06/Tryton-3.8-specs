#
# spec file for package python-GooCalendar
#
# Copyright (c) 2016 root.
#

Name:           python-GooCalendar
Version:        0.2
Release:        0
Url:            http://code.google.com/p/goocalendar/
Summary:        A calendar widget for GTK using PyGoocanvas
License:        GPL-2.0
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/G/GooCalendar/GooCalendar-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel

%description
GooCalendar
===========

A calendar widget for GTK using PyGoocanvas

Nutshell
--------

Example usage::

    >>> import datetime
    >>> import goocalendar
    >>> event_store = goocalendar.EventStore()
    >>> calendar = goocalendar.Calendar(event_store)
    >>> event = goocalendar.Event('Birthday',
    ...     datetime.date.today(),
    ...     bg_color='lightgreen')
    >>> event_store.add(event)

%define debug_package %{nil}

%prep
%setup -q -n GooCalendar-%{version}

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
