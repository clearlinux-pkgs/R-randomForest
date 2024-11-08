#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-randomForest
Version  : 4.7.1.2
Release  : 95
URL      : https://cran.r-project.org/src/contrib/randomForest_4.7-1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/randomForest_4.7-1.2.tar.gz
Summary  : Breiman and Cutlers Random Forests for Classification and
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-randomForest-lib = %{version}-%{release}
Requires: R-randomForest-license = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the R-randomForest package.
Group: Libraries
Requires: R-randomForest-license = %{version}-%{release}

%description lib
lib components for the R-randomForest package.


%package license
Summary: license components for the R-randomForest package.
Group: Default

%description license
license components for the R-randomForest package.


%prep
%setup -q -n randomForest
pushd ..
cp -a randomForest buildavx2
popd
pushd ..
cp -a randomForest buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727041967

%install
export SOURCE_DATE_EPOCH=1727041967
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-randomForest
cp %{_builddir}/randomForest/COPYING %{buildroot}/usr/share/package-licenses/R-randomForest/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/randomForest/CITATION
/usr/lib64/R/library/randomForest/DESCRIPTION
/usr/lib64/R/library/randomForest/INDEX
/usr/lib64/R/library/randomForest/Meta/Rd.rds
/usr/lib64/R/library/randomForest/Meta/data.rds
/usr/lib64/R/library/randomForest/Meta/features.rds
/usr/lib64/R/library/randomForest/Meta/hsearch.rds
/usr/lib64/R/library/randomForest/Meta/links.rds
/usr/lib64/R/library/randomForest/Meta/nsInfo.rds
/usr/lib64/R/library/randomForest/Meta/package.rds
/usr/lib64/R/library/randomForest/NAMESPACE
/usr/lib64/R/library/randomForest/NEWS
/usr/lib64/R/library/randomForest/R/randomForest
/usr/lib64/R/library/randomForest/R/randomForest.rdb
/usr/lib64/R/library/randomForest/R/randomForest.rdx
/usr/lib64/R/library/randomForest/data/imports85.rda
/usr/lib64/R/library/randomForest/help/AnIndex
/usr/lib64/R/library/randomForest/help/aliases.rds
/usr/lib64/R/library/randomForest/help/paths.rds
/usr/lib64/R/library/randomForest/help/randomForest.rdb
/usr/lib64/R/library/randomForest/help/randomForest.rdx
/usr/lib64/R/library/randomForest/html/00Index.html
/usr/lib64/R/library/randomForest/html/R.css

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/randomForest/libs/randomForest.so
/V4/usr/lib64/R/library/randomForest/libs/randomForest.so
/usr/lib64/R/library/randomForest/libs/randomForest.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-randomForest/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
