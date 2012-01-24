# revision 23092
# category TLCore
# catalog-ctan /language/hyphenation/fihyph
# catalog-date 2009-09-27 10:36:15 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-hyphen-finnish
Version:	20090927
Release:	3
Summary:	Finnish hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/fihyph
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-finnish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Finnish in T1/EC and UTF-8 encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-finnish
%_texmf_language_def_d/hyphen-finnish
%_texmf_language_lua_d/hyphen-finnish

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-finnish <<EOF
\%% from hyphen-finnish:
finnish loadhyph-fi.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-finnish
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-finnish <<EOF
\%% from hyphen-finnish:
\addlanguage{finnish}{loadhyph-fi.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-finnish
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-finnish <<EOF
-- from hyphen-finnish:
	['finnish'] = {
		loader = 'loadhyph-fi.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-fi.pat.txt',
		hyphenation = '',
	},
EOF
