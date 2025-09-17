#!/usr/bin/env bash
set -euo pipefail
CITY="casablanca"
LOG_FILE="rx_poc.log"
TZ_DB="Africa/Casablanca"

if ! command -v jq >/dev/null 2>&1; then
  echo "Error: jq is required. Install with: sudo apt update && sudo apt install -y jq" >&2
  exit 1
fi

# Ensure header exists
if [ ! -s "$LOG_FILE" ] || ! head -n1 "$LOG_FILE" | grep -q '^year\tmonth\tday\tobs_temp\tfc_temp$'; then
  printf 'year\tmonth\tday\tobs_temp\tfc_temp\n' > "$LOG_FILE"
fi

WEATHER_JSON=$(curl -s "https://wttr.in/${CITY}?format=j1")

obs_temp=$(echo "$WEATHER_JSON" | jq -r '.current_condition[0].temp_C')
fc_temp=$(echo "$WEATHER_JSON" | jq -r '.weather[1].hourly[] | select(.time=="1200") | .tempC' | head -n1)

# Fallback if 1200 not found (use first hourly of day)
if [ -z "${fc_temp:-}" ] || [ "$fc_temp" = "null" ]; then
  fc_temp=$(echo "$WEATHER_JSON" | jq -r '.weather[1].hourly[0].tempC')
fi

export TZ="$TZ_DB"
year=$(date +%Y)
month=$(date +%-m)
day=$(date +%-d)

printf '%s\t%s\t%s\t%s\t%s\n' "$year" "$month" "$day" "$obs_temp" "$fc_temp" >> "$LOG_FILE"


