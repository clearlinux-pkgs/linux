#
# note to self: Linus releases need to be named 4.x.0 not 4.x or various
# things break
#

Name:           linux
Version:        4.14.13
Release:        506
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v4.x/linux-4.14.13.tar.xz
Source1:        config
Source2:        cmdline
Source3:        installkernel

%define ktarget  native
%define kversion %{version}-%{release}.%{ktarget}

BuildRequires:  bash >= 2.03
BuildRequires:  bc
BuildRequires:  binutils-dev
BuildRequires:  elfutils-dev
BuildRequires:  make >= 3.78
BuildRequires:  openssl-dev
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  kmod
BuildRequires:  linux-firmware

Requires: systemd-console

# don't strip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

#    000X: cve, bugfixes patches

#    00XY: Mainline patches, upstream backports
Patch0011: 0011-libata-Add-new-med_power_with_dipm-link_power_manage.patch
Patch0012: 0012-platform-x86-intel_turbo_max_3-Add-Skylake-platform.patch

# Serie    01XX: Clear Linux patches
Patch0101: 0101-i8042-decrease-debug-message-level-to-info.patch
Patch0102: 0102-init-do_mounts-recreate-dev-root.patch
Patch0103: 0103-Increase-the-ext4-default-commit-age.patch
Patch0104: 0104-silence-rapl.patch
Patch0105: 0105-pci-pme-wakeups.patch
Patch0106: 0106-ksm-wakeups.patch
Patch0107: 0107-intel_idle-tweak-cpuidle-cstates.patch
Patch0108: 0108-xattr-allow-setting-user.-attributes-on-symlinks-by-.patch
Patch0109: 0109-init_task-faster-timerslack.patch
Patch0110: 0110-fs-ext4-fsync-optimize-double-fsync-a-bunch.patch
Patch0111: 0111-overload-on-wakeup.patch
Patch0112: 0112-bootstats-add-printk-s-to-measure-boot-time-in-more-.patch
Patch0113: 0113-fix-initcall-timestamps.patch
Patch0114: 0114-smpboot-reuse-timer-calibration.patch
Patch0115: 0115-raid6-add-Kconfig-option-to-skip-raid6-benchmarking.patch
Patch0116: 0116-Initialize-ata-before-graphics.patch
Patch0117: 0117-reduce-e1000e-boot-time-by-tightening-sleep-ranges.patch
Patch0118: 0118-give-rdrand-some-credit.patch
Patch0119: 0119-e1000e-change-default-policy.patch
Patch0120: 0120-ipv4-tcp-allow-the-memory-tuning-for-tcp-to-go-a-lit.patch
Patch0121: 0121-igb-no-runtime-pm-to-fix-reboot-oops.patch
Patch0122: 0122-tweak-perfbias.patch
Patch0123: 0123-e1000e-increase-pause-and-refresh-time.patch
Patch0124: 0124-kernel-time-reduce-ntp-wakeups.patch
Patch0125: 0125-init-wait-for-partition-and-retry-scan.patch
Patch0126: 0126-print-fsync-count-for-bootchart.patch

# Clear Linux KVM Memory Optimization
Patch0151: 0151-mm-Export-do_madvise.patch
Patch0152: 0152-x86-kvm-Notify-host-to-release-pages.patch
Patch0153: 0153-x86-Return-memory-from-guest-to-host-kernel.patch
Patch0154: 0154-sysctl-vm-Fine-grained-cache-shrinking.patch

Patch0300: 0001-x86-pti-Rename-BUG_CPU_INSECURE-to-BUG_CPU_MELTDOWN.patch
Patch0301: 0001-x86-spectre-Add-X86_BUG_SPECTRE_V-12.patch
Patch0302: 0002-x86-retpoline-Add-initial-retpoline-support.patch
Patch0303: 0003-x86-retpoline-crypto-Convert-crypto-assembler-indire.patch
Patch0304: 0004-x86-retpoline-entry-Convert-entry-assembler-indirect.patch
Patch0305: 0005-x86-retpoline-ftrace-Convert-ftrace-assembler-indire.patch
Patch0306: 0006-x86-retpoline-hyperv-Convert-assembler-indirect-jump.patch
Patch0307: 0007-x86-retpoline-xen-Convert-Xen-hypercall-indirect-jum.patch
Patch0308: 0008-x86-retpoline-checksum32-Convert-assembler-indirect-.patch
Patch0309: 0009-x86-retpoline-irq32-Convert-assembler-indirect-jumps.patch
Patch0310: 0010-x86-retpoline-Add-boot-time-option-to-disable-retpol.patch
Patch0311: 0011-x86-retpoline-Exclude-objtool-with-retpoline.patch
Patch0312: 0012-retpoline-modpost-Quieten-MODVERSION-retpoline-build.patch

Patch0400: 0001-asm-generic-barrier-add-generic-nospec-helpers.patch
Patch0401: 0001-Documentation-document-nospec-helpers.patch
Patch0402: 0002-arm64-implement-nospec_ptr.patch
Patch0403: 0003-arm-implement-nospec_ptr.patch
Patch0404: 0004-x86-implement-nospec_barrier.patch
Patch0405: 0005-x86-barrier-stop-speculation-for-failed-access_ok.patch
Patch0406: 0006-media-uvcvideo-prevent-bounds-check-bypass-via-specu.patch
Patch0407: 0007-carl9170-prevent-bounds-check-bypass-via-speculative.patch
Patch0408: 0008-p54-prevent-bounds-check-bypass-via-speculative-exec.patch
Patch0409: 0009-qla2xxx-prevent-bounds-check-bypass-via-speculative-.patch
Patch0410: 0010-cw1200-prevent-bounds-check-bypass-via-speculative-e.patch
Patch0411: 0011-Thermal-int340x-prevent-bounds-check-bypass-via-spec.patch
Patch0412: 0012-ipv6-prevent-bounds-check-bypass-via-speculative-exe.patch
Patch0413: 0013-ipv4-prevent-bounds-check-bypass-via-speculative-exe.patch
Patch0414: 0014-vfs-fdtable-prevent-bounds-check-bypass-via-speculat.patch
Patch0415: 0015-net-mpls-prevent-bounds-check-bypass-via-speculative.patch
Patch0416: 0016-udf-prevent-bounds-check-bypass-via-speculative-exec.patch
Patch0418: 0001-bpf-prevent-out-of-bounds-speculation.patch


