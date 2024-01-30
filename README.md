# Transportation Data Analysis

## Description

This project creates data visualizations for the following transportation datasets:

### United States:

#### Chicago:

CTA bus ridership data: https://rtams.org/media/datasets/cta-ridership
 
## Set up

### Environment creation

Before running an analysis, you must install the nesscary packages. It is recommended that you install them into a conda environment but please to use the environment/container of your choice. Below are instructions for creating a conda environment and installing the required packages into it.

1. Download and install conda from https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
2. Create an environment using the following command:

```
conda create -n transportation_data_analysis --file requirements.txt
```

This will install all of the packages required to run the analysis. 

## Running an analyses

1. Visit the link for Chicago bus ridership mentioned above and download the latest bus ridership dataset. Save this file in a designated directory for analysis inputs.
2. Fork and clone this repository. 
3. Activate the conda environment using the following command:

```
conda activate transportation_data_analysis
```

4. Navigate to the src directory and in the below command, replace FILE_PATH with the absolute path to the bus ridership data and OUTPUT_DIRECTORY with the directory to where you would like all visualizations to be written to.

```
python main.py python --bus_data_path FILE_PATH --output_dir OUTPUT_DIRECTORY
```

5. Run the updated command.
6. Check the output directory you specified and rerun the script as needed.

## Contributing to this project




