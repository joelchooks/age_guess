#!/bin/bash

app_name="$1"
mr_url="$2"

if [[ -z "$app_name" ]]; then
  echo "Error: Heroku application name (app_name) not provided!"
  exit 1
fi

if [[ -z "$mr_url" ]]; then
  echo "Error: Heroku application url (mr_url) not provided!"
  exit 1
fi

# Strip "https://" and trailing "/"
mr_url=$(echo "$mr_url" | sed 's#^https://##' | sed 's#/$##')

echo >> .env.sample
source .env.sample

while IFS='=' read -r name value; do
  if [[ ! -z "$name" && ! -z "$value" ]]; then
    if [[ "$name" == "ALLOWED_HOSTS" ]]; then
      value="$value,.${mr_url}"
    fi
    heroku config:set "$name"="$value" --app "$app_name"
  fi
done < ".env.sample"
