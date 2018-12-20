#
# note to self: Linus releases need to be named 4.x.0 not 4.x or various
# things break
#

Name:           linux
Version:        4.19.11
Release:        673
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.19.11.tar.xz
Source1:        config
Source2:        cmdline

%define ktarget  native
%define kversion %{version}-%{release}.%{ktarget}

BuildRequires:  buildreq-kernel

Requires: systemd-bin
Requires: init-rdahead-extras

# don't strip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

#    000X: cve, bugfixes patches


#    00XY: Mainline patches, upstream backports
Patch0010: 0010-drm-i915-cfl-Add-a-new-CFL-PCI-ID.patch

# Serie    01XX: Clear Linux patches
Patch0101: 0101-i8042-decrease-debug-message-level-to-info.patch
Patch0102: 0102-Increase-the-ext4-default-commit-age.patch
Patch0103: 0103-silence-rapl.patch
Patch0104: 0104-pci-pme-wakeups.patch
Patch0105: 0105-ksm-wakeups.patch
Patch0106: 0106-intel_idle-tweak-cpuidle-cstates.patch
Patch0107: 0107-bootstats-add-printk-s-to-measure-boot-time-in-more-.patch
Patch0108: 0108-smpboot-reuse-timer-calibration.patch
Patch0109: 0109-raid6-add-Kconfig-option-to-skip-raid6-benchmarking.patch
Patch0110: 0110-Initialize-ata-before-graphics.patch
Patch0111: 0111-reduce-e1000e-boot-time-by-tightening-sleep-ranges.patch
Patch0112: 0112-give-rdrand-some-credit.patch
Patch0113: 0113-ipv4-tcp-allow-the-memory-tuning-for-tcp-to-go-a-lit.patch
Patch0114: 0114-tweak-perfbias.patch
Patch0115: 0115-e1000e-increase-pause-and-refresh-time.patch
Patch0116: 0116-kernel-time-reduce-ntp-wakeups.patch
Patch0117: 0117-init-wait-for-partition-and-retry-scan.patch
Patch0118: 0118-print-fsync-count-for-bootchart.patch
Patch0119: 0119-Add-boot-option-to-allow-unsigned-modules.patch
Patch0120: 0120-Enable-stateless-firmware-loading.patch
Patch0121: 0121-Migrate-some-systemd-defaults-to-the-kernel-defaults.patch
Patch0122: 0122-xattr-allow-setting-user.-attributes-on-symlinks-by-.patch
Patch0124: turbo3-scheduler.patch

Patch0125: lfence.patch
Patch0126: lifo-accept.patch
#
# Small Clear Linux Tweaks
#
Patch0501: 0501-zero-extra-registers.patch
Patch0502: 0502-locking-rwsem-spin-faster.patch

#Serie1.name WireGuard
#Serie1.git  https://git.zx2c4.com/WireGuard
#Serie1.tag  00bf4f8c8c0ec006633a48fd9ee746b30bb9df17
Patch1001: 1001-WireGuard-fast-modern-secure-kernel-VPN-tunnel.patch
#Serie1.end

%description
The Linux kernel.

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel

%description extra
Linux kernel extra files

%package cpio
License:        GPL-2.0
Summary:        cpio file with kenrel modules
Group:          kernel

%description cpio
Creates a cpio file with i8042 module

%package dev
License:        GPL-2.0
Summary:        The Linux kernel
Group:          kernel
Requires:       %{name} = %{version}-%{release}, %{name}-extra = %{version}-%{release}

%description dev
Linux kernel build files and install script

%prep
%setup -q -n linux-4.19.11

#     000X  cve, bugfixes patches

#     00XY  Mainline patches, upstream backports
%patch0010 -p1

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
%patch0124 -p1
%patch0125 -p1
%patch0126 -p1

#
# Small tweaks
#
%patch0501 -p1
%patch0502 -p1

#Serie1.patch.start
%patch1001 -p1
#Serie1.patch.end

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

InstallKernel() {

    Target=$1
    Kversion=$2
    Arch=x86_64
    KernelDir=%{buildroot}/usr/lib/kernel
    DevDir=%{buildroot}/usr/lib/modules/${Kversion}/build

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

    mkdir -p ${DevDir}
    find . -type f -a '(' -name 'Makefile*' -o -name 'Kbuild*' -o -name 'Kconfig*' ')' -exec cp -t ${DevDir} --parents -pr {} +
    find . -type f -a '(' -name '*.sh' -o -name '*.pl' ')' -exec cp -t ${DevDir} --parents -pr {} +
    cp -t ${DevDir} -pr ${Target}/{Module.symvers,tools}
    ln -s ../../../kernel/config-${Kversion} ${DevDir}/.config
    ln -s ../../../kernel/System.map-${Kversion} ${DevDir}/System.map
    cp -t ${DevDir} --parents -pr arch/x86/include
    cp -t ${DevDir}/arch/x86/include -pr ${Target}/arch/x86/include/*
    cp -t ${DevDir}/include -pr include/*
    cp -t ${DevDir}/include -pr ${Target}/include/*
    cp -t ${DevDir} --parents -pr scripts/*
    cp -t ${DevDir}/scripts -pr ${Target}/scripts/*
    find  ${DevDir}/scripts -type f -name '*.[cho]' -exec rm -v {} +
    find  ${DevDir} -type f -name '*.cmd' -exec rm -v {} +
    # Cleanup any dangling links
    find ${DevDir} -type l -follow -exec rm -v {} +

    # Kernel default target link
    ln -s org.clearlinux.${Target}.%{version}-%{release} %{buildroot}/usr/lib/kernel/default-${Target}
}

# cpio file for i8042 libps2 atkbd
createCPIO() {

    Target=$1
    Kversion=$2
    KernelDir=%{buildroot}/usr/lib/kernel
    ModDir=/usr/lib/modules/${Kversion}

    mkdir -p cpiofile${ModDir}/kernel/drivers/input/{serio,keyboard}
    cp %{buildroot}${ModDir}/kernel/drivers/input/serio/i8042.ko    cpiofile${ModDir}/kernel/drivers/input/serio
    cp %{buildroot}${ModDir}/kernel/drivers/input/serio/libps2.ko   cpiofile${ModDir}/kernel/drivers/input/serio
    cp %{buildroot}${ModDir}/kernel/drivers/input/keyboard/atkbd.ko cpiofile${ModDir}/kernel/drivers/input/keyboard
    cp %{buildroot}${ModDir}/modules.order   cpiofile${ModDir}
    cp %{buildroot}${ModDir}/modules.builtin cpiofile${ModDir}

    depmod -b cpiofile/usr ${Kversion}

    (
      cd cpiofile
      find . | cpio --create --format=newc \
        | xz --check=crc32 --lzma2=dict=512KiB > ${KernelDir}/initrd-org.clearlinux.${Target}.%{version}-%{release}
    )
}

InstallKernel %{ktarget} %{kversion}

createCPIO %{ktarget} %{kversion}

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

%files cpio
/usr/lib/kernel/initrd-org.clearlinux.%{ktarget}.%{version}-%{release}

%files dev
%defattr(-,root,root)
/usr/lib/modules/%{kversion}/build
