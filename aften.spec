Summary:	A/52 audio encoder
Summary(pl.UTF-8):	Koder dźwięku A/52
Name:		aften
Version:	0.0.8
Release:	2
License:	LGPL v2+
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/aften/%{name}-%{version}.tar.bz2
# Source0-md5:	fde67146879febb81af3d95a62df8840
Patch0:		%{name}-libdir.patch
URL:		http://aften.sourceforge.net/
BuildRequires:	cmake >= 2.4
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aften is an audio encoder which generates compressed audio streams
based on ATSC A/52 specification. This type of audio is also known
as AC-3 or Dolby(R) Digital and is one of the audio codecs used in
DVD-Video content. 

%description -l en.UTF-8
Aften is an audio encoder which generates compressed audio streams
based on ATSC A/52 specification. This type of audio is also known
as AC-3 or Dolby® Digital and is one of the audio codecs used in
DVD-Video content. 

%description -l pl.UTF-8
Aften to koder dźwięku generujący skompresowane strumienie dźwięku
oparte na specyfikacji ATSC A/52. Ten format jest znany także jako
AC-3 lub Dolby® Digital i jest jednym z kodeków dźwięku używanych w
treściach DVD-Video.

%package devel
Summary:	Header files for Aften library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Aften
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Aften library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Aften.

%package c++
Summary:	C++ binding for Aften library
Summary(pl.UTF-8):	Interfejs C++ do biblioteki Aften
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ binding for Aften library.

%description c++ -l pl.UTF-8
Interfejs C++ do biblioteki Aften.

%package c++-devel
Summary:	Header file for C++ binding for Aften library
Summary(pl.UTF-8):	Plik nagłówkowy interfejsu C++ do biblioteki Aften
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header file for C++ binding for Aften library.

%description c++-devel -l pl.UTF-8
Plik nagłówkowy interfejsu C++ do biblioteki Aften.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake .. \
	-DSHARED=ON \
	-DBINDINGS_CXX=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install/fast \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/aften
%attr(755,root,root) %{_bindir}/wavfilter
%attr(755,root,root) %{_bindir}/wavinfo
%attr(755,root,root) %{_bindir}/wavrms
%attr(755,root,root) %{_libdir}/libaften.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaften.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaften.so
%dir %{_includedir}/aften
%{_includedir}/aften/aften-types.h
%{_includedir}/aften/aften.h

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaftenxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaftenxx.so.0

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaftenxx.so
%{_includedir}/aften/aftenxx.h
