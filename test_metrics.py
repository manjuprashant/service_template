from prometheus_client import CollectorRegistry, generate_latest
from src.metrics import REQUEST_COUNT

def test_metrics_counter():
    # Simulate increment
    REQUEST_COUNT.labels(method='GET', endpoint='/test', http_status='200').inc()
    data = generate_latest()
    assert b'http_requests_total' in data
