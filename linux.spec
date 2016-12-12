Name:           linux
# note to self: Linus releases need to be named 4.x.0 not 4.x or various
# things break
Version:        4.8.12
Release:        286
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        http://www.kernel.org/pub/linux/kernel/v4.x/linux-4.8.12.tar.xz
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
# Upstream 4.9-rc1
Patch0001: 0001-x86-asm-head-Remove-unused-init_rsp-variable-extern.patch
Patch0002: 0002-ACPI-CPPC-restructure-read-writes-for-efficient-sys-.patch
Patch0003: 0003-ACPI-CPPC-acquire-pcc_lock-only-while-accessing-PCC-.patch
Patch0004: 0004-ACPI-CPPC-support-for-batching-CPPC-requests.patch
Patch0005: 0005-ACPI-CPPC-set-a-non-zero-value-for-transition_latenc.patch
Patch0006: 0006-ACPI-CPPC-add-sysfs-support-to-compute-delivered-per.patch
Patch0007: 0007-ACPI-CPPC-move-all-PCC-related-information-into-pcc_.patch
Patch0008: 0008-ACPI-CPPC-check-for-error-bit-in-PCC-status-field.patch
Patch0009: 0009-ACPI-CPPC-Allow-build-with-ACPI_CPU_FREQ_PSS-config.patch
Patch0010: 0010-ACPI-CPPC-Don-t-return-on-CPPC-probe-failure.patch
Patch0011: 0011-ACPI-CPPC-Add-support-for-functional-fixed-hardware-.patch
Patch0012: 0012-ACPI-CPPC-Add-prefix-cppc-to-cpudata-structure-name.patch
Patch0013: 0013-ACPI-CPPC-Support-PCC-with-interrupt-flag.patch
# [PATCH v6 14-22] Support Intel® Turbo Boost Max Technology 3.0
Patch0014: 0014-sched-Extend-scheduler-s-asym-packing.patch
Patch0015: 0015-x86-topology-Provide-topology_num_packages.patch
Patch0016: 0016-x86-topology-Define-x86-s-arch_update_cpu_topology.patch
Patch0017: 0017-x86-Enable-Intel-Turbo-Boost-Max-Technology-3.0.patch
Patch0018: 0018-x86-sysctl-Add-sysctl-for-ITMT-scheduling-feature.patch
Patch0019: 0019-x86-sched-Add-SD_ASYM_PACKING-flags-to-x86-ITMT-CPU.patch
Patch0020: 0020-acpi-bus-Enable-HWP-CPPC-objects.patch
Patch0021: 0021-acpi-bus-Set-_OSC-for-diverse-core-support.patch
Patch0022: 0022-cpufreq-intel_pstate-Use-CPPC-to-get-max-performance.patch
# [ END ] Support Intel® Turbo Boost Max Technology 3.0
Patch0023: 0023-locking-static_keys-Provide-DECLARE-and-well-as-DEFI.patch

# [PATCH tip/x86/cache] Intel Cache Allocation Technology
# https://marc.info/?l=linux-kernel&m=147714255129238&w=2
Patch0041: 0041-Documentation-ABI-Document-the-new-sysfs-files-for-c.patch
Patch0042: 0042-cacheinfo-Introduce-cache-id.patch
Patch0043: 0043-x86-intel_cacheinfo-Enable-cache-id-in-cache-info.patch
Patch0044: 0044-x86-cpufeature-Add-RDT-CPUID-feature-bits.patch
Patch0045: 0045-x86-intel_rdt-Add-CONFIG-Makefile-and-basic-initiali.patch
Patch0046: 0046-x86-intel_rdt-Add-Haswell-feature-discovery.patch
Patch0047: 0047-x86-intel_rdt-Pick-up-L3-L2-RDT-parameters-from-CPUI.patch
Patch0048: 0048-x86-cqm-Share-PQR_ASSOC-related-data-between-CQM-and.patch
Patch0049: 0049-Documentation-x86-Documentation-for-Intel-resource-a.patch
Patch0050: 0050-x86-intel_rdt-Build-structures-for-each-resource-bas.patch
Patch0051: 0051-x86-intel_rdt-Add-basic-resctrl-filesystem-support.patch
Patch0052: 0052-x86-intel_rdt-Add-info-files-to-resctrl-file-system.patch
Patch0053: 0053-x86-intel_rdt-Add-mkdir-to-resctrl-file-system.patch
Patch0054: 0054-x86-intel_rdt-Add-cpus-file.patch
Patch0055: 0055-x86-intel_rdt-Add-tasks-files.patch
Patch0056: 0056-x86-intel_rdt-Add-schemata-file.patch
Patch0057: 0057-x86-intel_rdt-Add-scheduler-hook.patch
Patch0058: 0058-MAINTAINERS-Add-maintainer-for-Intel-RDT-resource-al.patch
Patch0059: 0059-x86-intel_rdt-Add-a-missing-include.patch
Patch0060: 0060-x86-intel_rdt-Propagate-error-in-rdt_mount-properly.patch
Patch0061: 0061-x86-intel_rdt-Export-the-minimum-number-of-set-mask-.patch
Patch0062: 0062-x86-intel_rdt-Add-info-files-to-Documentation.patch

Patch0071: cve-2016-8632.patch
Patch0073: cve-2016-9083.patch
Patch0074: cve-2016-9084.nopatch
Patch0075: cve-2016-8655.patch
Patch0076: cve-2016-9919.patch

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
Patch0122: e1000e-change-default-policy.patch

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
%setup -q -n linux-4.8.12

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
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1

# [PATCH tip/x86/cache] Intel Cache Allocation Technology
%patch0041 -p1
%patch0042 -p1
%patch0043 -p1
%patch0044 -p1
%patch0045 -p1
%patch0046 -p1
%patch0047 -p1
%patch0048 -p1
%patch0049 -p1
%patch0050 -p1
%patch0051 -p1
%patch0052 -p1
%patch0053 -p1
%patch0054 -p1
%patch0055 -p1
%patch0056 -p1
%patch0057 -p1
%patch0058 -p1
%patch0059 -p1
%patch0060 -p1
%patch0061 -p1
%patch0062 -p1

%patch0071 -p1
%patch0073 -p1
#%patch0074 -p1 No patch, same as 73
%patch0075 -p1
%patch0076 -p1

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
%patch0122 -p1

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
