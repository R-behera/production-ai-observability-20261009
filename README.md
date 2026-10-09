# Production AI Observability Monitor

An observability pipeline that classifies AI trace failures and produces release-ready reliability reports.

Generated on 2026-10-09 as an independent production-AI architecture project.

## Real-World Problem

Production AI teams need trace-level signals for latency, token growth, tool failures, and low-quality outputs.

## Hugging Face Tasks

- `text-classification`
- `token-classification`
- `summarization`
- `zero-shot-classification`

## Recommended Production Stack

- OpenTelemetry GenAI semantic conventions
- OpenTelemetry Collector for vendor-neutral ingestion
- ClickHouse or PostgreSQL for trace analytics
- Prometheus and Grafana for service-level metrics
- MLflow for model and prompt version linkage
- FastAPI for trace search and regression APIs

## Included

- Runnable Python pipeline with no runtime dependencies
- Local JSON HTTP inference service
- Public-data API connector with explicit provenance
- Reproducible training script
- Held-out evaluation command
- Synthetic dataset with explicit provenance
- Trained transparent baseline model
- Architecture and production-boundary documentation
- Unit tests, CI workflow, and Dockerfile
- Hugging Face-ready model and dataset cards

## Architecture

1. Structured trace ingestion
1. Failure taxonomy
1. Deterministic anomaly classifier
1. Service-level summaries
1. Release regression gate

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full flow and production
boundaries.

## Quick Start

```bash
python3 -m unittest discover -s tests
PYTHONPATH=src python3 -m ai_observability.cli "Request latency rose above the service objective"
PYTHONPATH=src python3 evaluate.py
PYTHONPATH=src python3 -m ai_observability.service
```

The service exposes `GET /health` and `POST /predict`.

Rebuild the model:

```bash
python3 train.py
```

## Baseline Evaluation

- Held-out synthetic examples: 4
- Accuracy: 1
- Target metrics: failure_class_accuracy, alert_precision, trace_coverage

This score verifies that the code and evaluation contract work. It does not
claim production performance.

## Hugging Face Artifacts

When the controller has a Hugging Face token and namespace configured, it
publishes:

- Dataset: `production-ai-observability-20261009-dataset`
- Model: `production-ai-observability-20261009-model`

## Portfolio Value

This repository maps to production AI engineering work in:

- LLMOps observability and trace instrumentation
- Prompt, model, dataset, and deployment lineage
- SLOs, anomaly detection, and incident diagnostics
- High-volume telemetry storage and aggregation
- Evaluation-driven production monitoring

See [PORTFOLIO.md](PORTFOLIO.md) for resume-ready impact targets and interview
discussion areas.

## 1-3 Month Expansion

Follow [ROADMAP.md](ROADMAP.md) to add real-world APIs, a stronger open model,
durable orchestration, evaluation, observability, scalability testing, and a
public deployment.

## Safety

Thresholds are demonstration defaults and need calibration against each production workload.

Review [ARCHITECTURE.md](ARCHITECTURE.md),
[PRODUCTION.md](PRODUCTION.md), [SECURITY.md](SECURITY.md),
[MODEL_CARD.md](MODEL_CARD.md), and [DATASET_CARD.md](DATASET_CARD.md) before
adapting this project.
