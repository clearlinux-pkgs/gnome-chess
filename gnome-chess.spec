#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-chess
Version  : 3.38.0
Release  : 6
URL      : https://download.gnome.org/sources/gnome-chess/3.38/gnome-chess-3.38.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-chess/3.38/gnome-chess-3.38.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC-BY-SA-3.0 GPL-3.0 W3C-19980720
Requires: gnome-chess-bin = %{version}-%{release}
Requires: gnome-chess-data = %{version}-%{release}
Requires: gnome-chess-license = %{version}-%{release}
Requires: gnome-chess-locales = %{version}-%{release}
Requires: gnome-chess-man = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : librsvg-dev
BuildRequires : pkgconfig(librsvg-2.0)
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
%setup -q -n gnome-chess-3.38.0
cd %{_builddir}/gnome-chess-3.38.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600277750
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-chess
cp %{_builddir}/gnome-chess-3.38.0/COPYING %{buildroot}/usr/share/package-licenses/gnome-chess/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gnome-chess-3.38.0/data/pieces/simple/COPYING.html %{buildroot}/usr/share/package-licenses/gnome-chess/47f1cad086978c84323c31985d84a78dcf1318bb
cp %{_builddir}/gnome-chess-3.38.0/help/C/license.page %{buildroot}/usr/share/package-licenses/gnome-chess/a5205a5ed7fcb904170e8d9ce7ad75fd6d541907
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-chess

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-chess

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Chess.desktop
/usr/share/dbus-1/services/org.gnome.Chess.service
/usr/share/defaults/gnome-chess/engines.conf
/usr/share/glib-2.0/schemas/org.gnome.Chess.gschema.xml
/usr/share/gnome-chess/pieces/fancy/blackBishop.svg
/usr/share/gnome-chess/pieces/fancy/blackKing.svg
/usr/share/gnome-chess/pieces/fancy/blackKnight.svg
/usr/share/gnome-chess/pieces/fancy/blackPawn.svg
/usr/share/gnome-chess/pieces/fancy/blackQueen.svg
/usr/share/gnome-chess/pieces/fancy/blackRook.svg
/usr/share/gnome-chess/pieces/fancy/whiteBishop.svg
/usr/share/gnome-chess/pieces/fancy/whiteKing.svg
/usr/share/gnome-chess/pieces/fancy/whiteKnight.svg
/usr/share/gnome-chess/pieces/fancy/whitePawn.svg
/usr/share/gnome-chess/pieces/fancy/whiteQueen.svg
/usr/share/gnome-chess/pieces/fancy/whiteRook.svg
/usr/share/gnome-chess/pieces/simple/COPYING.html
/usr/share/gnome-chess/pieces/simple/blackBishop.svg
/usr/share/gnome-chess/pieces/simple/blackKing.svg
/usr/share/gnome-chess/pieces/simple/blackKnight.svg
/usr/share/gnome-chess/pieces/simple/blackPawn.svg
/usr/share/gnome-chess/pieces/simple/blackQueen.svg
/usr/share/gnome-chess/pieces/simple/blackRook.svg
/usr/share/gnome-chess/pieces/simple/whiteBishop.svg
/usr/share/gnome-chess/pieces/simple/whiteKing.svg
/usr/share/gnome-chess/pieces/simple/whiteKnight.svg
/usr/share/gnome-chess/pieces/simple/whitePawn.svg
/usr/share/gnome-chess/pieces/simple/whiteQueen.svg
/usr/share/gnome-chess/pieces/simple/whiteRook.svg
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
/usr/share/help/C/gnome-chess/figures/gnome-chess-3-32.png
/usr/share/help/C/gnome-chess/figures/logo.png
/usr/share/help/C/gnome-chess/figures/logo32.png
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
/usr/share/help/ca/gnome-chess/figures/gnome-chess-3-32.png
/usr/share/help/ca/gnome-chess/figures/logo.png
/usr/share/help/ca/gnome-chess/figures/logo32.png
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
/usr/share/help/cs/gnome-chess/figures/gnome-chess-3-32.png
/usr/share/help/cs/gnome-chess/figures/logo.png
/usr/share/help/cs/gnome-chess/figures/logo32.png
/usr/share/help/cs/gnome-chess/index.page
/usr/share/help/cs/gnome-chess/license.page
/usr/share/help/cs/gnome-chess/play.page
/usr/share/help/cs/gnome-chess/rules.page
/usr/share/help/cs/gnome-chess/save-resume.page
/usr/share/help/cs/gnome-chess/timer.page
/usr/share/help/cs/gnome-chess/translate.page
/usr/share/help/de/gnome-chess/bug-filing.page
/usr/share/help/de/gnome-chess/change-board-orientation.page
/usr/share/help/de/gnome-chess/change-look-feel.page
/usr/share/help/de/gnome-chess/chess-engines.page
/usr/share/help/de/gnome-chess/develop.page
/usr/share/help/de/gnome-chess/documentation.page
/usr/share/help/de/gnome-chess/figures/gnome-chess-3-32.png
/usr/share/help/de/gnome-chess/figures/logo.png
/usr/share/help/de/gnome-chess/figures/logo32.png
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
/usr/share/help/es/gnome-chess/figures/gnome-chess-3-32.png
/usr/share/help/es/gnome-chess/figures/logo.png
/usr/share/help/es/gnome-chess/figures/logo32.png
/usr/share/help/es/gnome-chess/index.page
/usr/share/help/es/gnome-chess/license.page
/usr/share/help/es/gnome-chess/play.page
/usr/share/help/es/gnome-chess/rules.page
/usr/share/help/es/gnome-chess/save-resume.page
/usr/share/help/es/gnome-chess/timer.page
/usr/share/help/es/gnome-chess/translate.page
/usr/share/help/fr/gnome-chess/bug-filing.page
/usr/share/help/fr/gnome-chess/change-board-orientation.page
/usr/share/help/fr/gnome-chess/change-look-feel.page
/usr/share/help/fr/gnome-chess/chess-engines.page
/usr/share/help/fr/gnome-chess/develop.page
/usr/share/help/fr/gnome-chess/documentation.page
/usr/share/help/fr/gnome-chess/figures/gnome-chess-3-32.png
/usr/share/help/fr/gnome-chess/figures/logo.png
/usr/share/help/fr/gnome-chess/figures/logo32.png
/usr/share/help/fr/gnome-chess/index.page
/usr/share/help/fr/gnome-chess/license.page
/usr/share/help/fr/gnome-chess/play.page
/usr/share/help/fr/gnome-chess/rules.page
/usr/share/help/fr/gnome-chess/save-resume.page
/usr/share/help/fr/gnome-chess/timer.page
/usr/share/help/fr/gnome-chess/translate.page
/usr/share/help/pl/gnome-chess/bug-filing.page
/usr/share/help/pl/gnome-chess/change-board-orientation.page
/usr/share/help/pl/gnome-chess/change-look-feel.page
/usr/share/help/pl/gnome-chess/chess-engines.page
/usr/share/help/pl/gnome-chess/develop.page
/usr/share/help/pl/gnome-chess/documentation.page
/usr/share/help/pl/gnome-chess/figures/gnome-chess-3-32.png
/usr/share/help/pl/gnome-chess/figures/logo.png
/usr/share/help/pl/gnome-chess/figures/logo32.png
/usr/share/help/pl/gnome-chess/index.page
/usr/share/help/pl/gnome-chess/license.page
/usr/share/help/pl/gnome-chess/play.page
/usr/share/help/pl/gnome-chess/rules.page
/usr/share/help/pl/gnome-chess/save-resume.page
/usr/share/help/pl/gnome-chess/timer.page
/usr/share/help/pl/gnome-chess/translate.page
/usr/share/help/sv/gnome-chess/bug-filing.page
/usr/share/help/sv/gnome-chess/change-board-orientation.page
/usr/share/help/sv/gnome-chess/change-look-feel.page
/usr/share/help/sv/gnome-chess/chess-engines.page
/usr/share/help/sv/gnome-chess/develop.page
/usr/share/help/sv/gnome-chess/documentation.page
/usr/share/help/sv/gnome-chess/figures/gnome-chess-3-32.png
/usr/share/help/sv/gnome-chess/figures/logo.png
/usr/share/help/sv/gnome-chess/figures/logo32.png
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
/usr/share/help/uk/gnome-chess/figures/gnome-chess-3-32.png
/usr/share/help/uk/gnome-chess/figures/logo.png
/usr/share/help/uk/gnome-chess/figures/logo32.png
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

