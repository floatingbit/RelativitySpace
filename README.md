* Open a terminal
* Run `sudo apt-get update`
* Install git using `sudo-apt-get install git`
* Clone github repository using `git clone https://github.com/floatingbit/RelativitySpace.git; cd RelativitySpace`
* Run installation script using `./install.sh` which installs dependencies for InfluxDB, Grafana and Flask as well as imports a dashboard for viewing Time Series data that autorefreshes every 5s
* Start service that brings up an endpoint that can used to fetch Stocks data from Intrino for 3 companies using `./fetch-stock-data.py`
* Grafana requires your IP address to access the dashboard which can be retrieved using `ifconfig`
* Open the dashboard for viewing the incoming data by accessing it at http://192.168.0.14:3000/d/jU-Y9wVmz/stocks-graph345?orgId=1 using username : `admin`, password : `admin`
* Run the following curl command to begin fetching data `curl http://127.0.0.1:5000/get-stocks-data` (or) go to the URL `http://127.0.0.1:5000/get-stocks-data` using any web browser to view the incoming time series in real-time
