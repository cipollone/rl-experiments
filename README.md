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
training algorithm. From a code perspective, this does almost nothing. What
matters instead is the convention that we adopt regarding what a generic
training algorithm should have as input and outputs.

The input is a Yaml file containing a specification of an experiment. To see
the accepted format call:

	python -m rl_experiments show-format experiment.yaml

If you want to understand the fields, print it with comments, with the
`--comments` option. In this case, you may need to also show the format of
nested configurations.

Any training algorithm is expected to accept a `--params` option that allows
to receive a file in the `run-options.yaml` format (you may still use
`show-format` command to understand it). The algorithm must respect the given
seed, and assign it everywhere is needed.

We expect the algorithm to generate a file in the `run-outcome.yaml` format.
