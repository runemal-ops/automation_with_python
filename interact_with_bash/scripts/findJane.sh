#!/bin/bash
>oldFiles.txt
files=$(grep " jane " /home/student-00-95bee57bd148/data/list.txt | cut -d' ' -f3 | cut -d'/' -f3)
for i in $files; do
	if test -e /home/student-00-95bee57bd148/data/$i; then
		echo /home/student-00-95bee57bd148/data/$i >> oldFiles.txt
	fi
done 

