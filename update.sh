#!/bin/bash

set -euo pipefail

PKG=linux
STABLE_VER=6.6
SPEC=./$PKG.spec

CUR_VER=$(rpmspec --srpm -q --qf="%{VERSION}" $SPEC)
CUR_VER=${CUR_VER//./\\.}

rm -f releases.json
curl -sSf -O -L https://www.kernel.org/releases.json
NEW_VER=$(python3 ./filter-stable.py $STABLE_VER releases.json)

sed -i -e "s/$CUR_VER/$NEW_VER/g" $SPEC

if ! git diff --quiet $SPEC; then
	make generateupstream
	make bumpnogit
	git add $SPEC upstream release
	git commit -m "Stable update to $NEW_VER" $SPEC upstream release
	make koji-nowait
fi
