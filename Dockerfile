FROM grafana/grafana:10.3.7@sha256:d150251ffc9435ee28e18e42fc07199706776325d3d39ec07b41825abd778a27

COPY grafana.ini /etc/grafana/grafana.ini
COPY datasources /etc/grafana/provisioning/datasources
COPY dashboards-provider /etc/grafana/provisioning/dashboards
COPY dashboards /var/lib/grafana/dashboards