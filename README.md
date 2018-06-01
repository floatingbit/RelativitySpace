* Open a terminal
* Run sudo apt-get update
* Install git using sudo-apt-get install git
* Clone github repository using git clone https://github.com/floatingbit/RelativitySpace.git; cd RelativitySpace
* Run installation script using ./install.sh which installs dependencies for InfluxDB, Grafana and Flask as well as imports a dashboard for viewing Time Series data that autorefreshes every 5s
* Start service that brings up an endpoint that can used to fetch Stocks data from Intrino for 3 companies using ./fetch-stock-data.py
* Open the dashboard for viewing the incoming data
* Run the following curl command to begin fetching data
* This is what you should be seeing [screenshot]

