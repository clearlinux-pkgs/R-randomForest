#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-randomForest
Version  : 4.6.14
Release  : 47
URL      : https://cran.r-project.org/src/contrib/randomForest_4.6-14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/randomForest_4.6-14.tar.gz
Summary  : Breiman and Cutler's Random Forests for Classification and
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-randomForest-lib
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-randomForest package.
Group: Libraries

%description lib
lib components for the R-randomForest package.


%prep
%setup -q -c -n randomForest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522162522

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1522162522
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library randomForest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library randomForest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library randomForest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library randomForest|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/randomForest/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/randomForest/libs/randomForest.so
/usr/lib64/R/library/randomForest/libs/randomForest.so.avx2
/usr/lib64/R/library/randomForest/libs/randomForest.so.avx512
