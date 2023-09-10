## Instructions

1) To get started, clone this repository to your local machine:
   <br> git clone https://github.com/haloxil/gds-cc4.git
2) Install the required Python packages using pip:
   <br> pip install -r requirements.txt
3) Run the 1st task:
   <br> python src/restaurants.py
4) Run the 2nd task:
   <br> python src/restaurant_events.py
5) Run the 3rd task:
   <br> python src/threshold.py
6) View all csv outputs on the root folder

## Assumptions and Interpretations

- Assume that populating empty values does not include the string 'Dummy'
- Assume that extracting the list of restaurants that have past events in April 2019 means that as long as April 2019 is within the event start date and event end date, we include that row of data. For example: if the event start date is 30-04-2019 and the event_end_date is 30-05-2019, we do not filter out this row of data.
- When determining the threshold for the different rating text based on aggregate rating, we find the minimum aggregate rating to be classified as that user text rating.

## Design & Deployment Strategy

For this assignment, I have implemented IaC tools such as Terraform to provision a S3 bucket to read various files from AWS. I have commented them out for now as the S3 bucket is not public but I can show you how it works by contacting me for the access and secret keys to run it locally on your laptop as well. I plan to use Terraform to provision other AWS services as well. 
<br><br>
To migrate this assignment onto the cloud, I will be using Lambda for the Python scripts and these scripts will be triggered with EventTrigger upon someone modifying the List of Restaurants file on the S3 bucket. Once Lambda is triggered, it will run and store the csv output files in the same bucket but with a different key path. From there, we can use RedShift for our data lakehouse to create tables and views for further analysis that can be used to build dashboards on PowerBI for example. These AWS services will be monitored with CloudWatch.
<br><br>
These Lambda functions could be deployed using Docker and hosted on AWS ECR. It will be fully CI/CD with GitHub actions workflow to automate deployment, testing and building of code. Adding linting and integration tests to the GitHub Actions workflow is a good practice to ensure code quality and functionality before deploying the Lambda functions.
