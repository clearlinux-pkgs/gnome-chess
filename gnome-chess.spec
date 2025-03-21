#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : gnome-chess
Version  : 48.0
Release  : 23
URL      : https://download.gnome.org/sources/gnome-chess/48/gnome-chess-48.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-chess/48/gnome-chess-48.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC-BY-SA-3.0 GPL-3.0 W3C-19980720
Requires: gnome-chess-bin = %{version}-%{release}
Requires: gnome-chess-data = %{version}-%{release}
Requires: gnome-chess-license = %{version}-%{release}
Requires: gnome-chess-locales = %{version}-%{release}
Requires: gnome-chess-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : librsvg-dev
BuildRequires : pkgconfig(libadwaita-1)
BuildRequires : pkgconfig(librsvg-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-stateless-configuration.patch

%description
# GNOME Chess
GNOME Chess is a 2D chess game, where games can be played between a combination of human and computer players.
GNOME Chess detects known third party chess engines for computer players.

%package bin
Summary: bin components for the gnome-chess package.
Group: Binaries
Requires: gnome-chess-data = %{version}-%{release}
Requires: gnome-chess-license = %{version}-%{release}

%description bin
bin components for the gnome-chess package.


%package data
Summary: data components for the gnome-chess package.
Group: Data

%description data
data components for the gnome-chess package.


%package doc
Summary: doc components for the gnome-chess package.
Group: Documentation
Requires: gnome-chess-man = %{version}-%{release}

%description doc
doc components for the gnome-chess package.


%package license
Summary: license components for the gnome-chess package.
Group: Default

%description license
license components for the gnome-chess package.


%package locales
Summary: locales components for the gnome-chess package.
Group: Default

%description locales
locales components for the gnome-chess package.


%package man
Summary: man components for the gnome-chess package.
Group: Default

%description man
man components for the gnome-chess package.


%prep
%setup -q -n gnome-chess-48.0
cd %{_builddir}/gnome-chess-48.0
%patch -P 1 -p1
pushd ..
cp -a gnome-chess-48.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742586015
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :
cd ../buildavx2;
meson test -C builddir --print-errorlogs || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-chess
cp %{_builddir}/gnome-chess-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-chess/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/gnome-chess-%{version}/data/pieces/simple/COPYING.html %{buildroot}/usr/share/package-licenses/gnome-chess/47f1cad086978c84323c31985d84a78dcf1318bb || :
cp %{_builddir}/gnome-chess-%{version}/help/C/license.page %{buildroot}/usr/share/package-licenses/gnome-chess/a5205a5ed7fcb904170e8d9ce7ad75fd6d541907 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-chess
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gnome-chess
/usr/bin/gnome-chess

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Chess.desktop
/usr/share/dbus-1/services/org.gnome.Chess.service
/usr/share/defaults/gnome-chess/engines.conf
/usr/share/glib-2.0/schemas/org.gnome.Chess.gschema.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.Chess.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Chess-symbolic.svg
/usr/share/metainfo/org.gnome.Chess.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-chess/bug-filing.page
/usr/share/help/C/gnome-chess/change-board-orientation.page
/usr/share/help/C/gnome-chess/change-look-feel.page
/usr/share/help/C/gnome-chess/chess-engines.page
/usr/share/help/C/gnome-chess/develop.page
/usr/share/help/C/gnome-chess/documentation.page
/usr/share/help/C/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/C/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/C/gnome-chess/index.page
/usr/share/help/C/gnome-chess/license.page
/usr/share/help/C/gnome-chess/play.page
/usr/share/help/C/gnome-chess/rules.page
/usr/share/help/C/gnome-chess/save-resume.page
/usr/share/help/C/gnome-chess/timer.page
/usr/share/help/C/gnome-chess/translate.page
/usr/share/help/ca/gnome-chess/bug-filing.page
/usr/share/help/ca/gnome-chess/change-board-orientation.page
/usr/share/help/ca/gnome-chess/change-look-feel.page
/usr/share/help/ca/gnome-chess/chess-engines.page
/usr/share/help/ca/gnome-chess/develop.page
/usr/share/help/ca/gnome-chess/documentation.page
/usr/share/help/ca/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/ca/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/ca/gnome-chess/index.page
/usr/share/help/ca/gnome-chess/license.page
/usr/share/help/ca/gnome-chess/play.page
/usr/share/help/ca/gnome-chess/rules.page
/usr/share/help/ca/gnome-chess/save-resume.page
/usr/share/help/ca/gnome-chess/timer.page
/usr/share/help/ca/gnome-chess/translate.page
/usr/share/help/cs/gnome-chess/bug-filing.page
/usr/share/help/cs/gnome-chess/change-board-orientation.page
/usr/share/help/cs/gnome-chess/change-look-feel.page
/usr/share/help/cs/gnome-chess/chess-engines.page
/usr/share/help/cs/gnome-chess/develop.page
/usr/share/help/cs/gnome-chess/documentation.page
/usr/share/help/cs/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/cs/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/cs/gnome-chess/index.page
/usr/share/help/cs/gnome-chess/license.page
/usr/share/help/cs/gnome-chess/play.page
/usr/share/help/cs/gnome-chess/rules.page
/usr/share/help/cs/gnome-chess/save-resume.page
/usr/share/help/cs/gnome-chess/timer.page
/usr/share/help/cs/gnome-chess/translate.page
/usr/share/help/da/gnome-chess/bug-filing.page
/usr/share/help/da/gnome-chess/change-board-orientation.page
/usr/share/help/da/gnome-chess/change-look-feel.page
/usr/share/help/da/gnome-chess/chess-engines.page
/usr/share/help/da/gnome-chess/develop.page
/usr/share/help/da/gnome-chess/documentation.page
/usr/share/help/da/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/da/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/da/gnome-chess/index.page
/usr/share/help/da/gnome-chess/license.page
/usr/share/help/da/gnome-chess/play.page
/usr/share/help/da/gnome-chess/rules.page
/usr/share/help/da/gnome-chess/save-resume.page
/usr/share/help/da/gnome-chess/timer.page
/usr/share/help/da/gnome-chess/translate.page
/usr/share/help/de/gnome-chess/bug-filing.page
/usr/share/help/de/gnome-chess/change-board-orientation.page
/usr/share/help/de/gnome-chess/change-look-feel.page
/usr/share/help/de/gnome-chess/chess-engines.page
/usr/share/help/de/gnome-chess/develop.page
/usr/share/help/de/gnome-chess/documentation.page
/usr/share/help/de/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/de/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/de/gnome-chess/index.page
/usr/share/help/de/gnome-chess/license.page
/usr/share/help/de/gnome-chess/play.page
/usr/share/help/de/gnome-chess/rules.page
/usr/share/help/de/gnome-chess/save-resume.page
/usr/share/help/de/gnome-chess/timer.page
/usr/share/help/de/gnome-chess/translate.page
/usr/share/help/es/gnome-chess/bug-filing.page
/usr/share/help/es/gnome-chess/change-board-orientation.page
/usr/share/help/es/gnome-chess/change-look-feel.page
/usr/share/help/es/gnome-chess/chess-engines.page
/usr/share/help/es/gnome-chess/develop.page
/usr/share/help/es/gnome-chess/documentation.page
/usr/share/help/es/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/es/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/es/gnome-chess/index.page
/usr/share/help/es/gnome-chess/license.page
/usr/share/help/es/gnome-chess/play.page
/usr/share/help/es/gnome-chess/rules.page
/usr/share/help/es/gnome-chess/save-resume.page
/usr/share/help/es/gnome-chess/timer.page
/usr/share/help/es/gnome-chess/translate.page
/usr/share/help/eu/gnome-chess/bug-filing.page
/usr/share/help/eu/gnome-chess/change-board-orientation.page
/usr/share/help/eu/gnome-chess/change-look-feel.page
/usr/share/help/eu/gnome-chess/chess-engines.page
/usr/share/help/eu/gnome-chess/develop.page
/usr/share/help/eu/gnome-chess/documentation.page
/usr/share/help/eu/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/eu/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/eu/gnome-chess/index.page
/usr/share/help/eu/gnome-chess/license.page
/usr/share/help/eu/gnome-chess/play.page
/usr/share/help/eu/gnome-chess/rules.page
/usr/share/help/eu/gnome-chess/save-resume.page
/usr/share/help/eu/gnome-chess/timer.page
/usr/share/help/eu/gnome-chess/translate.page
/usr/share/help/fr/gnome-chess/bug-filing.page
/usr/share/help/fr/gnome-chess/change-board-orientation.page
/usr/share/help/fr/gnome-chess/change-look-feel.page
/usr/share/help/fr/gnome-chess/chess-engines.page
/usr/share/help/fr/gnome-chess/develop.page
/usr/share/help/fr/gnome-chess/documentation.page
/usr/share/help/fr/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/fr/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/fr/gnome-chess/index.page
/usr/share/help/fr/gnome-chess/license.page
/usr/share/help/fr/gnome-chess/play.page
/usr/share/help/fr/gnome-chess/rules.page
/usr/share/help/fr/gnome-chess/save-resume.page
/usr/share/help/fr/gnome-chess/timer.page
/usr/share/help/fr/gnome-chess/translate.page
/usr/share/help/hu/gnome-chess/bug-filing.page
/usr/share/help/hu/gnome-chess/change-board-orientation.page
/usr/share/help/hu/gnome-chess/change-look-feel.page
/usr/share/help/hu/gnome-chess/chess-engines.page
/usr/share/help/hu/gnome-chess/develop.page
/usr/share/help/hu/gnome-chess/documentation.page
/usr/share/help/hu/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/hu/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/hu/gnome-chess/index.page
/usr/share/help/hu/gnome-chess/license.page
/usr/share/help/hu/gnome-chess/play.page
/usr/share/help/hu/gnome-chess/rules.page
/usr/share/help/hu/gnome-chess/save-resume.page
/usr/share/help/hu/gnome-chess/timer.page
/usr/share/help/hu/gnome-chess/translate.page
/usr/share/help/ko/gnome-chess/bug-filing.page
/usr/share/help/ko/gnome-chess/change-board-orientation.page
/usr/share/help/ko/gnome-chess/change-look-feel.page
/usr/share/help/ko/gnome-chess/chess-engines.page
/usr/share/help/ko/gnome-chess/develop.page
/usr/share/help/ko/gnome-chess/documentation.page
/usr/share/help/ko/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/ko/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/ko/gnome-chess/index.page
/usr/share/help/ko/gnome-chess/license.page
/usr/share/help/ko/gnome-chess/play.page
/usr/share/help/ko/gnome-chess/rules.page
/usr/share/help/ko/gnome-chess/save-resume.page
/usr/share/help/ko/gnome-chess/timer.page
/usr/share/help/ko/gnome-chess/translate.page
/usr/share/help/pl/gnome-chess/bug-filing.page
/usr/share/help/pl/gnome-chess/change-board-orientation.page
/usr/share/help/pl/gnome-chess/change-look-feel.page
/usr/share/help/pl/gnome-chess/chess-engines.page
/usr/share/help/pl/gnome-chess/develop.page
/usr/share/help/pl/gnome-chess/documentation.page
/usr/share/help/pl/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/pl/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/pl/gnome-chess/index.page
/usr/share/help/pl/gnome-chess/license.page
/usr/share/help/pl/gnome-chess/play.page
/usr/share/help/pl/gnome-chess/rules.page
/usr/share/help/pl/gnome-chess/save-resume.page
/usr/share/help/pl/gnome-chess/timer.page
/usr/share/help/pl/gnome-chess/translate.page
/usr/share/help/pt_BR/gnome-chess/bug-filing.page
/usr/share/help/pt_BR/gnome-chess/change-board-orientation.page
/usr/share/help/pt_BR/gnome-chess/change-look-feel.page
/usr/share/help/pt_BR/gnome-chess/chess-engines.page
/usr/share/help/pt_BR/gnome-chess/develop.page
/usr/share/help/pt_BR/gnome-chess/documentation.page
/usr/share/help/pt_BR/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/pt_BR/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/pt_BR/gnome-chess/index.page
/usr/share/help/pt_BR/gnome-chess/license.page
/usr/share/help/pt_BR/gnome-chess/play.page
/usr/share/help/pt_BR/gnome-chess/rules.page
/usr/share/help/pt_BR/gnome-chess/save-resume.page
/usr/share/help/pt_BR/gnome-chess/timer.page
/usr/share/help/pt_BR/gnome-chess/translate.page
/usr/share/help/ru/gnome-chess/bug-filing.page
/usr/share/help/ru/gnome-chess/change-board-orientation.page
/usr/share/help/ru/gnome-chess/change-look-feel.page
/usr/share/help/ru/gnome-chess/chess-engines.page
/usr/share/help/ru/gnome-chess/develop.page
/usr/share/help/ru/gnome-chess/documentation.page
/usr/share/help/ru/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/ru/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/ru/gnome-chess/index.page
/usr/share/help/ru/gnome-chess/license.page
/usr/share/help/ru/gnome-chess/play.page
/usr/share/help/ru/gnome-chess/rules.page
/usr/share/help/ru/gnome-chess/save-resume.page
/usr/share/help/ru/gnome-chess/timer.page
/usr/share/help/ru/gnome-chess/translate.page
/usr/share/help/sv/gnome-chess/bug-filing.page
/usr/share/help/sv/gnome-chess/change-board-orientation.page
/usr/share/help/sv/gnome-chess/change-look-feel.page
/usr/share/help/sv/gnome-chess/chess-engines.page
/usr/share/help/sv/gnome-chess/develop.page
/usr/share/help/sv/gnome-chess/documentation.page
/usr/share/help/sv/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/sv/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/sv/gnome-chess/index.page
/usr/share/help/sv/gnome-chess/license.page
/usr/share/help/sv/gnome-chess/play.page
/usr/share/help/sv/gnome-chess/rules.page
/usr/share/help/sv/gnome-chess/save-resume.page
/usr/share/help/sv/gnome-chess/timer.page
/usr/share/help/sv/gnome-chess/translate.page
/usr/share/help/uk/gnome-chess/bug-filing.page
/usr/share/help/uk/gnome-chess/change-board-orientation.page
/usr/share/help/uk/gnome-chess/change-look-feel.page
/usr/share/help/uk/gnome-chess/chess-engines.page
/usr/share/help/uk/gnome-chess/develop.page
/usr/share/help/uk/gnome-chess/documentation.page
/usr/share/help/uk/gnome-chess/figures/gnome-chess-40.png
/usr/share/help/uk/gnome-chess/figures/org.gnome.Chess.svg
/usr/share/help/uk/gnome-chess/index.page
/usr/share/help/uk/gnome-chess/license.page
/usr/share/help/uk/gnome-chess/play.page
/usr/share/help/uk/gnome-chess/rules.page
/usr/share/help/uk/gnome-chess/save-resume.page
/usr/share/help/uk/gnome-chess/timer.page
/usr/share/help/uk/gnome-chess/translate.page

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-chess/47f1cad086978c84323c31985d84a78dcf1318bb
/usr/share/package-licenses/gnome-chess/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/gnome-chess/a5205a5ed7fcb904170e8d9ce7ad75fd6d541907

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man6/gnome-chess.6

%files locales -f gnome-chess.lang
%defattr(-,root,root,-)

