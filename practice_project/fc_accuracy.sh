#!/usr/bin/env bash
set -euo pipefail
LOG_FILE="rx_poc.log"
OUT_FILE="historical_fc_accuracy.tsv"

# Ensure output header exists
if [ ! -s "$OUT_FILE" ] || ! head -n1 "$OUT_FILE" | grep -q '^year\tmonth\tday\tobs_temp\tfc_temp\taccuracy\taccuracy_range$'; then
  printf 'year\tmonth\tday\tobs_temp\tfc_temp\taccuracy\taccuracy_range\n' > "$OUT_FILE"
fi

if [ ! -f "$LOG_FILE" ]; then
  echo "Error: $LOG_FILE not found" >&2
  exit 1
fi

# Need at least header + two data rows
line_count=$(awk 'END{print NR}' "$LOG_FILE")
if [ "$line_count" -lt 3 ]; then
  echo "Error: Not enough data in $LOG_FILE. Need at least two days." >&2
  exit 1
fi

today_line=$(tail -n 1 "$LOG_FILE")
yesterday_line=$(tail -n 2 "$LOG_FILE" | head -n 1)

IFS=$'\t' read -r year month day obs_today fc_today_unused <<< "$today_line"
IFS=$'\t' read -r year_prev month_prev day_prev obs_prev fc_today_forecast <<< "$yesterday_line"

# integer arithmetic
accuracy=$(( obs_today - fc_today_forecast ))
abs_accuracy=$accuracy
if [ $abs_accuracy -lt 0 ]; then
  abs_accuracy=$(( -abs_accuracy ))
fi

if [ $abs_accuracy -le 1 ]; then
  range="excellent"
elif [ $abs_accuracy -le 2 ]; then
  range="good"
elif [ $abs_accuracy -le 3 ]; then
  range="fair"
elif [ $abs_accuracy -le 4 ]; then
  range="poor"
else
  range="very_poor"
fi

printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
  "$year" "$month" "$day" "$obs_today" "$fc_today_forecast" "$accuracy" "$range" >> "$OUT_FILE"


