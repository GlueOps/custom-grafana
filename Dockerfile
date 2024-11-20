FROM grafana/grafana:11.3.1@sha256:fa801ab6e1ae035135309580891e09f7eb94d1abdbd2106bdc288030b028158c

COPY grafana.ini /etc/grafana/grafana.ini
COPY datasources /etc/grafana/provisioning/datasources
COPY dashboards-provider /etc/grafana/provisioning/dashboards
COPY dashboards /var/lib/grafana/dashboards