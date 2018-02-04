# SpaceAPI Sensor Logger

A Python 3 script to relay sensor values from a SpaceAPI endpoint to an
InfluxDB instance so it can be viewed in Grafana.

## Supported sensor types

- `beverage_supply`
- `network_connections`
- `people_now_present`
- `temperature`
- `total_member_count`

If you want support for another type, please open an issue or pull request! :)

## Configuration

Copy `config.example.json` to `config.json` and adjust the values.

## Running

After installing the requirements from `requirements.txt`, just run `python3
relay.py <endpoint-url>` regularly :)
