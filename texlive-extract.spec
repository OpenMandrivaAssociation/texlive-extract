# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/extract
# catalog-date 2006-11-09 15:16:55 +0100
# catalog-license lppl
# catalog-version 1.8
Name:		texlive-extract
Version:	1.8
Release:	5
Summary:	Extract parts of a document and write to another document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/extract
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extract.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extract.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extract.source.tar.xz
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
%{_texmfdistdir}/tex/latex/extract/extract.sty
%doc %{_texmfdistdir}/doc/latex/extract/README
%doc %{_texmfdistdir}/doc/latex/extract/extract.pdf
#- source
%doc %{_texmfdistdir}/source/latex/extract/extract.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.8-2
+ Revision: 751749
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.8-1
+ Revision: 718406
- texlive-extract
- texlive-extract
- texlive-extract
- texlive-extract

