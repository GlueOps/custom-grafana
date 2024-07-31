FROM grafana/grafana:10.2.9@sha256:166a95e0d0e07986b3572534cf4fc852493518464250af5507a505ed87f1834e

COPY grafana.ini /etc/grafana/grafana.ini
COPY datasources /etc/grafana/provisioning/datasources
COPY dashboards-provider /etc/grafana/provisioning/dashboards
COPY dashboards /var/lib/grafana/dashboards