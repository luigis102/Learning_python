#!/usr/bin/env bash
main() {
    clean="${1#"${1%%[![:space:]]*}"}"
    clean="${clean%"${clean##*[![:space:]]}"}"
    if [[ -z "$clean" ]]; then
        echo 'Fine. Be that way!'
    elif [[ "$clean" == "${clean^^}" ]] &&
         [[ "$clean" =~ [[:alpha:]] ]]; then
        if [[ "$clean" == *'?' ]]; then
            echo "Calm down, I know what I'm doing!"
        else
            echo 'Whoa, chill out!'
        fi
    elif [[ "$clean" == *'?' ]]; then
        echo 'Sure.'
    else
        echo 'Whatever.'
    fi
}
main "$@"