---
license: cc-by-4.0
language:
- en
pretty_name: Production AI Observability Monitor Synthetic Evaluation Set
size_categories:
- n<1K
task_categories:
- text-classification
tags:
- synthetic
- ai-observability
- evaluation
- text-classification
- token-classification
- summarization
- zero-shot-classification
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: test
    path: data/test.jsonl
---

# Production AI Observability Monitor Synthetic Dataset

## Summary

This dataset contains 14 training examples and 4
held-out examples for **Production AI teams need trace-level signals for latency, token growth, tool failures, and low-quality outputs.**

Every record is synthetic and includes:

- `input`: query, event, or feature description
- `label`: expected class, route, relation, or evidence category
- `context`: synthetic supporting context
- `source`: fictional source identifier
- `variant`: generation pattern
- `synthetic`: always `true`

## Uses

- Reproducible unit and integration tests
- Baseline model training
- Evaluation harness development
- Schema and architecture demonstrations

## Limitations

Thresholds are demonstration defaults and need calibration against each production workload.

This dataset does not represent real users, patients, customers, production
traffic, or licensed media. It must not be presented as real-world evidence.

## Related Model

[{{HF_NAMESPACE}}/production-ai-observability-20261009-model](https://huggingface.co/{{HF_NAMESPACE}}/production-ai-observability-20261009-model)
