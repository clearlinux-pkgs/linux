#!/bin/bash
# -*- mode: shell-script; indent-tabs-mode: nil; sh-basic-offset: 4; -*-
# ex: ts=8 sw=4 sts=4 et filetype=sh
#
# SPDX-License-Identifier: GPL-2.0
#
# Port old patches to new base
#
# Usage:
# 1. Goto current kernel source tree
# 2. /path/to/this/script /path/to/old/patch/set/*.patch

tmpdir=$(mktemp -d)
rejf=${tmpdir}/rej

for p in $*
do
    if ! git am --quiet $p 2> /dev/null
    then
        rm -f ${rejf}
        if ! patch --quiet --reject-file=${rejf} --forward -p1 < $p
        then
            if [ -f ${rejf} ]
            then
                if [ -n "${DISPLAY}" ]
                then
                    gvim -f ${rejf}
                else
                    vim ${rejf}
                fi
            fi
        fi
        git status
        echo $p
        read dopause
        if git diff --no-ext-diff --quiet
        then
            git am --quiet --skip
            git -C ${p%/*} rm --quiet ${p#*/}
        else
            git add --all
            git am --quiet --continue
        fi
    fi
done
rm -rf ${tmpdir}
