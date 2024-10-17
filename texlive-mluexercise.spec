Name:		texlive-mluexercise
Version:	56927
Release:	2
Summary:	Exercises/homework at the Martin Luther University Halle-Wittenberg
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mluexercise
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mluexercise.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mluexercise.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mluexercise.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a template class for solving weekly
exercises at the Institute for Computer Science of Martin
Luther University Halle-Wittenberg. The class can be used by
all students--especially first semesters--to typeset their
exercises with low effort in beautiful LaTeX. A bunch of handy
macros are included that are used throughout many lectures
during the bachelor's degree program. The class is maintained
by the students' council of the university. The focus is on
encouraging first semester students to use LaTeX for
typesetting, thus the package has been kept as simple as
possible.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mluexercise
%{_texmfdistdir}/tex/latex/mluexercise
%doc %{_texmfdistdir}/doc/latex/mluexercise

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
