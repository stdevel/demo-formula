#
# spec file for package sap-compliance-formula
#
#

# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           demo-formula
Version:        1.0
Release:        1%{?dist}
Summary:        Demo Formula for SUSE Manager
Url:            https://github.com/stdevel/salt-tdd-example
Requires:       salt-master
License:        GPL-3.0
Group:          System/Management
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

# This would be better with a macro that just strips "-formula" from {name}
%define fname demo

%description
Salt Formula for SUSE Manager. Configures demo content.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/share/susemanager/formulas/states/%{fname}
mkdir -p %{buildroot}/usr/share/susemanager/formulas/metadata/%{fname}
cp -R demo/* %{buildroot}/usr/share/susemanager/formulas/states/%{fname}
cp -R metadata/* %{buildroot}/usr/share/susemanager/formulas/metadata/%{fname}

%files
%defattr(-,root,root,-)
%doc COPYING README.md
/usr/share/susemanager

%changelog
*Tue May 11 10:45:00 CEST 2020 - info@cstan.io 1.0-1
- initial version
