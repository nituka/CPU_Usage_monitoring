Setup prometheus and grafana using kubernetes cluster on windows to monitor worker and master nodes metrics
Prerequisites
--
Install helm ,kubectl and kind(kubernetes package manager)

Note: yml files in repo are not for this setup. 
-
Step1: Create a Kind Cluster
--------------------------------
Use the provided kind-config.yml to create a cluster with one control-plane and two worker nodes.
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
  - role: worker
  
kind create cluster --config <path to kind-config.yml>
Verify the cluster: You should see one control-plane node and two worker nodes.
kubectl get nodes

Step 2: Install Prometheus and Grafana Using Helm
--------------------------------------------------
	1.Add Helm Repositories:
	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	helm repo add grafana https://grafana.github.io/helm-charts
	helm repo update
	2. Create a Namespace for Monitoring:
	kubectl create namespace monitoring
	3.Install Prometheus:
	helm install prometheus prometheus-community/prometheus --namespace monitoring

	4. Install Grafana:
	helm install grafana grafana/grafana --namespace monitoring

Step 3: Access Prometheus and Grafana: forward the ports to access it from localhost
---------------------------------------------
kubectl port-forward -n monitoring svc/grafana 3000:80
kubectl port-forward -n monitoring svc/prometheus-server 9090:80
Access Prometheus at http://localhost:9090.
grafana: http://localhost:3000
admin/prom-operator #thats default password

Step 4:Add Prometheus as a Data Source in Grafana
-------------------------------------
Log in to Grafana.
Go to Configuration > Data Sources.
Click Add data source and select Prometheus.
Set the URL to:http://prometheus-server.monitoring.svc.cluster.local:80
Click Save & Test.

Step 5. Import a Grafana Dashboard for Node Metrics
--
In Grafana, go to Dashboards > Import.
Use a prebuilt dashboard for node metrics. For example:
Dashboard ID: 1860 (Node Exporter Full)
Click Load, select the Prometheus data source, and import the dashboard.

Step 6: View Worker Node Metrics
--
Once the dashboard is imported, you can view metrics like CPU usage, memory usage, and more for your worker nodes.

Troubleshooting
-
No Data in Grafana:
Ensure Prometheus is scraping node-exporter metrics:
Check Status > Targets in Prometheus to ensure node-exporter targets are UP.
