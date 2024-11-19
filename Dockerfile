FROM grafana/grafana:10.4.13@sha256:c8644d0d41757dd444bd1aabc23740be71f0a34549128454a2b37f57a0c496b0

COPY grafana.ini /etc/grafana/grafana.ini
COPY datasources /etc/grafana/provisioning/datasources
COPY dashboards-provider /etc/grafana/provisioning/dashboards
COPY dashboards /var/lib/grafana/dashboards