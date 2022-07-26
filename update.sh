#!/bin/bash
rm releases.json
curl -s -O -L https://www.kernel.org/releases.json
regexp=`python3 parseversion.py`
#echo "Regexp is $regexp"
sed -i -e "$regexp" *.spec
foo="0"
git diff --exit-code || export foo="1"
echo $foo
if [ "$foo" -eq "1" ]; then
	make generateupstream
	git add *.spec upstream
	git commit -m "stable update" *.spec upstream
	make bump
	make koji-nowait
fi