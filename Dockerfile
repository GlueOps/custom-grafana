FROM grafana/grafana:10.4.11@sha256:594013a7e4bbc9271def30b8cc89f32b8f979cc2fd152d107bf6c8c340d52117

COPY grafana.ini /etc/grafana/grafana.ini
COPY datasources /etc/grafana/provisioning/datasources
COPY dashboards-provider /etc/grafana/provisioning/dashboards
COPY dashboards /var/lib/grafana/dashboards