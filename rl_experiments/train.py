"""Starts a training (an experiment)."""

import shutil
import subprocess
import tempfile
import time
from pathlib import Path

import pkg_resources
import yaml
from training_paths import paths as training_paths


def start(experiment_file: str):
    """Start an experiment."""

    # Load experiment file
    assert Path(experiment_file).suffix == ".yaml"
    with open(experiment_file) as f:
        params = yaml.safe_load(f)

    # Run all
    processes = []
    for i in range(params["n-runs"]):
        processes.append(
            start_run(params, run_number=i, experiment_file=experiment_file))

    # Wait all
    while any((proc.poll() is None for proc in processes)):
        time.sleep(5)


def start_run(params: dict, run_number: int, experiment_file: str):
    """Execute a single run."""

    # Select a seed for this run
    seed = int(time.time())

    # Select unique directories for this run
    output_base = (
        Path.cwd() / params["output-base"]
        if params["output-base"] else Path.cwd()
    )
    models_path, logs_path = training_paths.get_paths(
        base=output_base,
        scope=params["name"],
        add=(run_number != 0),
    )

    # Compose run-options
    run_options = dict(params)
    run_command = run_options.pop("run-command")
    run_options.pop("n-runs")
    run_options.pop("name")
    run_options.pop("comment")

    run_options["seed"] = seed
    run_options["model-dir"] = str(models_path)
    run_options["logs-dir"] = str(logs_path)

    # Add about this software
    run_options["rl-experiments"] = dict(
        version=pkg_resources.get_distribution("rl_experiments").version
    )

    # Save run options
    options_file = tempfile.NamedTemporaryFile(
        suffix="-run-options.yaml", mode="w+")
    yaml.dump(run_options, options_file)

    # Compose run command
    run_command_comment = (
        "# To re-execute, just change path of --params file\n"
        "#   to the run-options.yaml file in this directory\n")
    run_command = run_command + " --params " + options_file.name

    # Save files
    shutil.copy(experiment_file, logs_path / "experiment.yaml")
    shutil.copy(options_file.name, logs_path / "run-options.yaml")
    with open(logs_path / "run-command.sh", "w") as f:
        f.write(run_command_comment + run_command)
    if params["environment"]["diff"]:
        shutil.copy(
            params["environment"]["diff"],
            logs_path / "environment-diff.patch",
        )
    if params["algorithm"]["diff"]:
        shutil.copy(
            params["algorithm"]["diff"],
            logs_path / "algorithm-diff.patch",
        )

    # Launch
    print("Executing:", run_command)
    time.sleep(2)
    return subprocess.Popen(run_command, shell=True)
