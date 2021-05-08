"""Starts a training (an experiment)."""

import yaml
from pathlib import Path


def start(experiment_file: str):
    """Start an experiment."""

    # Load experiment file
    assert Path(experiment_file).suffix == ".yaml"
    with open(experiment_file) as f:
        params = yaml.safe_load(f)

    # TODO: allow multiple runs


def start_run(params: dict):
    """Execute a single run."""
