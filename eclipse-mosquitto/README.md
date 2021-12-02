# eclipse-mosquitto

## Environment
```
- Linux thinkpad-t480 5.4.0-81-generic #91~18.04.1-Ubuntu SMP Fri Jul 23 13:36:29 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
- Docker version 20.10.8, build 3967b7d
- Python 3.7.1
```

## How to run
- Run the eclipse mosquitto docker container
```bash
$ docker run -d -it -p 1883:1883 -v $(pwd)/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
```
- Run the CPU publisher
```bash
$ python3 publisher.py --ip localhost --port 1883 --topic cpu
```
- Run the MEM publisher
```bash
$ python3 publisher.py --ip localhost --port 1883 --topic mem
```
- Run the subscriber
```bash
$ python3 subscriber.py --ip localhost -- port 1883
```
