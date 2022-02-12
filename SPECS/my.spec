Name: my
Version: 1.0.0
Release: 0
Summary: An RPM to see if building works.
License: Apache
Group: Productivity
URL: https://buluma.github.io/
Source: https://github.com/buluma/rpm_build/blob/master/SOURCES/my-1.0.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: gcc make

%description
Build a mock RPM.

%prep
%setup -q

%build
make

%install
make PREFIX=/usr DESTDIR=%{?buildroot} install

%files
%defattr(-,root,root,-)
%{_bindir}/my

%changelog
