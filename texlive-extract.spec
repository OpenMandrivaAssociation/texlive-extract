%global tl_name extract
%global tl_revision 52117

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9a
Release:	%{tl_revision}.1
Summary:	Extract parts of a document and write to another document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/extract
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/extract.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/extract.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/extract.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to extract specific content from a source
document and write that to a target document. One could, for instance,
use this to extract all exercises from lecture notes and generate an
exercises book on the fly. The package also provides an environment
which writes its body entirely to the target file. Another environment
will write to the target file, but will also execute the body. This
allows to share code (for instance, a preamble) between the source
document and the target file. Finally, the package provides an interface
to conditionally extract content. With a single package option, one can
specify exactly which commands (counted from the start of the document)
should be extracted and which not. This might be useful for extracting
specific slides from a presentation and use them in a new file.

