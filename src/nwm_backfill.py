"""Backfill live cycles from START (ISO hour, UTC) up to now-2h. Idempotent (archive_cycle skips existing). Usage: python nwm_backfill.py 2026-10-10T22"""
import sys
from nwm_fc import *
a = sys.argv[1]  # ISO hour, or integer = hours back from now
c = (datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0) - timedelta(hours=int(a))) if a.isdigit() else datetime.fromisoformat(a).replace(tzinfo=timezone.utc)
end = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0) - timedelta(hours=2)
while c <= end:
    print(c.strftime("%Y-%m-%dT%HZ"), archive_cycle(c, sources=("aws", "gcs", "nomads"), require_complete=True), flush=True)
    c += timedelta(hours=1)
