#!/usr/bin/env bash
alphabet="abcdefghijklmnopqrstuvwxyz" # set the alphabet
pangram_candidate="${1,,}"            # set the candidate
# get outta here letters && I love Bash built-ins
zero_check="${alphabet//[$pangram_candidate]/}"
# if zero_check is empty then the candidate was a pangram
[[ -z $zero_check ]] && echo 'true' || echo 'false'


