"""Public-data connectors for the portfolio expansion phase.

The generated test suite never calls the network. Run this module manually to
download a small raw snapshot, then review licensing and terms before use.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.request
from pathlib import Path


SOURCES = [
    {
        "name": "Prometheus HTTP API",
        "url": "https://prometheus.demo.do.prometheus.io/api/v1/query?query=up",
        "purpose": "Real time-series telemetry for anomaly pipelines"
    },
    {
        "name": "GitHub Events API",
        "url": "https://api.github.com/events?per_page=10",
        "purpose": "Deployment-correlated public event metadata"
    }
]


def fetch(source: dict) -> bytes:
    request = urllib.request.Request(
        source["url"],
        headers={
            "Accept": "application/json, application/xml, text/plain",
            "User-Agent": os.environ.get(
                "DATA_SOURCE_USER_AGENT",
                "industry-ai-portfolio/0.1 contact@example.com",
            ),
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=int, default=0)
    parser.add_argument("--output", default="data/raw/source-snapshot.txt")
    args = parser.parse_args()

    source = SOURCES[args.source]
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(fetch(source))
    print(
        json.dumps(
            {
                "source": source["name"],
                "purpose": source["purpose"],
                "output": str(destination),
                "bytes": destination.stat().st_size,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
