import json
import sys
from typing import Optional, Dict, Iterable

import influxdb
import requests


def get_config() -> dict:
    with open('config.json', 'r') as f:
        return json.loads(f.read())


def query_spaceapi(endpoint: str) -> Optional[dict]:
    """
    Query the specified SpaceAPI endpoint and return the 'sensors' key.
    """
    resp = requests.get(endpoint)
    try:
        data = resp.json()
    except json.decoder.JSONDecodeError:
        print('Endpoint response is not valid JSON')
        sys.exit(2)
    if 'api' not in data or 'space' not in data:
        print('Endpoint response does not look like a valid SpaceAPI object')
        sys.exit(2)
    return data.get('sensors', [])


def make_datapoint(name: str, value: float, tags: Dict[str, str]):
    return {
        'measurement': name,
        'tags': tags,
        'fields': {
            'value': value,
        },
    }


def main(endpoint: str):
    config = get_config()

    # Fetch sensors
    sensors = query_spaceapi(endpoint)

    # List of datapoints
    datapoints = []

    # Helper function for all sensors that have a numeric "value" field.
    def process_sensor(name: str, req_tags: Iterable[str], opt_tags: Iterable[str]):
        if not sensors.get(name):
            return
        for s in sensors[name]:
            tags = {}
            for tag in req_tags:
                tags[tag] = s[tag]
            for tag in opt_tags:
                if s.get(tag):
                    tags[tag] = s[tag]
            datapoints.append(make_datapoint(
                name=name,
                value=float(s['value']),
                tags=tags,
            ))

    process_sensor('beverage_supply', ['unit'], ['name', 'location'])
    process_sensor('network_connections', [], ['type', 'name', 'location'])
    process_sensor('people_now_present', [], ['name', 'location'])
    process_sensor('temperature', ['unit', 'location'], ['name'])
    process_sensor('total_member_count', [], ['name', 'location'])

    # Send to InfluxDB
    client = influxdb.InfluxDBClient(
        config['influxdb_host'], config['influxdb_port'],
        config['influxdb_user'], config['influxdb_pass'],
        database=config['influxdb_db'],
        ssl=True, verify_ssl=True, timeout=10,
    )
    client.write_points(datapoints)

    print('OK, sent %d datapoints' % len(datapoints))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <spaceapi-endpoint>' % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
