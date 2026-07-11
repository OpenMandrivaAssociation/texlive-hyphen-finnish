%global tl_name hyphen-finnish
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Finnish hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/fihyph
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-finnish.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Finnish in T1 and UTF-8 encodings. The older
set, labelled just 'fi', tries to implement etymological rules, while
the newer ones (fi-x-school) implements the simpler rules taught at
Finnish school.

