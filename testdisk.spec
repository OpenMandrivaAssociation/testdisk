%define ver_progsreiserfs 0.3.1-rc8

Summary:	Tool to check and undelete partition
Name:		testdisk
Version:	6.13
Release:	2
License:	GPLv2+
Group:		System/Kernel and hardware
Source0:	http://www.cgsecurity.org/%{name}-%{version}.tar.bz2
Source1:	progsreiserfs-%{ver_progsreiserfs}.tar.bz2
Patch0:		progsreiserfs-journal.patch
# Upstream patch
Patch1:		photorec_611_exif_bound_checking_v2.patch
URL:		http://www.cgsecurity.org/wiki/TestDisk
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:  pkgconfig(libntfs-3g) 
BuildRequires:	devel(libjpeg(64bit))
BuildRequires:	pkgconfig(uuid)

%package -n	photorec
Summary:	Data recovery software
Group:		System/Kernel and hardware
Requires:	%{name} = %{version}

%description
Tool to check and undelete partition. Works with the following
filesystems:
    * BeFS ( BeOS )
    * BSD disklabel ( FreeBSD/OpenBSD/NetBSD )
    * CramFS, Compressed File System
    * DOS/Windows FAT12, FAT16 and FAT32
    * HFS and HFS+, Hierarchical File System
    * JFS, IBM's Journaled File System
    * Linux Ext2 and Ext3
    * Linux Raid
          o RAID 1: mirroring
          o RAID 4: striped array with parity device
          o RAID 5: striped array with distributed parity information
          o RAID 6: striped array with distributed dual redundancy information 
    * Linux Swap (versions 1 and 2)
    * LVM and LVM2, Linux Logical Volume Manager
    * Mac partition map
    * Novell Storage Services NSS
    * NTFS ( Windows NT/2K/XP/2003/Vista )
    * ReiserFS 3.5, 3.6 and 4
    * Sun Solaris i386 disklabel
    * Unix File System UFS and UFS2 (Sun/BSD/...)
    * XFS, SGI's Journaled File System 

%description -n	photorec
PhotoRec is file data recovery software designed to recover lost files
including video, documents and archives from Hard Disks and CDRom and lost
pictures (thus, its 'Photo Recovery' name) from digital camera memory.

PhotoRec ignores the filesystem and goes after the underlying data, so it
will still work even if your media's filesystem has been severely damaged
or re-formatted.


%package -n	fidentify
Summary:	Data recovery software
Group:		System/Kernel and hardware
Requires:	%{name} = %{version}

%description -n	fidentify
Recover lost files from harddisk, digital camera and cdrom
fidentify the file type, the "extension", by using thr same database than PhotoRec.


%prep
%setup -q -a 1 -D -n %{name}-%{version}
%patch0
#%patch1 -p1 -b .exiv2

%build
pushd progsreiserfs-%{ver_progsreiserfs}
%configure2_5x --disable-Werror
%make
popd

%configure2_5x --with-reiserfs-lib=`pwd`/progsreiserfs-%ver_progsreiserfs/libreiserfs/.libs/ --with-reiserfs-includes=`pwd`/progsreiserfs-%ver_progsreiserfs/include/
%make

%install
%makeinstall_std 

rm -rf %{buildroot}/%_docdir

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INFO INSTALL NEWS README THANKS doc/*.html
%attr(755,root,root) %{_bindir}/testdisk
%{_mandir}/man8/testdisk*

%files -n photorec
%attr(755,root,root) %{_bindir}/photorec
%{_mandir}/man8/photorec*

%files -n fidentify
%attr(755,root,root) %{_bindir}/fidentify
%{_mandir}/man8/fidentify*

