#!/bin/bash

current_time=$(date +%s)
echo $current_time

for app_name in $(heroku apps --json | jq -r '.[] | .name'); do
    creation_time=$(heroku apps:info --json -a $app_name | jq -r '.created_at')

    creation_timestamp=$(date -d "$creation_time" +%s)
    echo $creation_timestamp

    # Calculate the cutoff time (5 hours ago)
    # cutoff_time=$(($current_time - 5*60*60))
    cutoff_time=$(($current_time - 2*60))

    # If the app was created before the cutoff time, destroy it
    if [ "$creation_timestamp -lt $cutoff_time" ]; then
        echo "Destroying app: $app_name"
        heroku apps:destroy --app=$app_name --confirm=$app_name
    fi
done
