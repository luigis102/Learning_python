#!/usr/bin/env bash



word="$1"
char=""
for ((i=${#word} - 1; i >= 0; i--)); do
	char+="${word:i:1}"
done
echo "$char"