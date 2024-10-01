FROM grafana/grafana:10.4.10@sha256:e9b5417327531e1ea588bd617bb1bc3c724fa4de7fac0d96893a887fe5a478ad

COPY grafana.ini /etc/grafana/grafana.ini
COPY datasources /etc/grafana/provisioning/datasources
COPY dashboards-provider /etc/grafana/provisioning/dashboards
COPY dashboards /var/lib/grafana/dashboards