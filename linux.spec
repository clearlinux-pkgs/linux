Name:           linux
Version:        4.5.4
Release:        208
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v4.x/linux-4.5.4.tar.xz
Source1:        config
Source2:        installkernel
Source3:        cmdline

%define kversion %{version}-%{release}.native

BuildRequires:  bash >= 2.03
BuildRequires:  bc
# For bfd support in perf/trace
BuildRequires:  binutils-dev
BuildRequires:  elfutils
BuildRequires:  elfutils-dev
BuildRequires:  kmod
BuildRequires:  make >= 3.78
BuildRequires:  openssl
BuildRequires:  openssl-dev
BuildRequires:  flex bison
BuildRequires:  ncurses-dev
BuildRequires:  binutils-dev
BuildRequires:  slang-dev
BuildRequires:  libunwind-dev
BuildRequires:  python-dev
BuildRequires:  zlib-dev
BuildRequires:  xz-dev
BuildRequires:  numactl-dev
BuildRequires:  perl

# don't srip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

# Serie    00XX: mainline, CVE, bugfixes patches
# GCC 6 fix
Patch0001: 0001-perf-pmu-Fix-misleadingly-indented-assignment-whites.patch
Patch0002: 0002-perf-tools-Fix-unused-variables-x86_-32-64-_regoffse.patch

# Serie    01XX: Clear Linux patches
#Patch0101: 0101-init-don-t-wait-for-PS-2-at-boot.patch
Patch0102: 0102-sched-tweak-the-scheduler-to-favor-CPU-0.patch
Patch0103: 0103-kvm-silence-kvm-unhandled-rdmsr.patch
Patch0104: 0104-i8042-decrease-debug-message-level-to-info.patch
Patch0105: 0105-raid6-reduce-boot-time.patch
Patch0106: 0106-net-tcp-reduce-minimal-ack-time-down-from-40-msec.patch
Patch0107: 0107-init-do_mounts-recreate-dev-root.patch
Patch0108: 0108-Increase-the-ext4-default-commit-age.patch
Patch0109: 0109-silence-rapl.patch
Patch0110: 0110-pci-pme-wakeups.patch
Patch0111: 0111-ksm-wakeups.patch
Patch0112: 0112-intel_idle-tweak-cpuidle-cstates.patch
Patch0113: 0113-xattr-allow-setting-user.-attributes-on-symlinks-by-.patch
Patch0114: 0114-init_task-faster-timerslack.patch
Patch0115: 0115-KVM-x86-Add-hypercall-KVM_HC_RETURN_MEM.patch
Patch0116: 0116-Script-for-building-uvcvideo.ko.patch
Patch0117: 0117-fs-ext4-fsync-optimize-double-fsync-a-bunch.patch
Patch0118: 0118-overload-on-wakeup.patch

# Serie    XYYY: Extra features modules
# AUFS
Patch1001: 1001-aufs4-kbuild.patch
Patch1002: 1002-aufs-base.patch
Patch1003: 1003-aufs-mmap.patch
Patch1004: 1004-aufs-standalone.patch
Patch1005: 1005-aufs-driver-and-docs.patch

# DPDK 16.04 integration
Patch2001: 2001-dpdk-add-source-files.patch
Patch2002: 2002-dpdk-integrate-Kconfig-and-Makefiles.patch

# virtualbox modules
Patch3001: 3001-virtualbox-add-module-sources.patch
Patch3002: 3002-virtualbox-add-Kconfs-and-Makefiles.patch

%description
The Linux kernel.

%package dev
License:        GPL-2.0
Summary:        The Linux kernel
Group:          kernel

%description dev
Linux kernel install script

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel

%description extra
Linux kernel extra files

%package tools
License:        GPL-2.0
Summary:        The Linux kernel tools (perf)
Group:          kernel

%description tools
The Linux kernel tools perf/trace.

%package vboxguest-modules
License:        GPL-2.0
Summary:        Oracle VirtualBox guest additions modules
Group:          kernel

%description vboxguest-modules
Oracle VirtualBox guest additions modules

%prep
%setup -q -n linux-4.5.4

# Serie    00XX: mainline, CVE, bugfixes patches
# GCC 6 fix
%patch0001 -p1
%patch0002 -p1

# Serie    01XX: Clear Linux patches
#%patch0101 -p1
%patch0102 -p1
%patch0103 -p1
%patch0104 -p1
%patch0105 -p1
%patch0106 -p1
%patch0107 -p1
%patch0108 -p1
%patch0109 -p1
%patch0110 -p1
%patch0111 -p1
%patch0112 -p1
%patch0113 -p1
%patch0114 -p1
%patch0115 -p1
%patch0116 -p1
%patch0117 -p1
%patch0118 -p1

