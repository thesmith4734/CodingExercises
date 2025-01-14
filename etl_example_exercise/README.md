# There were a couple of differences in the files I recieved for this assignment and the repository I was directed to:
* The main and __init__ files were not present, so I created a consolidate_data.py file where the assignment is completed
* The sample_data.2.dat had a different seperator ( | instead of , )
* I have included an api.py file for a quick flask backend I was experimenting with
* During the interview, another assessment was given. It is explained and solved in the file newfile.py

# Sample ETL Exercise
### Write a program/script that performs the following:
* Reads the 3 sample_files.* in Input/data_source_1/ and Input/data_source_2/ folders into a dataframe
* Consolidates the data from each file into a single dataframe
* Create a new column that will help track which data source the products originally came from
* Saves to a new output file in the Output dir using the name consolidated_output.1.csv
* Try to make this as 'production-ready' as possible - consider readability, stability, scalability and performance
* Consider building this so that it is easy to include new files to this process.

### Not required but would be nice to try the below bonuses:

#### Bonus 1:
* The `sample_data.1` file has a number of products we do not want in our output. Filter this data so that the only products that remain are products with a `worth` of MORE than `1.00`
* The true worth of products in `sample_data.3` is based on the listed `worth` TIMES the `material_id`, recalculate the `worth` for this file to show that.
* Products in `sample_data.2` have indivudal parts listed as separate products. Aggregate this data on `product_name`, keeping the FIRST `quality`, MAX `material_id`, and SUM of `worth`
* Load and use the `material_reference` data file to get the material name for each product in the final dataframe
* Write functionality that would also load the consolidated dataframe to a table in a database (this can be largely stubbed or mocked out - especially any actual DB calls)

#### Bonus 2:
* Build a simple rest api framework (Django or Flask preferred) to return data from the consolidate_output file
* Feel free to come up with a few endpoints that make sense with the data, below are a few example ideas
    * Take quality as a parameter and return all products of that type (as json)
    * Take a list of product names and return of their worth

#### Bonus 3:
* Build a simple UI to show the data (your choice of language/framework)