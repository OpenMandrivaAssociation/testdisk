%define name    testdisk
%define version 6.6
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
partitions:
- FAT12 FAT16 FAT32
- Linux
- Linux SWAP (version 1 and 2)
- NTFS (Windows NT/W2K/XP)
- BeFS (BeOS)
- UFS (BSD)
- Netware
- ReiserFS

%description -l pl
Narzêdzie sprawdzaj±ce i odzyskujace partycje. Pracuje z partycjami:
- FAT12 FAT16 FAT32
- Linux
- Linux SWAP (version 1 and 2)
- NTFS (Windows NT/W2K/XP)
- BeFS (BeOS)
- UFS (BSD)
- Netware
- ReiserFS

%description -l fr
Outil pour vérifier et restaurer des partitions. Fonctionne avec les 
partitions suivantes :
- FAT12 FAT16 FAT32
- Linux
- Linux SWAP (version 1 et 2)
- NTFS (Windows NT/W2K/XP)
- BeFS (BeOS)
- UFS (BSD)
- Netware
- ReiserFS

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


