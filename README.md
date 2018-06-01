* Open a terminal
* Run `sudo apt-get update`
* Install git using `sudo apt-get install git`
* Clone github repository using `git clone https://github.com/floatingbit/RelativitySpace.git; cd RelativitySpace`
* Run the installation script using `./install.sh` which installs dependencies for InfluxDB, Grafana and Flask as well as imports a dashboard for viewing Time Series data
* Start the service that brings up an endpoint that can be used to fetch Stocks data from Intrino by running `./fetch-stock-data.py` in the terminal
* Using username : `admin`, password : `admin`, open the dashboard for viewing the incoming data by accessing it at `http://localhost:3000/d/jU-Y9wVmz/stocks-time-graph-series`
* In a new terminal window, run the following curl command to begin fetching data `curl http://127.0.0.1:5000/get-stocks-data` (or) go to the URL `http://127.0.0.1:5000/get-stocks-data` using any web browser to begin fetching data.
* View the incoming data in real-time using the Grafana dashboard that was previously opened
