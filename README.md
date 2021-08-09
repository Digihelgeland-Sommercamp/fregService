# Folkeregisteret service (FregService)

FregService is one of multiple micro services for redusert foreldrebetaling. Visit the [main repo](https://github.com/Altinn/summer-camp-2021) to get an overview and read more documentation.

FregService is a mock micro service that has a select few families downloaded from Tenor Testdata, folkeregisteret's synthetic testdata.

FregService has no couplings, but is designed with the needs of "Redusert foreldrebetaling" in mind. 

## API
Every route can be found in [app.py](https://github.com/Digihelgeland-Sommercamp/fregService/blob/main/app.py) 

[GET] [/person/\<personnummer>](https://app.swaggerhub.com/apis/Johannes-s-b/FregService/0.1)

Available personnummer of adults:
* 03839199405
* 04829098569
* 04838698536
* 05897997403
* 09828498166
* 09838197571
* 10908398829
* 11879597511
* 18817896738
* 18918899428
* 20827897842
* 21919298917
* 10858197681
* 26919398832
* 27867696526
* 30858799216

## Installation
You can use the [deployment.yaml](https://github.com/Digihelgeland-Sommercamp/fregService/blob/main/deployment.yaml) to create a deployment in kubernetes, and [service.yaml](https://github.com/Digihelgeland-Sommercamp/fregService/blob/main/service.yaml) to create a service.

[The latest docker image can be found here](https://hub.docker.com/repository/docker/johannesdigdir/freg_service)

## UML
Class diagrams of the service
![Picture showing class diagrams of the service](https://github.com/Altinn/summer-camp-2021/blob/main/Documentation/UML/FregService/FREG%20klassediagram.png "Picture showing class diagrams of the service")