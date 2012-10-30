%define ver_progsreiserfs 0.3.1-rc8

%bcond_without	uclibc

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
BuildRequires:	pkgconfig(libntfs-3g) 
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(uuid)
%if %{with uclibc}
BuildRequires:	uClibc-devel >= 0.9.33.2-9
%endif

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

%package -n	uclibc-%{name}
Summary:	Tool to check and undelete partition (uClibc build)
Group:		System/Kernel and hardware

%description -n	uclibc-%{name}
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

%package -n	photorec
Summary:	Data recovery software
Group:		System/Kernel and hardware
Requires:	%{name} = %{version}

%description -n	photorec
PhotoRec is file data recovery software designed to recover lost files
including video, documents and archives from Hard Disks and CDRom and lost
pictures (thus, its 'Photo Recovery' name) from digital camera memory.

PhotoRec ignores the filesystem and goes after the underlying data, so it
will still work even if your media's filesystem has been severely damaged
or re-formatted.

%package -n	uclibc-photorec
Summary:	Data recovery software (uClibc build)
Group:		System/Kernel and hardware
Requires:	uclibc-%{name} = %{version}

%description -n	uclibc-photorec
PhotoRec is file data recovery software designed to recover lost files
including video, documents and archives from Hard Disks and CDRom and lost
pictures (thus, its 'Photo Recovery' name) from digital camera memory.

PhotoRec ignores the filesystem and goes after the underlying data, so it
will still work even if your media's filesystem has been severely damaged
or re-formatted.

%package -n	uclibc-photorec
Summary:	Data recovery software (uClibc build)
Group:		System/Kernel and hardware
Requires:	uclibc-%{name} = %{version}

%package -n	fidentify
Summary:	Data recovery software
Group:		System/Kernel and hardware
Requires:	%{name} = %{version}

%description -n	fidentify
Recover lost files from harddisk, digital camera and cdrom fidentify the file
type, the "extension", by using the same database than PhotoRec.

%package -n	uclibc-fidentify
Summary:	Data recovery software (uClibc build)
Group:		System/Kernel and hardware
Requires:	%{name} = %{version}

%description -n	uclibc-fidentify
Recover lost files from harddisk, digital camera and cdrom fidentify the file
type, the "extension", by using the same database than PhotoRec.

%prep
%setup -q -a 1
%patch0
#%patch1 -p1 -b .exiv2

%build
TOP_DIR="$PWD"
CONFIGURE_TOP=..
%if %{with uclibc}
mkdir -p progsreiserfs-%{ver_progsreiserfs}/uclibc
pushd progsreiserfs-%{ver_progsreiserfs}/uclibc
%uclibc_configure \
		--enable-shared=no \
		--enable-static=yes \
		--disable-Werror
%make
popd

mkdir -p uclibc
pushd uclibc
%uclibc_configure \
		--with-reiserfs-lib=${TOP_DIR}/progsreiserfs-%{ver_progsreiserfs}/uclibc/libreiserfs/.libs/ \
		--with-reiserfs-includes=${TOP_DIR}/progsreiserfs-%{ver_progsreiserfs}/include/
%make
popd
%endif

mkdir -p progsreiserfs-%{ver_progsreiserfs}/system
pushd progsreiserfs-%{ver_progsreiserfs}/system
%configure2_5x --disable-Werror
%make
popd

mkdir -p system
pushd system
%configure2_5x	--with-reiserfs-lib=${TOP_DIR}/progsreiserfs-%{ver_progsreiserfs}/system/libreiserfs/.libs/ \
		--with-reiserfs-includes=${TOP_DIR}/progsreiserfs-%{ver_progsreiserfs}/include/ \
		--enable-shared=no \
		--enable-static=yes
%make
popd

%install
%if %{with uclibc}
%makeinstall_std -C uclibc
%endif

%makeinstall_std -C system
rm -rf %{buildroot}%{_docdir}

%files
%doc AUTHORS ChangeLog INFO NEWS README THANKS doc/*.html
%attr(755,root,root) %{_bindir}/testdisk
%{_mandir}/man8/testdisk*

%files -n photorec
%{_bindir}/photorec
%{_mandir}/man8/photorec*

%files -n fidentify
%{_bindir}/fidentify
%{_mandir}/man8/fidentify*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}%{_bindir}/testdisk

%files -n uclibc-photorec
%{uclibc_root}%{_bindir}/photorec

%files -n uclibc-fidentify
%{uclibc_root}%{_bindir}/fidentify
%endif
