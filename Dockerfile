FROM grafana/grafana:10.4.6@sha256:ffef0672f94b4a9141e3979011bbf3357e54df77492381faecc016cbfe170e00

COPY grafana.ini /etc/grafana/grafana.ini
COPY datasources /etc/grafana/provisioning/datasources
COPY dashboards-provider /etc/grafana/provisioning/dashboards
COPY dashboards /var/lib/grafana/dashboards