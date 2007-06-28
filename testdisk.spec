%define name    testdisk
%define version 6.7
%define rel     %mkrel 1
%define ver_e2fsprogs 1.35
%define ver_progsreiserfs 0.3.1-rc8
%define ver_ntfsprogs 1.9.4

Summary:	Tool to check and undelete partition
Summary(pl):	Narzêdzie sprawdzaj±ce i odzyskuj±ce partycje
Summary(fr):	Outil pour vérifier et restaurer des partitions
Name:		%name
Version:	%version
Release:	%rel
License:	GPL
Group:		System/Kernel and hardware
Source0:	http://www.cgsecurity.org/%{name}-%{version}.tar.bz2
Source1:	progsreiserfs-%ver_progsreiserfs.tar.bz2
Patch0:		progsreiserfs-journal.patch
URL:		http://www.cgsecurity.org/wiki/TestDisk
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:  e2fsprogs-devel >= %ver_e2fsprogs
BuildRequires:  libntfs-devel >= %ver_ntfsprogs
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot


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

%description -l pl
Narzêdzie sprawdzaj±ce i odzyskujace partycje. Pracuje z partycjami:
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

%description -l fr
Outil pour vérifier et restaurer des partitions. Fonctionne avec les 
systèmes de fichiers suivants :

    * BeFS ( BeOS )
    * BSD disklabel ( FreeBSD/OpenBSD/NetBSD )
    * CramFS (Compressed File System)
    * DOS/Windows FAT12, FAT16 and FAT32
    * HFS et HFS+, Hierarchical File System
    * JFS, Système de fichier journalisé d'IBM
    * Linux Ext2 et Ext3
    * Linux Raid
          o RAID 1: mirroring
          o RAID 4: striped array with parity device
          o RAID 5: striped array with distributed parity information
          o RAID 6: striped array with distributed dual redundancy information 
    * Linux Swap (versions 1 et 2)
    * LVM et LVM2, Linux Logical Volume Manager
    * Netware NSS
    * NTFS ( Windows NT/2K/XP/2003 )
    * ReiserFS 3.5, 3.6 et 4
    * Sun Solaris i386 disklabel
    * UFS et UFS2 (Sun/BSD/...)
    * XFS, Système de fichier journalisé de SGI 

%prep
%setup -q -n %{name}-%{version}
%setup -q -a 1 -D -n %{name}-%{version}
%patch0

%build
(
cd progsreiserfs-%ver_progsreiserfs
%configure
sed -i s/-Werror// libreiserfs/Makefile
make
)

%configure --with-reiserfs-lib=`pwd`/progsreiserfs-%ver_progsreiserfs/libreiserfs/.libs/ --with-reiserfs-includes=`pwd`/progsreiserfs-%ver_progsreiserfs/include/
%make

%install
rm -rf $RPM_BUILD_ROOT

%make DESTDIR=$RPM_BUILD_ROOT install
#install -d $RPM_BUILD_ROOT%{_sbindir}

#install src/testdisk	$RPM_BUILD_ROOT%{_sbindir}/

rm -rf $RPM_BUILD_ROOT/%_docdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INFO INSTALL NEWS README THANKS doc/*.html doc/*.gif
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*.1.bz2
