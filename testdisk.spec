%define ver_progsreiserfs 0.3.1-rc8

Summary:	Tool to check and undelete partition
Name:		testdisk
Version:	7.0
Release:	5
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://www.cgsecurity.org/wiki/TestDisk
Source0:	http://www.cgsecurity.org/%{name}-%{version}.tar.bz2
Source1:	progsreiserfs-%{ver_progsreiserfs}.tar.bz2
Patch0:		progsreiserfs-journal.patch
# Upstream patch
Patch1:		progsreiserfs-file-read.patch
Patch2:		testdisk-7.0-progsreiserfs-0.3.1-rc8-gcc7.patch
BuildRequires:	pkgconfig(libewf)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(libntfs-3g)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(uuid)
BuildRequires:	gettext-devel

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

%prep
%setup -q -a 1
%patch0
%patch1
%patch2
%before_configure

libtoolize --force
aclocal
automake -a
autoconf

cd progsreiserfs-%{ver_progsreiserfs}
libtoolize --force
touch config.rpath
aclocal -I m4
automake -a
autoconf

%build
TOP_DIR="$PWD"
CONFIGURE_TOP=..

mkdir -p progsreiserfs-%{ver_progsreiserfs}/system
pushd progsreiserfs-%{ver_progsreiserfs}/system
%configure	--enable-shared=no \
		--enable-static=yes \
		--disable-Werror 
%make
popd

mkdir -p system
pushd system
%configure	--with-dal-lib="${TOP_DIR}/progsreiserfs-%{ver_progsreiserfs}/system/libdal/.libs/" \
		--with-reiserfs-lib="${TOP_DIR}/progsreiserfs-%{ver_progsreiserfs}/system/libreiserfs/.libs/" \
		--with-reiserfs-includes="${TOP_DIR}/progsreiserfs-%{ver_progsreiserfs}/include/" \
		--enable-shared=no \
		--enable-static=yes
%make
popd

%install
%makeinstall_std -C system

rm -r %{buildroot}%{_docdir}/%{name}/

%files
%doc AUTHORS ChangeLog INFO NEWS README THANKS
# doc/*.html
%{_bindir}/testdisk
%{_mandir}/man8/testdisk*
%{_mandir}/*/man8/testdisk*

%files -n photorec
%{_bindir}/photorec
%{_mandir}/man8/photorec*
%{_mandir}/man8/qphotorec*
%{_mandir}/*/man8/*photorec*
%{_iconsdir}/hicolor/48x48/apps/qphotorec.png
%{_iconsdir}/hicolor/scalable/apps/qphotorec.svg

%files -n fidentify
%{_bindir}/fidentify
%{_mandir}/man8/fidentify*
%{_mandir}/zh_CN/man8/fidentify.8.*
