# Run tests in check section
%bcond_without check

%global goipath         github.com/VividCortex/godaemon
%global commit          3d9f6e0b234fe7d17448b345b2e14ac05814a758

%global common_description %{expand:
Daemonize Go applications with exec() instead of fork().

You can't daemonize the usual way in Go. Daemonizing is a Unix concept that 
requires some specific things you can't do easily in Go. But you can still 
accomplish the same goals if you don't mind that your program will start 
copies of itself several times, as opposed to using fork() the way many 
programmers are accustomed to doing.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Daemonize Go applications deviously
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git3d9f6e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1.20180508git3d9f6e0
- First package for Fedora

