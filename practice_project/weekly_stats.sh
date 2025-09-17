#!/usr/bin/env bash
set -euo pipefail
DATA_FILE="synthetic_historical_fc_accuracy.tsv"
URL="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-LX0117EN-Coursera/labs/synthetic_historical_fc_accuracy.tsv"

if [ ! -f "$DATA_FILE" ]; then
  wget -q "$URL" -O "$DATA_FILE"
fi

# Extract last 7 accuracy values (col 6), skipping header
mapfile -t accuracies < <(tail -n +2 "$DATA_FILE" | tail -n 7 | awk -F'\t' '{print $6}')

if [ ${#accuracies[@]} -eq 0 ]; then
  echo "No data to process" >&2
  exit 1
fi

min=""
max=""
for a in "${accuracies[@]}"; do
  # absolute value
  if [[ "$a" == -* ]]; then
    abs=${a#-}
  else
    abs=$a
  fi
  # initialize
  if [ -z "$min" ] || [ "$abs" -lt "$min" ]; then
    min="$abs"
  fi
  if [ -z "$max" ] || [ "$abs" -gt "$max" ]; then
    max="$abs"
  fi
done

echo "Min absolute error (last 7): $min"
echo "Max absolute error (last 7): $max"


