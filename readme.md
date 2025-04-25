Bring up prometheus and grafana containers to monitor local system CPU usage using node exporter
docker-compose.yml
prometheus.yml
max_cpu.py -> this is to increase CPU load to check CPU usage variations

'Note':If you want to try kubernetes to monitor CPU usage for worker and master nodes. Please follow steps mentioned in GarafnaKubernetes.md 
This repository doesnt have any config files related to kubernetes setup. 
