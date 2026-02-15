#!/usr/bin/env bash

score=$(( $1 ))   # Force input to be a number
command="$2"
item="$3"

# 1. Define names in order (Low bit -> High bit)
# We use this to ensure the loop output is always correct.
allergens=(eggs peanuts shellfish strawberries tomatoes chocolate pollen cats)

# 2. Define values for lookup (Associative Array)
declare -A values
values[eggs]=1
values[peanuts]=2
values[shellfish]=4
values[strawberries]=8
values[tomatoes]=16
values[chocolate]=32
values[pollen]=64
values[cats]=128


if [[ "$command" == "list" ]]; then
    result=""
    # Iterate through the ORDERED list of names
    for name in "${allergens[@]}"; do
        val=${values[$name]}
        # Bitwise Check: (( (score & val) == val ))
        if (( (score & val) == val )); then
             # Use a newline or space depending on test requirements
             # Standard exercism often wants output on separate lines or space-separated
             result+="$name " 
        fi
    done
    # Remove trailing space and print
    echo "${result% }"
    exit 0
fi

# CASE 2: Check a specific allergy
if [[ "$command" == "allergic_to" ]]; then
    val=${values[$item]}
    # Check if bit is set
    if (( (score & val) == val )); then
        echo "true"
    else
        echo "false"
    fi
    exit 0
fi