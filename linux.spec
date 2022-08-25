#
# note to self: Linus releases need to be named 5.x.0 not 5.x or various
# things break
#
#

Name:           linux
Version:        5.19.4
Release:        1181
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.19.4.tar.xz
Source1:        config
Source2:        cmdline

%define ktarget  native
%define kversion %{version}-%{release}.%{ktarget}

BuildRequires:  buildreq-kernel

Requires: systemd-bin
Requires: init-rdahead-extras
Requires: linux-license = %{version}-%{release}

# don't strip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

#cve.start cve patches from 0001 to 050
#cve.end

#mainline: Mainline patches, upstream backport and fixes from 0051 to 0099
#mainline.end

#Serie.clr 01XX: Clear Linux patches
Patch0101: 0101-i8042-decrease-debug-message-level-to-info.patch
Patch0102: 0102-increase-the-ext4-default-commit-age.patch
Patch0103: 0103-silence-rapl.patch
Patch0104: 0104-pci-pme-wakeups.patch
Patch0105: 0105-ksm-wakeups.patch
Patch0106: 0106-intel_idle-tweak-cpuidle-cstates.patch
Patch0107: 0107-bootstats-add-printk-s-to-measure-boot-time-in-more-.patch
Patch0108: 0108-smpboot-reuse-timer-calibration.patch
Patch0109: 0109-initialize-ata-before-graphics.patch
Patch0111: 0111-ipv4-tcp-allow-the-memory-tuning-for-tcp-to-go-a-lit.patch
Patch0112: 0112-init-wait-for-partition-and-retry-scan.patch
Patch0113: 0113-print-fsync-count-for-bootchart.patch
Patch0114: 0114-add-boot-option-to-allow-unsigned-modules.patch
Patch0115: 0115-enable-stateless-firmware-loading.patch
Patch0116: 0116-migrate-some-systemd-defaults-to-the-kernel-defaults.patch
Patch0117: 0117-xattr-allow-setting-user.-attributes-on-symlinks-by-.patch
Patch0118: 0118-add-scheduler-turbo3-patch.patch
Patch0119: 0119-use-lfence-instead-of-rep-and-nop.patch
Patch0120: 0120-do-accept-in-LIFO-order-for-cache-efficiency.patch
Patch0121: 0121-locking-rwsem-spin-faster.patch
Patch0122: 0122-ata-libahci-ignore-staggered-spin-up.patch
Patch0123: 0123-print-CPU-that-faults.patch
Patch0124: 0124-x86-microcode-Add-an-option-to-reload-microcode-even.patch
Patch0125: 0125-nvme-workaround.patch
Patch0126: 0126-don-t-report-an-error-if-PowerClamp-run-on-other-CPU.patch
Patch0127: 0127-lib-raid6-add-patch.patch
Patch0128: 0128-itmt_epb-use-epb-to-scale-itmt.patch
Patch0130: 0130-itmt2-ADL-fixes.patch
Patch0131: 0131-add-a-per-cpu-minimum-high-watermark-an-tune-batch-s.patch
Patch0132: 0132-prezero-20220308.patch
Patch0133: 0133-novector.patch
Patch0134: scale.patch
Patch0135: libsgrowdown.patch
Patch0136: kdf-boottime.patch
Patch0137: adlrdt.patch
#Serie.end

#backports
#Patch0200: mm-lru_cache_disable-use-synchronize_rcu_expedited.patch
Patch0201: 0001-sched-numa-Initialise-numa_migrate_retry.patch
Patch0202: 0002-sched-numa-Do-not-swap-tasks-between-nodes-when-spar.patch
Patch0203: 0003-sched-numa-Apply-imbalance-limitations-consistently.patch
Patch0204: 0004-sched-numa-Adjust-imb_numa_nr-to-a-better-approximat.patch
Patch0205: 0005-sched-fair-Consider-CPU-affinity-when-allowing-NUMA-.patch
Patch0206: 0006-sched-fair-Optimize-and-simplify-rq-leaf_cfs_rq_list.patch
Patch0207: 0007-sched-deadline-Use-proc_douintvec_minmax-limit-minim.patch
Patch0208: 0008-sched-Allow-newidle-balancing-to-bail-out-of-load_ba.patch
Patch0209: 0009-sched-Fix-the-check-of-nr_running-at-queue-wakelist.patch
Patch0210: 0010-sched-Remove-the-limitation-of-WF_ON_CPU-on-wakelist.patch
Patch0211: 0011-selftests-rseq-riscv-use-rseq_get_abi-helper.patch
Patch0212: 0012-selftests-rseq-riscv-fix-literal-suffix-warning.patch
Patch0213: 0013-selftests-rseq-check-if-libc-rseq-support-is-registe.patch
Patch0214: 0014-sched-fair-Remove-redundant-word.patch
Patch0215: 0015-sched-Remove-unused-function-group_first_cpu.patch
Patch0216: 0016-sched-only-perform-capability-check-on-privileged-op.patch
Patch0217: 0017-sched-fair-Introduce-SIS_UTIL-to-search-idle-CPU-bas.patch
Patch0218: 0018-sched-fair-Provide-u64-read-for-32-bits-arch-helper.patch
Patch0219: 0019-sched-fair-Decay-task-PELT-values-during-wakeup-migr.patch
Patch0220: 0020-sched-drivers-Remove-max-param-from-effective_cpu_ut.patch
Patch0221: 0021-sched-fair-Rename-select_idle_mask-to-select_rq_mask.patch
Patch0222: 0022-sched-fair-Use-the-same-cpumask-per-PD-throughout-fi.patch
Patch0223: 0023-sched-fair-Remove-task_util-from-effective-utilizati.patch
Patch0224: 0024-sched-fair-Remove-the-energy-margin-in-feec.patch
Patch0225: 0025-sched-core-add-forced-idle-accounting-for-cgroups.patch
Patch0226: 0026-sched-core-Use-try_cmpxchg-in-set_nr_-and_not-if-_po.patch
Patch0227: 0027-sched-fair-fix-case-with-reduced-capacity-CPU.patch
Patch0228: 0028-sched-core-Always-flush-pending-blk_plug.patch
Patch0229: 0029-nohz-full-sched-rt-Fix-missed-tick-reenabling-bug-in.patch
Patch0230: 0030-sched-core-Fix-the-bug-that-task-won-t-enqueue-into-.patch
Patch0231: 0031-rseq-Deprecate-RSEQ_CS_FLAG_NO_RESTART_ON_-flags.patch
Patch0232: 0032-rseq-Kill-process-when-unknown-flags-are-encountered.patch

