Summary: Patch stack for Git repositories
Name: stgit
Version: 0.17.1
Release: 2%{?dist}
License: GPLv2
Group: Development/Tools
URL: http://www.procode.org/stgit/
Source: http://download.gna.org/%{name}/%{name}-%{version}.tar.gz

# resolves: #872651
Patch0: stgit-0.16-tmpl.patch

# Lambda Linux patches
Patch1001: 1001-Add-support-for-amzn-layout.patch

BuildArch: noarch
BuildRequires: git-core, python2-devel, asciidoc, xmlto
Requires: git-core, git-email, python2, vim-filesystem

%description
StGit is a Python application providing similar functionality
to Quilt (i.e. pushing/popping patches to/from a stack) on top of Git.
These operations are performed using Git commands and the patches
are stored as Git commit objects, allowing easy merging of the StGit patches
into other repositories using standard Git functionality.

Note that StGit is not an SCM interface on top of Git and it expects
a previously initialized Git repository. For standard SCM operations,
either use plain Git commands or the Cogito tool.

%prep
%setup -q
%patch0 -p1 -b .templ

%patch1001 -p1

chmod -x contrib/stgbashprompt.sh

%build
make all doc prefix=%{_prefix} %{?_smp_mflags}

%install
make install install-doc DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix}

# Install bash completion
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
ln -s ../..%{_datadir}/%{name}/completion/stgit-completion.bash \
    $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}

# Install vim syntax highlighting
install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax
install -m 644 contrib/vim/syntax/*.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax/
install -m 644 -D contrib/vim/ftdetect/stg.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/ftdetect/stg.vim

%files
%doc AUTHORS COPYING README RELEASENOTES
%{_bindir}/stg
%{python_sitelib}/*
%{_mandir}/man1/stg*
%{_sysconfdir}/bash_completion.d/
%{_datadir}/stgit/
%{_datadir}/vim/vimfiles/syntax/*.vim
%{_datadir}/vim/vimfiles/ftdetect/stg.vim

%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Peter Schiffer <pschiffe@redhat.com> - 0.17.1-1
- resolves: #1014240
  updated to 0.17.1
- resolves: #1004478
  added dependency on git-email package, so the stg mail command
  can function properly

* Wed Jul 31 2013 Peter Schiffer <pschiffe@redhat.com> - 0.17-3
- fixed dirty index errors when resolving conflicts

* Tue Jul 30 2013 Peter Schiffer <pschiffe@redhat.com> - 0.17-2
- included vim syntax highlighting (thanks to Zane Bitter <zbitter@redhat.com>)

* Thu Jul  4 2013 Peter Schiffer <pschiffe@redhat.com> - 0.17-1
- resolves: #979618
  updated to 0.17

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec  4 2012 Peter Schiffer <pschiffe@redhat.com> - 0.16-2
- resolves: #872651
  fixed regression when "stg new" command was ignoring patchdescr.tmpl file

* Mon Oct 22 2012 Peter Schiffer <pschiffe@redhat.com> - 0.16-1
- updated to 0.16

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.14.3-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.14.3-4
- Rebuild for Python 2.6

* Tue Dec 02 2008 James Bowes <jbowes@redhat.com> 0.14.3-3
- Try and make the summary text better

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.14.3-2
- Rebuild for Python 2.6

* Tue Jun 17 2008 James Bowes <jbowes@redhat.com> 0.14.3-1
- Update to 0.14.3

* Wed Mar 26 2008 James Bowes <jbowes@redhat.com> 0.14.2-1
- Update to 0.14.2

* Wed Dec 12 2007 James Bowes <jbowes@redhat.com> - 0.14.1-1
- Update to 0.14.1

* Thu Aug 23 2007 James Bowes <jbowes@redhat.com> - 0.13-2
- Mark license as GPLv2+

* Sun Aug 05 2007 James Bowes <jbowes@redhat.com> - 0.13-1
- Update to 0.13

* Wed Apr 25 2007 James Bowes <jbowes@redhat.com> - 0.12.1-2
- Use macro for datadir.

* Thu Apr 19 2007 James Bowes <jbowes@redhat.com> - 0.12.1-1
- Update version.
- Don't install the bash prompt shell script as executable.

* Fri Feb 02 2007 James Bowes <jbowes@redhat.com> - 0.12-1
- Initial packaging.
