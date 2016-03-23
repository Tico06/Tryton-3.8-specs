# Tryton-3.8-specs
Tryton 3.8 spec files to create Fedora packages

I am currently testing tryton 3.8 and in order to reproduce my install with ease on other system I have created some SPEC file for FEDORA.

In order to compile the packages you need to install python-py2pack. To get the sources first create the following directories:
~/rpmbuild
  |-SOURCES
  \-SPECS
  
cd ~rpmbuild/SOURCES

and execute the following commands
$> py2pack fetch <package_name>

copy all the spec files in ~/rpmbuild/SPECS and execute the following
$> rpmbuild -bb <package_name.spec>

you can now install your package with:
$> yum install ~rpmbuild/RPMS/x86_64/<package_name.rpm>

Tryton could by find @ http://www.tryton.org/
