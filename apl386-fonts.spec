%define commit 6332c9dbb588946a0e8c9d7984dd0c003eeea266

Name:           apl386-fonts
Version:        20220307
Release:        %{autorelease}
Summary:        APL385 Unicode font evolved

License:        Unlicense
URL:            https://abrudz.github.io/APL386/
Source0:        https://github.com/abrudz/APL386/archive/%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib

Requires:       fontpackages-filesystem

%description
APL font based on Adrian Smith's APL385 font with a fun, whimsical look, inspired by Comic Sans Serif.

%prep
%setup -q -n APL386-%{commit}


%build


%install
install -Dm 0644 APL386.ttf %{buildroot}%{_fontdir}/APL386.ttf


%files
%{_fontdir}/APL386.ttf

%license LICENSE
%doc README.md


%changelog
* Sat Aug 26 2023 buffet <niclas@countingsort.com>
- Init at 20220307
