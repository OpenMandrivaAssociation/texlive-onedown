Name:		texlive-onedown
Version:	69067
Release:	1
Summary:	Typeset Bridge Diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/onedown
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onedown.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onedown.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onedown.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a comprehensive package to draw all sorts of bridge
diagrams, including hands (stand alone or arround a compass),
bidding tables (stand alone or in connection with
hands/compass), trick tables, and expert quizzes. Features:
Works for all fontsizes from \ssmall to \HUGE. Different fonts
for hands, bidding diagrams, compass, etc. are possible.
Annotations to card and bidding diagrams. Automated check on
consistency of suit and hands. Multilingual output of bridge
terms. Extensive documentation: User manual, Reference manual,
and Examples.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/onedown
%{_texmfdistdir}/tex/latex/onedown
%doc %{_texmfdistdir}/doc/latex/onedown

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