# Serie    XYYY: Extra features modules
#    100X: Accelertor Abstraction Layer (AAL)
Patch1001: 1001-fpga-add-AAL-6.3.1.patch
Patch1002: 1002-fpga-add-AAL-to-fpga-Kconfig-and-Makefile.patch
Patch1003: 1003-fix-aal-for-4.14.patch

#    200X: Open Programmable Acceleration Engine (OPAE)
Patch2001: 2001-opae-add-intel-fpga-drivers.patch
Patch2002: 2002-opae-add-Kconfig.patch

%description
The Linux kernel.

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel

%description extra
Linux kernel extra files

%package dev
License:        GPL-2.0
Summary:        The Linux kernel
Group:          kernel

%description dev
Linux kernel install script

%prep
%setup -q -n linux-4.14.13

#     000X  cve, bugfixes patches

#     00XY  Mainline patches, upstream backports
%patch0011 -p1
%patch0012 -p1

#     01XX  Clear Linux patches
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
%patch0123 -p1
%patch0124 -p1
%patch0125 -p1
%patch0126 -p1

# Clear Linux KVM Memory Optimization
%patch0151 -p1
%patch0152 -p1
%patch0153 -p1
%patch0154 -p1

%patch0300 -p1
%patch0301 -p1
%patch0302 -p1
%patch0303 -p1
%patch0304 -p1
%patch0305 -p1
%patch0306 -p1
%patch0307 -p1
%patch0308 -p1
%patch0309 -p1
%patch0310 -p1
%patch0311 -p1
%patch0312 -p1

%patch0400 -p1
%patch0401 -p1
%patch0402 -p1
%patch0403 -p1
%patch0404 -p1
%patch0405 -p1
%patch0406 -p1
%patch0407 -p1
%patch0408 -p1
%patch0409 -p1
%patch0410 -p1
%patch0411 -p1
%patch0412 -p1
%patch0413 -p1
%patch0414 -p1
%patch0415 -p1
%patch0416 -p1
%patch0418 -p1

# Serie    XYYY: Extra features modules
#     100X  Accelertor Abstraction Layer (AAL)
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1

#    200X: Open Programmable Acceleration Engine (OPAE)
%patch2001 -p1
%patch2002 -p1

cp %{SOURCE1} .

cp -a /usr/lib/firmware/i915 firmware/
cp -a /usr/lib/firmware/intel-ucode firmware/

%build
BuildKernel() {

    Target=$1
    Arch=x86_64
    ExtraVer="-%{release}.${Target}"

    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile

    make O=${Target} -s mrproper
    cp config ${Target}/.config

    make O=${Target} -s ARCH=${Arch} olddefconfig
    make O=${Target} -s ARCH=${Arch} CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} %{?sparse_mflags}
}

BuildKernel %{ktarget}

%install
mkdir -p %{buildroot}/usr/sbin
install -m 755 %{SOURCE3} %{buildroot}/usr/sbin

InstallKernel() {

    Target=$1
    Kversion=$2
    Arch=x86_64
    KernelDir=%{buildroot}/usr/lib/kernel

    mkdir   -p ${KernelDir}
    install -m 644 ${Target}/.config    ${KernelDir}/config-${Kversion}
    install -m 644 ${Target}/System.map ${KernelDir}/System.map-${Kversion}
    install -m 644 ${Target}/vmlinux    ${KernelDir}/vmlinux-${Kversion}
    install -m 644 %{SOURCE2}           ${KernelDir}/cmdline-${Kversion}
    cp  ${Target}/arch/x86/boot/bzImage ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}
    chmod 755 ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}

    mkdir -p %{buildroot}/usr/lib/modules
    make O=${Target} -s ARCH=${Arch} INSTALL_MOD_PATH=%{buildroot}/usr modules_install

    rm -f %{buildroot}/usr/lib/modules/${Kversion}/build
    rm -f %{buildroot}/usr/lib/modules/${Kversion}/source

    ln -s org.clearlinux.${Target}.%{version}-%{release} %{buildroot}/usr/lib/kernel/default-${Target}
}

InstallKernel %{ktarget}  %{kversion}

rm -rf %{buildroot}/usr/lib/firmware

%files
%dir /usr/lib/kernel
%dir /usr/lib/modules/%{kversion}
/usr/lib/kernel/config-%{kversion}
/usr/lib/kernel/cmdline-%{kversion}
/usr/lib/kernel/org.clearlinux.%{ktarget}.%{version}-%{release}
/usr/lib/kernel/default-%{ktarget}
/usr/lib/modules/%{kversion}/kernel
/usr/lib/modules/%{kversion}/modules.*

%files extra
%dir /usr/lib/kernel
/usr/lib/kernel/System.map-%{kversion}
/usr/lib/kernel/vmlinux-%{kversion}

%files dev
%defattr(-,root,root)
/usr/sbin/installkernel
