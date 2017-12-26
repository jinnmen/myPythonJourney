#https://www.youtube.com/watch?v=vQv4W-JfrmQ
#! /bin/bash
# this is a comment
echo "Hellow World" # this is also a comment

# if begin with capital letter, most likely system variable

echo Our shell name is $BASH
echo Our shell version name is $BASH_VERSION
echo Our home directory is $HOME
echo Our Present Working Directory is $PWD

#user defined variables
name=Mark
10vals=10 #Don't start variables with numbers, will get missing prints
echo The name is $name 
echo The value is $10val # not considering value as variable

val=10
echo value $val
VAL=101
echo VALUE $VAL

#https://www.macissues.com/2014/04/29/commands-for-finding-files-in-the-os-x-terminal/
#mdfind command to show full path of a file with certain keyword