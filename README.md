# chaos-example
Example of chaos lua NGINX plugin in docker



# Instruction
1) run docker compose
2) Open localhost:3000
3) Add Prometheus data source with url: http://prometheus:9090
4) Create dashboard with metrics: 
- request_timings_bucket [ histogram_quantile(0.95, sum by(le) (rate(request_timings_bucket[$__rate_interval]))) ]
- oks [ increase(oks[$__rate_interval]) ]
- errors [ increase(errors[$__rate_interval]) ]
5) write in chaos/config.txt file one of:
  - reject
  - latency
  - no chaos

