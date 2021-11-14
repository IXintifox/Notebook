Implementation of the RNN model used in "Exploring the GDB-13 chemical space using deep generative models"
======================================================================================================

> **NOTE:** This repository has been archived because a newer one has been created with additional features. The code here is left only to complement the [previously published article](https://chemrxiv.org/articles/Exploring_the_GDB-13_Chemical_Space_Using_Deep_Generative_Models/7172849).
>
> Please have a look at [undeadpixel/reinvent-randomized](https://github.com/undeadpixel/reinvent-randomized) for the improved software.

This code allows to create, train and sample RNN with the architecture described in:

[Exploring the GDB-13 Chemical Space Using Deep Generative Models](https://chemrxiv.org/articles/Exploring_the_GDB-13_Chemical_Space_Using_Deep_Generative_Models/7172849)

Also find an already trained model with a 1M random sample of GDB-13 in the `trained_models` folder.

Install
-------
A [Conda](https://conda.io/miniconda.html) `environment.yml` is supplied with all the required libraries.

~~~~
$> conda env create -f environment.yml
$> source activate reinvent-gdb13
(reinvent-gdb13) $> ./create_model.py -h
usage: create_model.py [-h] --input-smiles-path INPUT_SMILES_PATH
                       --output-model-path OUTPUT_MODEL_PATH
                       [--num-gru-layers NUM_GRU_LAYERS]
                       [--gru-layer-size GRU_LAYER_SIZE]
                       [--embedding-layer-size EMBEDDING_LAYER_SIZE]

Create a model with the vocabulary extracted from a SMILES file.

optional arguments:
  -h, --help            show this help message and exit
  --input-smiles-path INPUT_SMILES_PATH, -i INPUT_SMILES_PATH
                        SMILES to calculate the vocabulary from. The SMILES
                        are taken as-is, no processing is done.
  --output-model-path OUTPUT_MODEL_PATH, -o OUTPUT_MODEL_PATH
                        Prefix to the output model.
  --num-gru-layers NUM_GRU_LAYERS, -n NUM_GRU_LAYERS
                        Number of GRU layers of the model [DEFAULT: 3]
  --gru-layer-size GRU_LAYER_SIZE, -s GRU_LAYER_SIZE
                        Size of each of the GRU layers [DEFAULT: 512]
  --embedding-layer-size EMBEDDING_LAYER_SIZE, -e EMBEDDING_LAYER_SIZE
                        Size of the embedding layer [DEFAULT: 256]
~~~~

General Usage
-------------
Three tools are supplied. By default the parameters are set to match those used in the publication. To get further information about the tool, please run the help implemented in each of them, or look at the examples below.

1) Create Model (`create_model.py`): Creates a blank model file.
2) Train Model (`train_model.py`): Trains the model with the specified parameters.
3) Sample Model (`sample_from_model.py`): Samples an already trained model for a given number of SMILES. It can also retrieve the log-likelihood in the process.

Usage example
-------------

Create, train and sample a network as in the publication.
~~~~
(reinvent-gdb13) $> mkdir gdb13_models
(reinvent-gdb13) $> ./create_model.py -i training_set.smi -o gdb13.1M.model.empty
(reinvent-gdb13) $> ./train_model.py -i gdb.13.1M.model.empty -o gdb13_models/model -s training_set.smi --num-epochs=200 --lrcs=0.9772 --save-every-n-epochs=1
# (... wait 24-48h ...)
(reinvent-gdb13) $> ./sample_from_model.py gdb13_models/model.70 -n 1000000 --with-likelihood -o sample.smi
~~~~
