%define	oname	shoulda

Summary:	Making tests easy on the fingers and eyes
Name:		rubygem-%{oname}
Version:	2.11.3
Release:	%mkrel 1
License:	GPLv2
Group:		Development/Ruby
URL:		http://rubygems.org/gems/%{oname}
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
Requires:	ruby
BuildArch:	noarch

%description
Making tests easy on the fingers and eyes.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

chmod g-w,g+r,o+r -R %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/bin/convert_to_should_syntax
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

