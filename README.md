# create-an-ec2-instance-than-give-the-tag-name-and-than-terminate-it-by-using-python
Create an EC2 Instance give the tag name and terminate it by using python boto3

An EC2 instance is nothing but a virtual server in Amazon Web services terminology. It stands for Elastic Compute Cloud. It is a web service where an AWS subscriber can request and provision a compute server in AWS cloud.
There are 3 task we have to do 
1.Create the instance
2.Give the tag name
3.Termination

1.Create the instance
Open the cmd prompt  type pip install boto3 to install python boto3
 

After that type pip install awscli to install aws command line interface

 

And than type pip install boto

 


Now after installing boto3 and awscli open browser and open your aws console

After that goto IAM section
 


Now click on add user

 

 




  
 

 
Our new user is created download .csv file
Now open cmd and type command aws configure
 

After that open notepad type the program
 






Now open cmd run the file
 


Now go to aws console goto ec2 instance
 

Our instance is created.




2.Create tag

 
Run the program in cmd
 
 And after the program run open your console

3.Termination

 Type the program

 


Now in cmd run the program
 

After that go to your console and you see your instance is shutting down

 

 
