# revision 25990
# category TLCore
# catalog-ctan /language/hyphenation/fihyph
# catalog-date 2009-09-27 10:36:15 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-hyphen-finnish
Version:	20181105
Release:	1
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
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-finnish
%_texmf_language_def_d/hyphen-finnish
%_texmf_language_lua_d/hyphen-finnish

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

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


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090927-4
+ Revision: 804731
- Update to latest release.

* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090927-3
+ Revision: 767542
- Add workaround to rpm bug that broke hyphenation files
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090927-2
+ Revision: 759912
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090927-1
+ Revision: 718654
- texlive-hyphen-finnish
- texlive-hyphen-finnish
- texlive-hyphen-finnish
- texlive-hyphen-finnish

