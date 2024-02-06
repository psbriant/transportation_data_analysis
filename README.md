# Transportation Data Analysis

## Description

This project creates data visualizations for the following transportation datasets:

### United States:

#### Chicago:

CTA bus ridership data: https://rtams.org/media/datasets/cta-ridership
 
## Set up

Before doing anything please fork and clone this repository. 

### Environment creation

Before running an analysis, you must install the necessary packages. It is recommended that you install them into a [conda environment](https://docs.conda.io/en/latest/) but please to use the environment/container of your choice. Below are instructions for creating a `conda` environment and installing the required packages into it.

1. Download and install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
2. Create an environment using the following command:

```
conda env create -f environment.yml
```

This will install all of the packages required to run the analysis. 

## Running an analyses

1. Visit the link for Chicago bus ridership mentioned in the [description section](#Description) and download the latest bus ridership dataset. Save this file in a designated directory for analysis inputs.

2. Activate the `conda` environment using the following command:

```
conda activate transportation_data_analysis
```

3. Navigate to the `src` directory and in the below command, replace `FILE_PATH` with the absolute path to the bus ridership data and `OUTPUT_DIRECTORY` with the directory to where you would like all visualizations to be written to.

```
python main.py --bus_data_path FILE_PATH --output_dir OUTPUT_DIRECTORY
```

4. Run the updated command.
5. Check the output directory you specified and rerun the script as needed.

## Contributing to this project

### Reporting a bug

To report a bug, please create an issue, tag it as a `bug` and write a short description of the problem and attach a screenshot of any error message.

### Suggesting a new feature

To suggest a new feature, please create an issue, tag it as a `enhancement` and write a short description of what you would like to see added.

### Setting up an development environment

Since this project is not currently a package, you can use the transportation_data_analysis environment to make modifications and run tests.

### Making modifications

When making modifications, please create a new branch and submit a pull request when you are ready to merge with the `main` branch. Please refrain from making changes on `main`.

### Running tests

For any function you add, please add tests for any outputs and any exceptions that are raised. This project currently has a test framework that uses [pytest](https://docs.pytest.org/en/8.0.x/) as a test runner. [Github actions](https://docs.github.com/en/actions) is currently setup to run all tests when someone tries to merge a pull request. You can also run tests from any directory within the `transportation_data_analysis` repo using the following command:

```
pytest
```
