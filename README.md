# SpaceAPI InfluxDB Sensor Logger

[![Docker Image Size (tag)](https://img.shields.io/docker/image-size/spaceapi/influxdb-sensor-logger/latest)](https://hub.docker.com/r/spaceapi/influxdb-sensor-logger)

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


## Docker

The repository provides a `Dockerfile` that calls `relay.py` in a loop.
Configure it using the following env vars:

- `INFLUXDB_HOST`
- `INFLUXDB_PORT`
- `INFLUXDB_USER`
- `INFLUXDB_PASS`
- `INFLUXDB_DB`
- `SPACEAPI_ENDPOINT`
- `RELAY_INTERVAL_SECONDS`

The image is published at [docker.io/spaceapi/influxdb-sensor-logger](https://hub.docker.com/r/spaceapi/influxdb-sensor-logger).


## License

Licensed under either of

 * Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
 * MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.


### Contribution

Unless you explicitly state otherwise, any contribution intentionally
submitted for inclusion in the work by you, as defined in the Apache-2.0
license, shall be dual licensed as above, without any additional terms or
conditions.
