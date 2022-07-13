#!/bin/bash

changed-files () {
	git diff-tree --no-commit-id --name-only -r ${@:-HEAD}
}

exists () {
	while read line; do
		test -f $line && echo $line
	done
}

root=$(git rev-parse --show-toplevel)
cd $root

files=$(changed-files $@ | grep '\.py$' | exists)
flake8 $files