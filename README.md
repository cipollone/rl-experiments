# RL Experiments

A protocol / template for Reinforcement learning experiments.

## Install
This package can be installed as usual:

    pip install .

Or, we can install a specific tested version of this package and its dependencies with:

    poetry install --no-dev

Omit the `--no-dev` option if you're installing for local development.

## Run
If installed with poetry, you can run the main function with:

    poetry run python -m rl_experiments

Or simply omit `poetry run` if installed with pip. Obtain help with `--help` option.


## Use

This tiny software executes a training command and passes options to the
training algorithm. The actual code is small. What matters instead is the
convention that we adopt regarding what a generic training algorithm should
have as input and outputs.

The input for this program is a Yaml file containing a specification of an
experiment. This file is in a format that we call `experiment.yaml`. To see its
content, run:

	python -m rl_experiments show-format experiment.yaml

As you can see, the `show-format` command shows how a specific file format
should be. If you want to start from this basic file as a template, just
redirect it to a file. In linux we could write
`show-format format-name.yaml > format-name.yaml`. To better understand the
fields of a format, you could use the `--comments` option. In this case,
nested formats won't be substituted, and you may also need to show the format
of nested configurations.

The training algorithm that this small program will start is any executable
that accept a `--params "file-path".yaml` option as last argument. The
`"file-path".yaml` is a file of parameters in the `run-options.yaml` format.
The algorithm must respect the given seed (assign it everywhere is needed) and
output directories. It should also allow indipendent runs.

Even though not strictly necessary, we expect the algorithm to generate a file
in the `run-outcome.yaml` format.
