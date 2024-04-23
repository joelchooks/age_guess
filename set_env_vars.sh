#!/bin/bash

app_name="$1"

if [[ -z "$app_name" ]]; then
  echo "Error: Heroku application name (APP_NAME) not provided!"
  exit 1
fi

echo >> .env.sample
source .env.sample

while IFS='=' read -r name value; do
  if [[ ! -z "$name" && ! -z "$value" ]]; then
    heroku config:set "$name"="$value" --app  "$app_name"
  fi
done < ".env.sample"