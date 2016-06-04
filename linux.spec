Name:           linux
Version:        4.6.1
Release:        228
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v4.x/linux-4.6.1.tar.xz
Source1:        config
Source2:        installkernel
Source3:        cmdline

%define kversion %{version}-%{release}.native

BuildRequires:  bash >= 2.03
BuildRequires:  bc
BuildRequires:  binutils-dev
BuildRequires:  elfutils-dev
BuildRequires:  kmod
BuildRequires:  make >= 3.78
BuildRequires:  openssl-dev
BuildRequires:  flex
BuildRequires:  bison

# don't srip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

# Serie    00XX: mainline, CVE, bugfixes patches
Patch0001: 0001-crypto-testmgr-Add-a-flag-allowing-the-self-tests-to.patch

# Serie    01XX: Clear Linux patches
#Patch0101: 0101-init-don-t-wait-for-PS-2-at-boot.patch
Patch0102: 0102-sched-tweak-the-scheduler-to-favor-CPU-0.patch
Patch0103: 0103-kvm-silence-kvm-unhandled-rdmsr.patch
Patch0104: 0104-i8042-decrease-debug-message-level-to-info.patch
Patch0105: 0105-net-tcp-reduce-minimal-ack-time-down-from-40-msec.patch
Patch0106: 0106-init-do_mounts-recreate-dev-root.patch
Patch0107: 0107-Increase-the-ext4-default-commit-age.patch
Patch0108: 0108-silence-rapl.patch
Patch0109: 0109-pci-pme-wakeups.patch
Patch0110: 0110-ksm-wakeups.patch
Patch0111: 0111-intel_idle-tweak-cpuidle-cstates.patch
Patch0112: 0112-xattr-allow-setting-user.-attributes-on-symlinks-by-.patch
Patch0113: 0113-init_task-faster-timerslack.patch
Patch0114: 0114-KVM-x86-Add-hypercall-KVM_HC_RETURN_MEM.patch
Patch0115: 0115-fs-ext4-fsync-optimize-double-fsync-a-bunch.patch
Patch0116: 0116-overload-on-wakeup.patch
Patch0117: 0117-bootstats-add-printk-s-to-measure-boot-time-in-more-.patch
Patch0118: 0118-fix-initcall-timestamps.patch
Patch0119: 0119-smpboot-reuse-timer-calibration.patch
Patch0120: 0120-raid6-add-Kconfig-option-to-skip-raid6-benchmarking.patch
Patch0121: 0121-Initialize-ata-before-graphics.patch
Patch0122: 0122-e1000e-reduce-sleep-time.patch

# Serie    XYYY: Extra features modules
# AUFS
Patch1001: 1001-aufs-kbuild.patch
Patch1002: 1002-aufs-base.patch
Patch1003: 1003-aufs-mmap.patch
Patch1004: 1004-aufs-standalone.patch
Patch1005: 1005-aufs-driver-and-docs.patch

# DPDK 16.04 integration
Patch2001: 2001-dpdk-add-source-files.patch
Patch2002: 2002-dpdk-integrate-Kconfig-and-Makefiles.patch

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

%package vboxguest-modules
License:        GPL-2.0
Summary:        Oracle VirtualBox guest additions modules
Group:          kernel

%description vboxguest-modules
Oracle VirtualBox guest additions modules

%prep
%setup -q -n linux-4.6.1

# Serie    00XX: mainline, CVE, bugfixes patches
%patch0001 -p1

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
%patch0119 -p1
%patch0120 -p1
%patch0121 -p1
%patch0122 -p1

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

BuildKernel bzImage

%install
mkdir -p %{buildroot}/usr/sbin
install -m 755 %{SOURCE2} %{buildroot}/usr/sbin

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

InstallKernel arch/x86/boot/bzImage

rm -rf %{buildroot}/usr/lib/firmware

# Copy kernel-install script
mkdir -p %{buildroot}/usr/lib/kernel/install.d

# Erase some modules index and then re-crate them
for i in alias ccwmap dep ieee1394map inputmap isapnpmap ofmap pcimap seriomap symbols usbmap softdep devname
do
    rm -f %{buildroot}/usr/lib/modules/%{kversion}/modules.${i}*
done
rm -f %{buildroot}/usr/lib/modules/%{kversion}/modules.*.bin

# Recreate modules indices
depmod -a -b %{buildroot}/usr %{kversion}

ln -s org.clearlinux.native.%{version}-%{release} %{buildroot}/usr/lib/kernel/default-native

mkdir %{buildroot}/usr/lib/modules/%{kversion}/kernel/arch/x86/virtualbox/

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
/usr/sbin/installkernel

%files extra
%dir /usr/lib/kernel
/usr/lib/kernel/System.map-%{kversion}

%files vboxguest-modules
%dir /usr/lib/modules/%{kversion}/kernel/arch/x86/virtualbox/