# Serie    XYYY: Extra features modules
# AUFS
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1

# DPDK 16.04 integration
%patch2001 -p1
%patch2002 -p1

# virtualbox modules
%patch3001 -p1
%patch3002 -p1

cp %{SOURCE1} .

%build
BuildKernel() {
    MakeTarget=$1

    Arch=x86_64
    ExtraVer="-%{release}.native"

    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile

    make -s mrproper
    cp config .config

    make -s ARCH=$Arch oldconfig > /dev/null
    make -s CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} ARCH=$Arch $MakeTarget %{?sparse_mflags}
    make -s CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} ARCH=$Arch modules %{?sparse_mflags} || exit 1
}

BuildTools() {
    pushd tools/perf
    sed -i '/# Define NO_GTK2/a NO_GTK2 = 1' Makefile.perf
    # TODO: Fix me
    # error message: ld: XXX.o: plugin needed to handle lto object
    sed -i '/# Define NO_LIBPYTHON/a NO_LIBPYTHON = 1' Makefile.perf
    make -s %{?sparse_mflags}
    popd
    pushd tools/power/x86/turbostat
    make
    popd
}

BuildKernel bzImage

BuildTools

%install
mkdir -p %{buildroot}/sbin
install -m 755 %{SOURCE2} %{buildroot}/sbin

InstallKernel() {
    KernelImage=$1

    Arch=x86_64
    KernelVer=%{kversion}
    KernelDir=%{buildroot}/usr/lib/kernel

    mkdir   -p ${KernelDir}
    install -m 644 .config    ${KernelDir}/config-${KernelVer}
    install -m 644 System.map ${KernelDir}/System.map-${KernelVer}
    install -m 644 %{SOURCE3} ${KernelDir}/cmdline-${KernelVer}
    cp  $KernelImage ${KernelDir}/org.clearlinux.native.%{version}-%{release}
    chmod 755 ${KernelDir}/org.clearlinux.native.%{version}-%{release}

    mkdir -p %{buildroot}/usr/lib/modules/$KernelVer
    make -s ARCH=$Arch INSTALL_MOD_PATH=%{buildroot}/usr modules_install KERNELRELEASE=$KernelVer

    rm -f %{buildroot}/usr/lib/modules/$KernelVer/build
    rm -f %{buildroot}/usr/lib/modules/$KernelVer/source
}

InstallTools() {
    pushd tools/perf
    %make_install prefix=/usr
    popd
    pushd tools/power/x86/turbostat
    %make_install prefix=/usr
    popd
}

InstallKernel arch/x86/boot/bzImage
InstallTools

rm -rf %{buildroot}/usr/lib/firmware

# Copy kernel-install script
mkdir -p %{buildroot}/usr/lib/kernel/install.d

# Move bash-completion
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_sysconfdir}/bash_completion.d/perf %{buildroot}%{_datadir}/bash-completion/completions/perf
rmdir %{buildroot}%{_sysconfdir}/bash_completion.d
rmdir %{buildroot}%{_sysconfdir}

# Erase some modules index and then re-crate them
for i in alias ccwmap dep ieee1394map inputmap isapnpmap ofmap pcimap seriomap symbols usbmap softdep devname
do
    rm -f %{buildroot}/usr/lib/modules/%{kversion}/modules.${i}*
done
rm -f %{buildroot}/usr/lib/modules/%{kversion}/modules.*.bin

# Recreate modules indices
depmod -a -b %{buildroot}/usr %{kversion}

ln -s org.clearlinux.native.%{version}-%{release} %{buildroot}/usr/lib/kernel/default-native

%files
%dir /usr/lib/kernel
%exclude  /usr/lib/modules/%{kversion}/kernel/arch/x86/virtualbox/
%dir /usr/lib/modules/%{kversion}
/usr/lib/kernel/config-%{kversion}
/usr/lib/kernel/cmdline-%{kversion}
/usr/lib/kernel/org.clearlinux.native.%{version}-%{release}
/usr/lib/kernel/default-native
/usr/lib/modules/%{kversion}/kernel
/usr/lib/modules/%{kversion}/modules.*

%files dev
%defattr(-,root,root)
/usr/bin/installkernel

%files extra
%dir /usr/lib/kernel
/usr/lib/kernel/System.map-%{kversion}

%files tools
%{_bindir}/trace
%{_bindir}/perf
/usr/libexec/perf-core
/usr/lib64/traceevent/plugins/
%{_datadir}/bash-completion/completions/*
/usr/bin/turbostat
/usr/share/man/man8/turbostat.8
/usr/share/doc/perf-tip/tips.txt

%files vboxguest-modules
/usr/lib/modules/%{kversion}/kernel/arch/x86/virtualbox/
