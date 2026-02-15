#! /usr/bin/env bash
score="$1"
second="$2"
third="$3"
declare -A allergy_scores

allergens=(eggs peanuts shellfish strawberries tomatoes chocolate pollen cats)
allergy_scores["eggs"]=1
allergy_scores["peanuts"]=2
allergy_scores["shellfish"]=4
allergy_scores["strawberries"]=8
allergy_scores["tomatoes"]=16
allergy_scores["chocolate"]=32
allergy_scores["pollen"]=64
allergy_scores["cats"]=128

	if [[ $second == "list" ]]; then
		list=""
		for a in "${allergens[@]}"; do
			val=${allergy_scores[$a]}
			if [[ $((score & val)) -eq $val ]]; then
				list+="$a "
			fi
		done
		echo ${list% }
		exit 0
	fi

	if [[ "$second" == "allergic_to" ]]; then
		val=${allergy_scores[$third]}
		if [[ $((score & val)) == "$val" ]]; then
			echo "true"
		else
			echo "false"
		fi
		exit 0
	fi