Patch0301: 0001-sched-cpuset-Fix-dl_cpu_busy-panic-due-to-empty-cs-c.patch
Patch0302: 0002-exit-Fix-typo-in-comment-s-sub-theads-sub-threads.patch
Patch0303: 0003-sched-rt-Fix-Sparse-warnings-due-to-undefined-rt.c-d.patch
Patch0304: 0004-sched-core-Do-not-requeue-task-on-CPU-excluded-from-.patch

%description
The Linux kernel.

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel
Requires:       linux-license = %{version}-%{release}

%description extra
Linux kernel extra files

%package license
Summary: license components for the linux package.
Group: Default

%description license
license components for the linux package.

%package cpio
License:        GPL-2.0
Summary:        cpio file with kenrel modules
Group:          kernel

%description cpio
Creates a cpio file with some modules

%package dev
License:        GPL-2.0
Summary:        The Linux kernel
Group:          kernel
Requires:       linux = %{version}-%{release}
Requires:       linux-extra = %{version}-%{release}
Requires:       linux-license = %{version}-%{release}

%description dev
Linux kernel build files

%prep
%setup -q -n linux-5.19.4

#cve.patch.start cve patches
#cve.patch.end

#mainline.patch.start Mainline patches, upstream backport and fixes
#mainline.patch.end

#Serie.patch.start Clear Linux patches
%patch0101 -p1
%patch0102 -p1
%patch0103 -p1
%patch0104 -p1
%patch0105 -p1
%patch0106 -p1
%patch0107 -p1
%patch0108 -p1
%patch0109 -p1
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
%patch0127 -p1
%patch0128 -p1
%patch0130 -p1
%patch0131 -p1
#patch0132 -p1
%patch0133 -p1
%patch0134 -p1
%patch0135 -p1
%patch0136 -p1
%patch0137 -p1
#Serie.patch.end

# backports
#patch0200 -p1
#%patch0201 -p1
%patch0202 -p1
%patch0203 -p1
%patch0204 -p1
%patch0205 -p1
%patch0206 -p1
%patch0207 -p1
%patch0208 -p1
#%patch0209 -p1
#%patch0210 -p1
%patch0211 -p1
%patch0212 -p1
%patch0213 -p1
%patch0214 -p1
%patch0215 -p1
#%patch0216 -p1
#%patch0217 -p1
%patch0218 -p1
%patch0219 -p1
%patch0220 -p1
%patch0221 -p1
%patch0222 -p1
%patch0223 -p1
%patch0224 -p1
%patch0225 -p1
%patch0226 -p1
#%patch0227 -p1
#%patch0228 -p1
#%patch0229 -p1
%patch0230 -p1
%patch0231 -p1
%patch0232 -p1

#%patch0301 -p1
%patch0302 -p1
%patch0303 -p1
#%patch0304 -p1

cp %{SOURCE1} .

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

# cpio file for keyboard drivers
createCPIO() {

    Target=$1
    Kversion=$2
    KernelDir=%{buildroot}/usr/lib/kernel
    ModDir=/usr/lib/modules/${Kversion}

    mkdir -p cpiofile${ModDir}/kernel/drivers/input/{serio,keyboard}
    mkdir -p cpiofile${ModDir}/kernel/drivers/hid
    cp %{buildroot}${ModDir}/kernel/drivers/input/serio/i8042.ko      cpiofile${ModDir}/kernel/drivers/input/serio
    cp %{buildroot}${ModDir}/kernel/drivers/input/serio/libps2.ko     cpiofile${ModDir}/kernel/drivers/input/serio
    cp %{buildroot}${ModDir}/kernel/drivers/input/keyboard/atkbd.ko   cpiofile${ModDir}/kernel/drivers/input/keyboard
    cp %{buildroot}${ModDir}/kernel/drivers/hid/hid-logitech-dj.ko    cpiofile${ModDir}/kernel/drivers/hid
    cp %{buildroot}${ModDir}/kernel/drivers/hid/hid-logitech-hidpp.ko cpiofile${ModDir}/kernel/drivers/hid
    cp %{buildroot}${ModDir}/kernel/drivers/hid/hid-apple.ko          cpiofile${ModDir}/kernel/drivers/hid
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

mkdir -p %{buildroot}/usr/share/package-licenses/linux
cp COPYING %{buildroot}/usr/share/package-licenses/linux/COPYING
cp -a LICENSES/* %{buildroot}/usr/share/package-licenses/linux

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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/linux

%files cpio
/usr/lib/kernel/initrd-org.clearlinux.%{ktarget}.%{version}-%{release}

%files dev
%defattr(-,root,root)
/usr/lib/modules/%{kversion}/build
