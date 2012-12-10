%global packname  sgeostat
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0_24
Release:          1
Summary:          An Object-oriented Framework for Geostatistical Modeling in S+
Group:            Sciences/Mathematics
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-24.tar.gz
Requires:         R-stats R-grDevices R-graphics 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-grDevices R-graphics

%description
An Object-oriented Framework for Geostatistical Modeling in S+

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0_24-1
+ Revision: 776272
- Import R-sgeostat
- Import R-sgeostat

