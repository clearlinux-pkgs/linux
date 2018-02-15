#
# note to self: Linus releases need to be named 4.x.0 not 4.x or various
# things break
#

Name:           linux
Version:        4.15.3
Release:        529
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v4.x/linux-4.15.3.tar.xz
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
Patch0001: 0001-drm-i915-Update-watermark-state-correctly-in-sanitiz.patch

#    00XY: Mainline patches, upstream backports

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

#
# Upstream backports
#
Patch0201: 0001-ima-Use-i_version-only-when-filesystem-supports-it.patch
Patch0202: 0002-lustre-don-t-set-f_version-in-ll_readdir.patch
Patch0203: 0003-ntfs-remove-i_version-handling.patch
Patch0204: 0004-fs-new-API-for-handling-inode-i_version.patch
Patch0205: 0005-fs-don-t-take-the-i_lock-in-inode_inc_iversion.patch
Patch0206: 0006-fat-convert-to-new-i_version-API.patch
Patch0207: 0007-affs-convert-to-new-i_version-API.patch
Patch0208: 0008-afs-convert-to-new-i_version-API.patch
Patch0209: 0009-btrfs-convert-to-new-i_version-API.patch
Patch0210: 0010-exofs-switch-to-new-i_version-API.patch
Patch0211: 0011-ext2-convert-to-new-i_version-API.patch
Patch0212: 0012-ext4-convert-to-new-i_version-API.patch
Patch0213: 0013-nfs-convert-to-new-i_version-API.patch
Patch0214: 0014-nfsd-convert-to-new-i_version-API.patch
Patch0215: 0015-ocfs2-convert-to-new-i_version-API.patch
Patch0216: 0016-ufs-use-new-i_version-API.patch
Patch0217: 0017-xfs-convert-to-new-i_version-API.patch
Patch0218: 0018-IMA-switch-IMA-over-to-new-i_version-API.patch
Patch0219: 0019-fs-only-set-S_VERSION-when-updating-times-if-necessa.patch
Patch0220: 0020-xfs-avoid-setting-XFS_ILOG_CORE-if-i_version-doesn-t.patch
Patch0221: 0021-btrfs-only-dirty-the-inode-in-btrfs_update_time-if-s.patch
Patch0222: 0022-fs-handle-inode-i_version-more-efficiently.patch
patch0223: kvm-retpoline.patch

# nospec
#Patch0401: 0401-Documentation-document-array_ptr.patch
#Patch0402: 0402-asm-nospec-array_ptr-sanitize-speculative-array-de-r.patch
#Patch0403: 0403-x86-implement-array_ptr_mask.patch
#Patch0404: 0404-x86-introduce-__uaccess_begin_nospec-and-ifence.patch
#Patch0405: 0405-x86-__get_user-use-__uaccess_begin_nospec.patch
#Patch0406: 0406-x86-get_user-use-pointer-masking-to-limit-speculatio.patch
#Patch0407: 0407-x86-narrow-out-of-bounds-syscalls-to-sys_read-under-.patch
#Patch0408: 0408-vfs-fdtable-prevent-bounds-check-bypass-via-speculat.patch
#Patch0409: 0409-kvm-x86-update-spectre-v1-mitigation.patch
#Patch0410: 0410-nl80211-sanitize-array-index-in-parse_txq_params.patch
Patch0500: zero-regs.patch
Patch0501: itmt.patch

# Serie    XYYY: Extra features modules
#    100X: Accelertor Abstraction Layer (AAL)
Patch1001: 1001-fpga-add-AAL-6.3.1.patch
Patch1002: 1002-fpga-add-AAL-to-fpga-Kconfig-and-Makefile.patch
Patch1003: 1003-fix-aal-for-4.14.patch

#    200X: Open Programmable Acceleration Engine (OPAE)
Patch2001: 2001-opae-add-intel-fpga-drivers.patch
Patch2002: 2002-opae-add-Kconfig-and-Makefile.patch

%description
The Linux kernel.

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel

%description extra
Linux kernel extra files

%package clr-init
License:        GPL-2.0
Summary:        Symlink to clr-init file
Group:          kernel

%description clr-init
Generates a symlink to the clr-init file to boot with encrypted root partion.

%package dev
License:        GPL-2.0
Summary:        The Linux kernel
Group:          kernel

%description dev
Linux kernel install script

%prep
%setup -q -n linux-4.15.3

#     000X  cve, bugfixes patches
%patch0001 -p1

#     00XY  Mainline patches, upstream backports

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

# upstream backports
%patch0201 -p1
%patch0202 -p1
%patch0203 -p1
%patch0204 -p1
%patch0205 -p1
%patch0206 -p1
%patch0207 -p1
%patch0208 -p1
%patch0209 -p1
%patch0210 -p1
%patch0211 -p1
%patch0212 -p1
%patch0213 -p1
%patch0214 -p1
%patch0215 -p1
%patch0216 -p1
%patch0217 -p1
%patch0218 -p1
%patch0219 -p1
%patch0220 -p1
%patch0221 -p1
%patch0222 -p1
%patch0223 -p1


# nospec
#%patch0401 -p1
#%patch0402 -p1
#%patch0403 -p1
#%patch0404 -p1
#%patch0405 -p1
#%patch0406 -p1
#%patch0407 -p1
#%patch0408 -p1
#%patch0409 -p1
#%patch0410 -p1

%patch0500 -p1
%patch0501 -p1

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
    ln -s clr-init.img.gz %{buildroot}/usr/lib/kernel/initrd-org.clearlinux.${Target}.%{version}-%{release}
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

%files clr-init
%dir /usr/lib/kernel
/usr/lib/kernel/initrd-org.clearlinux.%{ktarget}.%{version}-%{release}

%files dev
%defattr(-,root,root)
/usr/sbin/installkernel
