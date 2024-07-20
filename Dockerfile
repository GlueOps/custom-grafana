FROM grafana/grafana:10.2.5@sha256:33df8202cfe40b8959c4b7237bc309af9ec8637f860fbccff111399dc7c46c32

COPY grafana.ini /etc/grafana/grafana.ini
COPY datasources /etc/grafana/provisioning/datasources
COPY dashboards-provider /etc/grafana/provisioning/dashboards
COPY dashboards /var/lib/grafana/dashboards