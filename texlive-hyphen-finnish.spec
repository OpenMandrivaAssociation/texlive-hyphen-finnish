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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Finnish in T1 and UTF-8 encodings. The older
set, labelled just 'fi', tries to implement etymological rules, while
the newer ones (fi-x-school) implements the simpler rules taught at
Finnish school.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-finnish:
finnish loadhyph-fi.tex
schoolfinnish loadhyph-fi-x-school.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-finnish:
\addlanguage{finnish}{loadhyph-fi.tex}{}{2}{2}
\addlanguage{schoolfinnish}{loadhyph-fi-x-school.tex}{}{1}{1}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-finnish:
['finnish'] = {
	loader = 'loadhyph-fi.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-fi.pat.txt',
},
['schoolfinnish'] = {
	loader = 'loadhyph-fi-x-school.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-fi-x-school.pat.txt',
},
TL_HYPHEN_EOF
