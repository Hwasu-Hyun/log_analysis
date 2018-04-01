# Log Analysis Project 
This is [Full Stack Web Developer Nanodegree of Udacity](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/079be127-2d22-4c62-91a8-aa031e760eb0)

## Project Description
Build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
The database contains newspaper articles, authors and the web server log. 
Using that information, This code will answer questions about the site's user activity.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 

## How to run 
1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/). 
2. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm).
3. Clone this [repository](https://github.com/Hwasu-Hyun/log_analysis).
4. Download the database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
5. Run **vagrant up** and **vagrant ssh** command.
6. Use command **psql -d news -f newsdata.sql** to connect database.
7. Run **python3 logs.py**.
