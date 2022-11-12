Name:		texlive-extract
Version:	52117
Release:	1
Summary:	Extract parts of a document and write to another document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/extract
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extract.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extract.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extract.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to extract specific content from
a source document and write that to a target document. One
could, for instance, use this to extract all exercises from
lecture notes and generate an exercises book on the fly. The
package also provides an environment which writes its body
entirely to the target file. Another environment will write to
the target file, but will also execute the body. This allows to
share code (for instance, a preamble) between the source
document and the target file. Finally, the package provides an
interface to conditionally extract content. With a single
package option, one can specify exactly which commands (counted
from the start of the document) should be extracted and which
not. This might be useful for extracting specific slides from a
presentation and use them in a new file.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/extract
%doc %{_texmfdistdir}/doc/latex/extract
#- source
%doc %{_texmfdistdir}/source/latex/extract

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
