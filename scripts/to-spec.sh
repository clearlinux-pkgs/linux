#!/bin/bash
# -*- mode: shell-script; indent-tabs-mode: nil; sh-basic-offset: 4; -*-
# ex: ts=8 sw=4 sts=4 et filetype=sh
#
# SPDX-License-Identifier: GPL-3.0-or-later

KLR_SPEC_FILE=$1
repo_path=.
tmpd=$(mktemp -d /tmp/spec.XXX)

sed -i '/PK XXXX/,/#END/{//!d}' ${KLR_SPEC_FILE}
sed -i '/patchXXXX/,/End XXXX/{//!d}' ${KLR_SPEC_FILE}

for patch in ${repo_path}/[01234]*.patch
do
    P=${patch##*/}
    N=$(echo ${P} | cut -c 1-4)
    echo "Patch${N}: ${P}"  >> ${tmpd}/PatchXXXX
    echo "%patch${N} -p1" >> ${tmpd}/patchYYYY
done

sed -i "/PK XXXX/r ${tmpd}/PatchXXXX"   ${KLR_SPEC_FILE}
sed -i "/patchXXXX/r ${tmpd}/patchYYYY" ${KLR_SPEC_FILE}

rm -rf ${tmpd}
