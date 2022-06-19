%define ver_progsreiserfs 0.3.1-rc8
%define _disable_rebuild_configure 1

%ifnarch %{riscv}
%bcond_without qt5
%else
%bcond_with qt5
%endif

Summary:	Tool to check and undelete partition
Name:		testdisk
Version:	7.1
Release:	3
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://www.cgsecurity.org/wiki/TestDisk
Source0:	http://www.cgsecurity.org/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libewf)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(libntfs-3g)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(uuid)
BuildRequires:	gettext-devel
BuildRequires:  zlib-devel
BuildRequires:	perl
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	m4

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

%package -n	fidentify
Summary:	Data recovery software
Group:		System/Kernel and hardware
Requires:	%{name} = %{version}

%description -n	fidentify
Recover lost files from harddisk, digital camera and cdrom fidentify the file
type, the "extension", by using the same database than PhotoRec.

%if %{with qt5}
%package -n qphotorec
Summary:        Signature based file carver. Recover lost files
BuildRequires:  qt5-linguist
BuildRequires:	qt5-linguist-tools
BuildRequires:  qt5-qtbase-devel

%description -n qphotorec
QPhotoRec is a Qt version of PhotoRec. It is a signature based file recovery
utility. It handles more than 440 file formats including JPG, MSOffice,
OpenOffice documents.
%endif

%prep
%autosetup -p1

%build
TOP_DIR="$PWD"
CONFIGURE_TOP=..

mkdir -p system
pushd system
%configure	--without-reiserfs \
		--enable-shared=no \
		--enable-static=yes
%make_build
popd

%install
%makeinstall_std -C system

rm -r %{buildroot}%{_docdir}/%{name}/

%files
%doc AUTHORS ChangeLog INFO NEWS THANKS
# doc/*.html
%{_bindir}/testdisk
%{_mandir}/man8/testdisk*
%{_mandir}/*/man8/testdisk*

%files -n photorec
%{_bindir}/photorec
%{_mandir}/man8/photorec*
%{_mandir}/zh_CN/man8/photorec.8*

%if %{with qt5}
%files -n qphotorec
%{_bindir}/qphotorec
%{_mandir}/man8/qphotorec.8*
%{_mandir}/zh_CN/man8/qphotorec.8*
%{_datadir}/applications/qphotorec.desktop
%{_datadir}/icons/hicolor/48x48/apps/qphotorec.png
%{_datadir}/icons/hicolor/scalable/apps/qphotorec.svg
%endif

%files -n fidentify
%{_bindir}/fidentify
%{_mandir}/man8/fidentify*
%{_mandir}/zh_CN/man8/fidentify.8.*
