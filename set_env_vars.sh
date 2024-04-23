# #!/bin/bash

# # Read variables from .env.sample (replace with actual location)
# source .env.sample

# # Loop through each line and set Heroku config var
# while IFS=':' read -r name value; do
#   if [[ ! -z "$name" && ! -z "$value" ]]; then
#     heroku config:set "$name"="$value" --app APP_NAME
#   fi
# done < ".env.sample"
