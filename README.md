# Quant Dev
**Quant Dev** is a Python toolkit for quantitative finance, engineered for development and analysis of quantitative trading strategies and quantitative risk management.

## Requirements

* Anaconda or Miniconda (Miniconda preferred as it solves conda environments faster). To install Miniconda, follow the link [here](https://docs.anaconda.com/miniconda/install/#).

## Set Up
[Given this repo is still under development, there will be no released version of quant_dev on pip/conda. To use this repo in the meantime, here are the steps you need to set up your machine]:

1. Set your machine's PYTHONPATH environment variable to the quant_dev directory on your machine:
* a) In Windows, type "envir" in the lower left search box, select "Edit environment variables for your account", and set PYTHONPATH to "{YOUR_PATH}/quant_dev"

* b) In Linux, you have to open either the `~/.bash_profile` or `~/.zshrc` file depending on the terminal you are using, go to the end of the file, and paste export PYTHONPATH="{YOUR_PATH}/quant_dev"


2. Create your conda environment:
```
conda env create --name quant -f environment.yml
```

3. Activate your conda environment:
```
conda activate quant
```

4. If you would like to have access to all APIs, you will need the following credentials: [FILL ME IN]
