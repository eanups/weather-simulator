# weather-simulator

This is a prototype of a program which artificially simulates the weather and outputs weather data in a standard format as an input for a game.

The simulator generates reads the city location co-ordinates (latitude, longitude) and topography image data to generate weather conditions as shown below. 
    
    Location|Position|Local Time|Conditions|Temperature|Pressure|Humidity
    
    Sydney|-33.86,151.21,39|2015-12-23T05:02:12Z|Rain|+12.5|1004.3|97
    Melbourne|-37.83,144.98,7|2015-12-24T15:30:55Z|Snow|-5.3|998.4|55
    Adelaide|-34.92,138.62,48|2016-01-03T12:35:37Z|Sunny|+39.4|1114.1|12

where
* Location is an optional label describing one or more positions,
* Position is a comma-separated triple containing latitude, longitude, and elevation in metres above sea
level,
* Local time is an ISO8601 date time,
* Conditions is either Snow, Rain, Sunny,
* Temperature is in °C,
* Pressure is in hPa, and
* Relative humidity is a %.


### Installation 

#### Setup With Pipenv. (Skip to `Setup with Docker` if running on a container is preferred)

Ensure you have python 3.6+ on your system. 

Download the weather-simulator project onto a directory. Install `pipenv` a python virtual env manager if you already don't have.

`$ cd weather-simulator`

`$ pipenv shell`

`$ pipenv sync`


##### Execution 

`$ python weather_generate.py`

```
Sydney|-33.869, 151.209, 93.57450980392157|2019-06-17T14:08:07+10:00|SUNNY|19.621115356667698|1005|44
London|51.507, -0.128, 0.9208333333333332|2019-06-17T05:08:07+01:00|SUNNY|6.531865722508956|1029|60
Bangalore|12.97, 77.56, 627.0288725490196|2019-06-17T04:08:07+00:00|RAINY|31.234142650835192|1011|73
Dubai|25.205, 55.271, 172.7980392156863|2019-06-17T08:08:07+04:00|SUNNY|27.294594537699417|1017|65
Dallas|32.777, -96.797, 262.0449509803921|2019-06-17T04:08:07+00:00|SUNNY|13.540999718688358|1026|63
Thimphu|27.473, 89.639, 4357.348921568628|2019-06-17T10:08:07+06:00|SNOWY|-1.411217211447692|1002|60
Toronto|43.653, -79.383, 295.74617647058824|2019-06-17T00:08:07-04:00|SUNNY|13.49357620845891|1022|53
Buenos Aires|-34.604, -58.382, 48.009509803921574|2019-06-17T04:08:07+00:00|RAINY|25.35208419858957|1017|80
Cape Town|-33.925, 18.424, 2.1226960784313724|2019-06-17T04:08:07+00:00|SUNNY|23.59603661807487|1018|53
Beijing|39.904, 116.407, 1227.525637254902|2019-06-17T04:08:07+00:00|SUNNY|9.887511369422173|1022|64
```



#### Setup (with Docker)

* Make sure you have a docker engine running on your system. 

* Go to the project directory `$ cd weather-simulator `
    
* Run `$ docker build -t weather-simulator:v1 . `
    

This might take a while depending on the system resource (during the first time). Once all the dependencies are built, 
    run the app within the container.
    
#### Execution 

Ensure port 8080 is open.

    `$ docker run -p 8080:8080 weather-simulator:v1 `
     
```
(weather-simulator) bash-3.2$ docker run -p 8080:8080 weather-simulator:v1
    [2019-06-17 05:06:14 +0000] [1] [INFO] Starting gunicorn 19.9.0
    [2019-06-17 05:06:14 +0000] [1] [INFO] Listening at: http://0.0.0.0:8080 (1)
    [2019-06-17 05:06:14 +0000] [1] [INFO] Using worker: sync
    [2019-06-17 05:06:14 +0000] [8] [INFO] Booting worker with pid: 8 
```



Now, go to the browser and try the below URL. 


##### Initial Ping

    http://localhost:8080/
    
Displays the default help and the API's available.    
    
```
{
    "404": "The API call you tried to make was not defined. Here's a definition of the API to help you get going :)",
    "documentation": {
        "handlers": {
            "/index": {
                "GET": {
                    "examples": [
                        "http://localhost/index"
                    ],
                    "outputs": {
                        "format": "JSON (Javascript Serialized Object Notation)",
                        "content_type": "application/json; charset=utf-8"
                    }
                }
            },
            "/weather": {
                "GET": {
                    "examples": [
                        "http://localhost/weather"
                    ],
                    "outputs": {
                        "format": "JSON (Javascript Serialized Object Notation)",
                        "content_type": "application/json; charset=utf-8"
                    },
                    "inputs": {
                        "city": {
                            "type": "Basic text / string value"
                        }
                    }
                }
            }
        }
    }
}
```


##### Request for weather with city parameter

    http://localhost:8080/weather?city=Sydney 

```
{"city": "Sydney", "weather": "Sydney|-33.869, 151.209, 93.57450980392157|2019-06-17T15:38:40+10:00|SUNNY|17.033336190496577|1025|74"}
```


##### Request for weather for all configured cities

    http://localhost:8080/weather 



### Tests.

```bash
---------- coverage: platform darwin, python 3.7.2-final-0 -----------
Name                                             Stmts   Miss  Cover
--------------------------------------------------------------------
weather/__init__.py                                  0      0   100%
weather/logger.py                                    5      0   100%
weather/simulator/__init__.py                        0      0   100%
weather/simulator/meta/__init__.py                   0      0   100%
weather/simulator/meta/parsers/__init__.py           0      0   100%
weather/simulator/meta/parsers/img_parser.py        17      0   100%
weather/simulator/meta/parsers/json_parser.py       14      3    79%
weather/simulator/model/__init__.py                  0      0   100%
weather/simulator/model/algos/__init__.py            0      0   100%
weather/simulator/model/algos/mercator.py            8      0   100%
weather/simulator/model/factors/__init__.py          0      0   100%
weather/simulator/model/factors/coordinates.py      10      0   100%
weather/simulator/model/factors/forecaster.py       47     14    70%
weather/simulator/model/factors/generator.py        17      0   100%
weather/simulator/model/img_viewer.py               12      6    50%
weather/simulator/readers/__init__.py                0      0   100%
weather/simulator/readers/img_reader.py             12      0   100%
weather/simulator/readers/json_reader.py            12      1    92%
weather/simulator/utils/__init__.py                  0      0   100%
weather/simulator/utils/file_util.py                 6      0   100%
weather/simulator/utils/timezone.py                  8      0   100%
weather/simulator/utils/weather_config.py           20      0   100%
--------------------------------------------------------------------
TOTAL                                              188     24    87%

========================================================================================== 19 passed, 1 warnings in 4.21 seconds ==========================================================================================
(weather-simulator)
```

#### Location Display 

The tool can be extended for manual display of location. However this functionality was used only for manual testing.

![Alt text](resources/image.png?raw=true "Locating Sydney")




>> End of Document 