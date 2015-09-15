Name:           linux
Version:        4.2.0
Release:        122
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://kernel.org/pub/linux/kernel/v4.x/linux-4.2.tar.xz
Source1:        config
Source2:        installkernel
Source3:        80-copy-initrd.install
Source4:        cmdline

%define kversion %{version}-%{release}

BuildRequires:  bash >= 2.03
BuildRequires:  bc
# For bfd support in perf/trace
BuildRequires:  binutils-dev
BuildRequires:  elfutils
BuildRequires:  elfutils-dev
BuildRequires:  kmod
BuildRequires:  make >= 3.78
BuildRequires:  openssl
BuildRequires:  flex bison
BuildRequires:  ncurses-dev
BuildRequires:  binutils-dev
BuildRequires:  slang-dev
BuildRequires:  libunwind-dev
BuildRequires:  python-dev
BuildRequires:  zlib-dev
# For initrd binary package
BuildRequires:  dracut
BuildRequires:  util-linux
BuildRequires:  systemd
BuildRequires:  lz4
# For EFI Stub kernel
BuildRequires:  systemd-boot

# don't srip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

Patch1:  0001-Don-t-wait-for-PS-2-at-boot.patch
Patch2:  0002-tweak-the-scheduler-to-favor-CPU-0.patch
Patch3:  0003-Silence-kvm-unhandled-rdmsr.patch
Patch4:  0004-intel-idle.patch
Patch5:  0005-i8042-Decrease-debug-message-level-to-info.patch
Patch6:  0006-Tweak-Intel-idle.patch
Patch7:  0007-raid6-boottime.patch
Patch8:  0008-reduce-the-damage-from-intel_pt-by-bailing-out-on-cp.patch
Patch9:  0009-reduce-minimal-ack-time-down-from-40-msec.patch

# Boot
Patch30: 3001-init-fix-boot-from-the-same-loader-device.patch

# DPDK 2.0.0 integration
Patch50: 5000-Add-DPDK-kni-source-files.patch
Patch51: 5001-Add-DPDK-igb_uio-source-files.patch
Patch52: 5002-Integrate-Kconfig-and-Makefiles.patch
Patch53: 5003-dpdk-remove-wrong-use-of-NLM_F_MULTI.patch
Patch54: 5004-dpdk-remove-rebuild-from-header_ops.patch

# kdbus
Patch701: 701-kdbus.patch

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

%prep
%setup -q -n linux-4.2

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

# Boot
%patch30 -p1

# DPDK 2.0.0 integration
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1

# kdbus
%patch701 -p1

cp %{SOURCE1} .

%build
BuildKernel() {
    MakeTarget=$1

    Arch=x86_64
    ExtraVer="-%{release}"

    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile

    make -s mrproper
    cp config .config

    make -s ARCH=$Arch oldconfig > /dev/null
    make -s CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} ARCH=$Arch $MakeTarget %{?sparse_mflags}
    make -s CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} ARCH=$Arch modules %{?sparse_mflags} || exit 1
}

BuildTools() {
    cd tools/perf
    sed -i '/# Define NO_GTK2/a NO_GTK2 = 1' Makefile.perf
    # TODO: Fix me
    # error message: ld: XXX.o: plugin needed to handle lto object
    sed -i '/# Define NO_LIBPYTHON/a NO_LIBPYTHON = 1' Makefile.perf
    make -s %{?sparse_mflags}
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
    install -m 644 %{SOURCE4} ${KernelDir}/cmdline-${KernelVer}
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
}

createEFIStub() {

   KernelVer=%{kversion}
   KernelDir=%{buildroot}/usr/lib/kernel

   BZIMAGE=$1
   CMDLINE=$2

   cp /usr/lib/os-release /tmp/os-release
   OS_RELEASE=/tmp/os-release
   sed -i 's/_ID=1/_ID=%{release}/'      $OS_RELEASE

   EFISTUB=org.clearlinux.native.%{version}-%{release}.efi

   kernel-efi-stub -r $OS_RELEASE -b $BZIMAGE -c $CMDLINE \
       -o ${KernelDir}/$EFISTUB
}

InstallKernel arch/x86/boot/bzImage
InstallTools

rm -rf %{buildroot}/usr/lib/firmware

# Create Linux EFI Stub file
createEFIStub arch/x86/boot/bzImage %{SOURCE4}

# Copy kernel-install script
mkdir -p %{buildroot}/usr/lib/kernel/install.d
install -m 0755 %{SOURCE3} %{buildroot}/usr/lib/kernel/install.d

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

%files
%dir /usr/lib/kernel
%dir /usr/lib/modules/%{kversion}
/usr/lib/kernel/config-%{kversion}
/usr/lib/kernel/org.clearlinux.native.%{version}-%{release}.efi
/usr/lib/modules/%{kversion}/kernel
/usr/lib/modules/%{kversion}/modules.*
/usr/lib/kernel/install.d/80-copy-initrd.install

%files dev
%defattr(-,root,root)
/usr/bin/installkernel

%files extra
%dir /usr/lib/kernel
/usr/lib/kernel/org.clearlinux.native.%{version}-%{release}
/usr/lib/kernel/System.map-%{kversion}
/usr/lib/kernel/cmdline-%{kversion}

%files tools
%{_bindir}/trace
%{_bindir}/perf
/usr/libexec/perf-core
/usr/lib64/traceevent/plugins/
%{_datadir}/bash-completion/completions/*
