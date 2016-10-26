Name:           linux
# note to self: Linus releases need to be named 4.x.0 not 4.x or various
# things break
Version:        4.8.4
Release:        269
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        http://www.kernel.org/pub/linux/kernel/v4.x/linux-4.8.4.tar.xz
Source1:        config
Source2:        cmdline
Source3:        installkernel

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
# [PATCH v6 0/9] Support Intel® Turbo Boost Max Technology 3.0
Patch0001: 0001-sched-Extend-scheduler-s-asym-packing.patch
Patch0002: 0002-x86-topology-Provide-topology_num_packages.patch
Patch0003: 0003-x86-topology-Define-x86-s-arch_update_cpu_topology.patch
Patch0004: 0004-x86-Enable-Intel-Turbo-Boost-Max-Technology-3.0.patch
Patch0005: 0005-x86-sysctl-Add-sysctl-for-ITMT-scheduling-feature.patch
Patch0006: 0006-x86-sched-Add-SD_ASYM_PACKING-flags-to-x86-ITMT-CPU.patch
Patch0007: 0007-acpi-bus-Enable-HWP-CPPC-objects.patch
Patch0008: 0008-acpi-bus-Set-_OSC-for-diverse-core-support.patch
Patch0009: 0009-cpufreq-intel_pstate-Use-CPPC-to-get-max-performance.patch
# Alredy in upstream 4.9-rc1
Patch0010: 0010-ACPI-CPPC-Allow-build-with-ACPI_CPU_FREQ_PSS-config.patch
Patch0011: 0011-ACPI-CPPC-Don-t-return-on-CPPC-probe-failure.patch
Patch0012: 0012-ACPI-CPPC-Add-support-for-functional-fixed-hardware-.patch
Patch0013: 0013-ACPI-CPPC-Add-prefix-cppc-to-cpudata-structure-name.patch

# Serie    01XX: Clear Linux patches
Patch0101: 0101-kvm-silence-kvm-unhandled-rdmsr.patch
Patch0102: 0102-i8042-decrease-debug-message-level-to-info.patch
Patch0103: 0103-init-do_mounts-recreate-dev-root.patch
Patch0104: 0104-Increase-the-ext4-default-commit-age.patch
Patch0105: 0105-silence-rapl.patch
Patch0106: 0106-pci-pme-wakeups.patch
Patch0107: 0107-ksm-wakeups.patch
Patch0108: 0108-intel_idle-tweak-cpuidle-cstates.patch
Patch0109: 0109-xattr-allow-setting-user.-attributes-on-symlinks-by-.patch
Patch0110: 0110-init_task-faster-timerslack.patch
Patch0111: 0111-KVM-x86-Add-hypercall-KVM_HC_RETURN_MEM.patch
Patch0112: 0112-fs-ext4-fsync-optimize-double-fsync-a-bunch.patch
Patch0113: 0113-overload-on-wakeup.patch
Patch0114: 0114-bootstats-add-printk-s-to-measure-boot-time-in-more-.patch
Patch0115: 0115-fix-initcall-timestamps.patch
Patch0116: 0116-smpboot-reuse-timer-calibration.patch
Patch0117: 0117-raid6-add-Kconfig-option-to-skip-raid6-benchmarking.patch
Patch0118: 0118-Initialize-ata-before-graphics.patch
Patch0119: 0119-reduce-e1000e-boot-time-by-tightening-sleep-ranges.patch
Patch0120: 0120-xor-skip-benchmark-allocations-for-short-circuit-pat.patch
Patch0121: 0121-give-rdrand-some-credit.patch

# Serie    XYYY: Extra features modules
# DPDK 16.04 integration
Patch1001: 1001-dpdk-add-source-files.patch
Patch1002: 1002-dpdk-integrate-Kconfig-and-Makefiles.patch
Patch1003: 1003-kni-fix-build-with-kernel-4.7.patch

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

%prep
%setup -q -n linux-4.8.4

# Serie    00XX: mainline, CVE, bugfixes patches
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1

# Serie    01XX: Clear Linux patches
%patch0101 -p1
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

# Serie    XYYY: Extra features modules
# DPDK 16.04 integration
#%patch1001 -p1
#%patch1002 -p1
#%patch1003 -p1

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
    make -s CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} ARCH=$Arch %{?sparse_mflags}
}

BuildKernel bzImage

%install
mkdir -p %{buildroot}/usr/sbin
install -m 755 %{SOURCE3} %{buildroot}/usr/sbin

InstallKernel() {
    KernelImage=$1

    Arch=x86_64
    KernelVer=%{kversion}
    KernelDir=%{buildroot}/usr/lib/kernel

    mkdir   -p ${KernelDir}
    install -m 644 .config    ${KernelDir}/config-${KernelVer}
    install -m 644 System.map ${KernelDir}/System.map-${KernelVer}
    install -m 644 %{SOURCE2} ${KernelDir}/cmdline-${KernelVer}
    cp  $KernelImage ${KernelDir}/org.clearlinux.native.%{version}-%{release}
    chmod 755 ${KernelDir}/org.clearlinux.native.%{version}-%{release}

    mkdir -p %{buildroot}/usr/lib/modules/$KernelVer
    make -s ARCH=$Arch INSTALL_MOD_PATH=%{buildroot}/usr modules_install KERNELRELEASE=$KernelVer

    rm -f %{buildroot}/usr/lib/modules/$KernelVer/build
    rm -f %{buildroot}/usr/lib/modules/$KernelVer/source
}

InstallKernel arch/x86/boot/bzImage

rm -rf %{buildroot}/usr/lib/firmware

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
