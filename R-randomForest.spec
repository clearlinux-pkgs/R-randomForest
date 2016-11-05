#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-randomForest
Version  : 4.6
Release  : 24
URL      : http://cran.r-project.org/src/contrib/randomForest_4.6-10.tar.gz
Source0  : http://cran.r-project.org/src/contrib/randomForest_4.6-10.tar.gz
Summary  : Breiman and Cutler's random forests for classification and
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n randomForest

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library randomForest
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library randomForest


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/randomForest/CITATION
/usr/lib64/R/library/randomForest/DESCRIPTION
/usr/lib64/R/library/randomForest/INDEX
/usr/lib64/R/library/randomForest/Meta/Rd.rds
/usr/lib64/R/library/randomForest/Meta/data.rds
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
/usr/lib64/R/library/randomForest/libs/randomForest.so
/usr/lib64/R/library/randomForest/libs/symbols.rds
