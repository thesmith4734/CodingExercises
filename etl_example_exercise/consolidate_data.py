'''
Notes:

    I generally take notes of my thought process during these assessments to give a better idea of my thought process during the creation process

    Initial Thoughts:
    - Reading in files seems simple, to maximize scalability for larger data sets I will look into using gerenrators for loading information from file
    - Though I have little experience with Pandas, I'll look into it more. I think it would apply here, especially with the 'dataframe' terminology
    - Will need to set up a flask server for the bonus objectives, and refresh my memory on using flask's front end capabilities for the simple ui
        - While I have some experience working with react, I am less confident in my Javascript abilities and setting up a front end and backend for something this small doesnt make sense
    
    - Update:
        I have looked into Pandas more and it looks like exactly what I should be using. Looks like the initial problem will be more simple than I thought

        Attempted to use regex expression to load file:

            pd.read_table('./Input/data_source_1/sample_data.2.dat', sep=',|\|')
        
        I learned uses the python engine and will be slower, not good for scalability. 
    
        I researched the csv.Sniffer function, but it does not work with .dat files

        In the interest of time, I will use it the python engine for now, and go back to change it if I have the time.



        Plan:
        Create a master dataframe that all the sample data will be filed into
        Loop through the Input folder
            - load each sample data file, adding a column for where the data came from
            - Merge dataframe with master dataframe
        Create consolidated_output.1.csv file with master dataframe data


'''
import pandas as pd
import os

### Function that collects sample data from multiple files and combines them into one large data set with addition column dictating where the data was sourced
### Input the location foldername for the input data and the desired path for the output file
### returns a combined data set, and creates a csv file of the data set at desired output path
def getInputData(input_foldername, output_file):

    master_dataframe = pd.DataFrame()

    # Loop through the files within given directory
    for root, dirs, files in os.walk(input_foldername, topdown=False):
        # filter files to those with 'sample_data' in the name
        for name in [sample_data for sample_data in files if "sample_data" in sample_data]:
            # Get the dataframe from the file, checking for seperation by either , or | (Requires python engine)
            temp_frame = pd.read_table(os.path.join(root, name), sep=',|\|', engine='python')

            # Add data source column to data frame
            temp_frame['data_source'] = os.path.basename(root)

            # Concatinate the newly created data frame to the master data frame
            master_dataframe = pd.concat([master_dataframe, temp_frame], ignore_index=True)

            # Save master data frame to a csv file
            master_dataframe.to_csv(output_file, index=False)
    return(master_dataframe)


print(f"Consolidated Data:\n\n { getInputData('./Input', 'Output/consolidated_output.csv') }\n")

### Bonus 1 ###

### Function to filter a data set based on the worth of an item.
### Input a file path, and optionally the minimum worth
### Returns a filtered dataframe
def filterWorth(filename, worth=1.00):
        temp_frame = pd.read_table(filename, sep=',|\|', engine='python')
        filtered_frame = temp_frame[temp_frame['worth'] > worth]
        return(filtered_frame)

    

print(f"Filtered By Worth:\n\n { filterWorth('./Input/data_source_1/sample_data.1.csv') }\n")

### Function to recalculate the worth of a sample set of data by multiplying its worth by th material id
### Input a file path
### Returns a data frame with recalculated worth 
def recalculateWorth(filename):
    data_frame = pd.read_table(filename, sep=',|\|', engine='python')
    data_frame['worth'] = data_frame['worth'] * data_frame['material_id']
    return(data_frame)

print(f"Modified Worth:\n\n { recalculateWorth('./Input/data_source_2/sample_data.3.dat') }\n")

### Function to aggregate multiple rows of the same product name in a single data set
### Input a file path
### Returns a data frame with duplicate rows condensed base on the following rules: first rows quality, highest value of material_id, a summation of all duplicates worth
def aggregateData(filename):
    data_frame = pd.read_table(filename, sep=',|\|', engine='python')
    data_frame = data_frame.groupby('product_name').agg({'quality':'first',
                                            'material_id':'max',
                                            'worth':'sum'})
    return(data_frame)

print(f"Aggregated Data:\n\n { aggregateData('./Input/data_source_1/sample_data.2.dat') }\n")

### Function to replace the material id of a data set with the corrasponding value of a given material file table
### Input a data file and a material reference file
### Returns the same data set with the material id column values replaced with corrasponding material refernce values
def replaceMaterial(data_file, material_file):
    data_frame = pd.read_table(data_file, sep=',|\|', engine='python')
    material_df = pd.read_table(material_file, sep=',|\|', engine='python')
    material_dict = dict(material_df.values)
    data_frame = data_frame.replace({'material_id': material_dict})
    return(data_frame)

print(f"Replace Material ID:\n\n { replaceMaterial('./Output/consolidated_output.csv', './Input/data_source_2/material_reference.csv') }\n")
