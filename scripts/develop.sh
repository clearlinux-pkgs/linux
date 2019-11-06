#!/bin/bash
# -*- mode: shell-script; indent-tabs-mode: nil; sh-basic-offset: 4; -*-
# ex: ts=8 sw=4 sts=4 et filetype=sh

SPECFILE=$1
DESTDIR=$2

for c in grep cmp sha1sum make tar git
do
    if ! command -v $c > /dev/null
    then
        echo >&2 "The script needs the \"$c\" command, and it was not found."
        exit 1
    fi
done

if [ ! ${SPECFILE} ]
then
    echo >&2 "${SPECFILE} not found"
    exit 1
fi

if [ -z "${DESTDIR}" ]
then
    DESTDIR=.
else
    mkdir -p ${DESTDIR}
fi

SRC_URL=$(grep "^Source0:" "${SPECFILE}" | cut -f 2- -d ':' | tr -d " ")
SRC_FILE=${SRC_URL##*/}
SRC_DIR=${SRC_FILE%*.tar.xz}
SRC_VER=${SRC_DIR#*-}

if [ ! -f ${SRC_FILE} ]
then
    # Get upstream sources
    if ! curl --fail -LO ${SRC_URL}
    then
        echo >&2 "Cannot download ${SRC_FILE}"
        exit 3
    fi
fi

echo $(sha1sum ${SRC_FILE} | cut -d\  -f1)/${SRC_FILE} > upstream.check

if ! cmp --quiet upstream upstream.check
then
    echo >&2 "${SRC_FILE} checksum fails"
    rm upstream.check
    exit 2
fi

rm upstream.check

rm -rf ${DESTDIR}/${SRC_DIR}
tar xf ${SRC_FILE} -C ${DESTDIR}

git -C ${DESTDIR}/${SRC_DIR} init --quiet
git -C ${DESTDIR}/${SRC_DIR} config gc.auto 0
git -C ${DESTDIR}/${SRC_DIR} add --all
git -C ${DESTDIR}/${SRC_DIR} commit -m "${PKG_NAME} ${SRC_VER}" --quiet
git -C ${DESTDIR}/${SRC_DIR} tag -a -m "v${SRC_VER}" "v${SRC_VER}"

for p in CVE* [0-9]*.patch
do
    if [ -f $p ]
    then
        if ! git -C ${DESTDIR}/${SRC_DIR} am --quiet $(realpath $p)
        then
            echo >&2 "Error at: ${p}"
            exit 4
        fi
    fi
done

cp config ${DESTDIR}/${SRC_DIR}/.config

echo
echo "The linux source plus Clear Linux patches is"
echo "placed at: \"$(realpath ${DESTDIR}/${SRC_DIR})\""
