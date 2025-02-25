# Generated from shoulda-2.11.3.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	shoulda

Summary:	Making tests easy on the fingers and eyes
Name:		rubygem-%{rbname}

Version:	2.11.3
Release:	3
Group:		Development/Ruby
License:	GPLv2
URL:		https://thoughtbot.com/community/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Making tests easy on the fingers and eyes.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(rails|test)/'

%install
%gem_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/convert_to_should_syntax
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/convert_to_should_syntax
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/rails
%{ruby_gemdir}/gems/%{rbname}-%{version}/rails/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*


%changelog
* Tue Mar 15 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.11.3-2
+ Revision: 645141
- regenerate spec with gem2rpm5

* Fri Sep 17 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.11.3-1mdv2011.0
+ Revision: 579207
- import rubygem-shoulda


