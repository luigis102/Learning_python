#!/usr/bin/env bash

main()
{
    lower="${1,,}"
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for (( i = 0; i < 26; i++ )); do
        char="${alphabet:$i:1}"
        if [[ "$lower" != *"$char"* ]]; then
            echo "false"
            return 
        fi
    done
    echo "true"
}

main "$@"


