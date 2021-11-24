#!/usr/bin/env bash
set -euo pipefail

# Ensure that the specified variable is defined and non-empty.
# Otherwise, abort.
function ensure_var() {
    var=$1
    if [[ ${!var:-} == "" ]]; then
        1>&2 echo "Error: Variable $var not defined!"
        exit 1
    fi
}

# Required vars
ensure_var "INFLUXDB_HOST"
ensure_var "INFLUXDB_PORT"
ensure_var "INFLUXDB_USER"
ensure_var "INFLUXDB_PASS"
ensure_var "INFLUXDB_DB"
ensure_var "SPACEAPI_ENDPOINT"
ensure_var "RELAY_INTERVAL_SECONDS"

# Write config file
{
echo "{"
echo "    \"influxdb_host\": \"$INFLUXDB_HOST\","
echo "    \"influxdb_port\": $INFLUXDB_PORT,"
echo "    \"influxdb_user\": \"$INFLUXDB_USER\","
echo "    \"influxdb_pass\": \"$INFLUXDB_PASS\","
echo "    \"influxdb_db\": \"$INFLUXDB_DB\""
echo "}"
} > config.json

# Run every $RELAY_INTERVAL_SECONDS seconds
while true; do
    echo -n "$(date)    "
    python3 relay.py "$SPACEAPI_ENDPOINT"
    sleep "$RELAY_INTERVAL_SECONDS"
done
