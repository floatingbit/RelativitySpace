sudo apt-get update -y

curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt-get update && sudo apt-get install influxdb -y
sudo service influxdb start


echo "deb https://packagecloud.io/grafana/stable/debian/ wheezy main" | sudo tee /etc/apt/sources.list.d/grafana.list
curl https://packagecloud.io/gpg.key | sudo apt-key add -

sudo apt-get update && sudo apt-get install grafana -y
sudo service grafana-server start

sudo apt-get install python3-pip -y

sudo python3 -m pip install Flask
sudo python3 -m pip install influxdb

curl -u admin:admin \
  --header "Content-Type: application/json" \
  --request POST\
  --data '
{
  "name":"Stocks",
  "type":"influxdb",
  "url":"http://localhost:8086",
  "database":"stocks",
  "access":"server",
  "user":"admin",
  "password":"admin"
}' \
http://192.168.0.14:3000/api/datasources

curl -u admin:admin \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"dashboard":{"__inputs":[{"name":"DS_STOCKS","label":"Stocks","description":"","type":"datasource","pluginId":"influxdb","pluginName":"InfluxDB"}],"__requires":[{"type":"grafana","id":"grafana","name":"Grafana","version":"5.1.3"},{"type":"panel","id":"graph","name":"Graph","version":"5.0.0"},{"type":"datasource","id":"influxdb","name":"InfluxDB","version":"5.0.0"}],"annotations":{"list":[{"builtIn":1,"datasource":"-- Grafana --","enable":true,"hide":true,"iconColor":"rgba(0, 211, 255, 1)","name":"Annotations & Alerts","type":"dashboard"}]},"editable":true,"gnetId":null,"graphTooltip":0,"id":null,"links":[],"panels":[{"aliasColors":{},"bars":false,"dashLength":10,"dashes":false,"datasource":"${DS_STOCKS}","fill":1,"gridPos":{"h":23,"w":24,"x":0,"y":0},"id":2,"legend":{"avg":false,"current":false,"max":false,"min":false,"show":true,"total":false,"values":false},"lines":true,"linewidth":1,"nullPointMode":"null","percentage":false,"pointradius":5,"points":false,"renderer":"flot","seriesOverrides":[],"spaceLength":10,"stack":false,"steppedLine":false,"targets":[{"groupBy":[{"params":["$__interval"],"type":"time"},{"params":["null"],"type":"fill"}],"orderByTime":"ASC","policy":"default","query":"select * from stocks group by Symbol","rawQuery":true,"refId":"A","resultFormat":"time_series","select":[[{"params":["value"],"type":"field"},{"params":[],"type":"mean"}]],"tags":[]}],"thresholds":[],"timeFrom":null,"timeShift":null,"title":"Panel Title","tooltip":{"shared":true,"sort":0,"value_type":"individual"},"type":"graph","xaxis":{"buckets":null,"mode":"time","name":null,"show":true,"values":[]},"yaxes":[{"format":"short","label":null,"logBase":1,"max":null,"min":null,"show":true},{"format":"short","label":null,"logBase":1,"max":null,"min":null,"show":true}],"yaxis":{"align":false,"alignLevel":null}}],"refresh":"1s","schemaVersion":16,"style":"dark","tags":[],"templating":{"list":[]},"time":{"from":"2015-01-01T05:00:00.000Z","to":"now"},"timepicker":{"refresh_intervals":["5s","10s","30s","1m","5m","15m","30m","1h","2h","1d"],"time_options":["5m","15m","1h","6h","12h","24h","2d","7d","30d"]},"timezone":"","title":"Stocks - Time Series Graph","uid":"jU-Y9wVmz","version":2},"overwrite":true,"inputs":[{"name":"DS_STOCKS","type":"datasource","pluginId":"influxdb","value":"Stocks"}]}' \
  http://192.168.0.14:3000/api/dashboards/import
