%global tl_name mluexercise
%global tl_revision 56927

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Exercises/homework at the Martin Luther University Halle-Wittenberg
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mluexercise
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mluexercise.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mluexercise.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mluexercise.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a template class for solving weekly exercises at
the Institute for Computer Science of Martin Luther University Halle-
Wittenberg. The class can be used by all students--especially first
semesters--to typeset their exercises with low effort in beautiful
LaTeX. A bunch of handy macros are included that are used throughout
many lectures during the bachelor's degree program. The class is
maintained by the students' council of the university. The focus is on
encouraging first semester students to use LaTeX for typesetting, thus
the package has been kept as simple as possible.

