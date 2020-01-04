# BA model

Simulation code of Barabasi-Albert model written in Python.
https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model

## Prerequisites

- Python 3
- networkx
- matplotlib
- powerlaw

To install prerequisites, run `pipenv install`.

## Usage

Input parameters for this simulator are the following.

- N : number of nodes (integer)
- m : number of links for new nodes (integer)
- seed : seed of random number generator (integer)

To run the simulator, give the above parameters as arguments of `run_BA.sh`.

```
./run_BA.sh 10000 5 1234
```

When the simulation is complete, degree exponent $alpha$ and $x_min$ are estimated using the `powerlaw` package.
You will find two files `pk.png` and `_output.json`. The png file shows the degree distribution like the following.

![snapshot](https://raw.githubusercontent.com/yohm/sim_BA_model/master/sample/pk.png)

The json file contains the estimated degree exponent and $x_min$.

```json:_output.json
{"alpha": 2.8234382407147103, "x_min": 7.0}
```

## Using with OACIS

To register this simulation code to OACIS, run the following code. It will clone the repository, run `pipenv install`, and registers the simulator on OACIS.

```sh
curl -fsSL https://raw.githubusercontent.com/yohm/sim_BA_model/master/setup.sh | bash
```

If you're using [oacis_docker](https://github.com/crest-cassia/oacis_docker), run the following command.

```sh
docker exec -it -u oacis my_oacis bash -lc "curl -fsSL https://raw.githubusercontent.com/yohm/sim_BA_model/master/setup.sh | bash"
```

