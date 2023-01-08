from prometheus_client import Counter, Summary


QUANTILE = 0.5
domain_event_metric = Counter("domain_events", "Domain Events", ["name"])
api_request_duration = Summary("http_request_duration_seconds", "Api requests response time in seconds", ["endpoint"])
