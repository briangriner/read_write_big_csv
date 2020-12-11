# read_write_big_csv
Data engineering example where the challenge was to automate creation of a summary report in .csv format from a data source too big to read into memory. Small cut of original file included. 

run.sh is a shell script for automation of the report. To run in linux: ./run.sh 
Be sure to check the permissions on your system using: ls -l run.sh
To change the permissions to executable: chmod +x run.sh (or use octal 775 or 755 instead of +x)

TO DOs: 
- Add regex to manage records with unquoted address fields containing commas
- Update to add summary statistics






