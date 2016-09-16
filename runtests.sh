#!/bin/sh
#
# Imports testdata from $TESTDATADIR and runs test scripts from $TESTSCRIPTDIR.
#

rootdir=`dirname "$0"`
TESTDATADIR="$rootdir"/testdata
TESTSCRIPTDIR="$rootdir"/tests
project_name=`basename "$TESTDATADIR"`.tar.gz

"$rootdir"/import_testcode.sh "$TESTDATADIR"

for t in "$TESTSCRIPTDIR"/*
do
	"$rootdir"/joshi.py -p "$project_name" $t
done

