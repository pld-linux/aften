Summary:	A/52 audio encoder
#Summary(pl.UTF-8):	-
Name:		aften
Version:	0.0.8
Release:	1
License:	LGPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	fde67146879febb81af3d95a62df8840
URL:		http://aften.sourceforge.net/
BuildRequires:	cmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aften is an audio encoder which generates compressed audio streams
based on ATSC A/52 specification. This type of audio is also known
as AC-3 or Dolby® Digital and is one of the audio codecs used in
DVD-Video content. 

#%description -l pl.UTF-8

%prep
%setup -q

%build
install -d build
cd build
%cmake \
        ../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make}  -C build install/fast \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*
