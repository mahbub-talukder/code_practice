select NAME from CITY where COUNTRYCODE = 'USA' AND POPULATION > 120000


/*

Samantha interviews many candidates from different colleges using coding challenges and contests. Write a query to print the contest_id, hacker_id, name, and the sums of total_submissions, total_accepted_submissions, total_views, and total_unique_views for each contest sorted by contest_id. Exclude the contest from the result if all four sums are .

Note: A specific contest can be used to screen candidates at more than one college, but each college only holds  screening contest.
*/





select 
cnt.contest_id,
cnt.hacker_id,
cnt.name,
sum(sub_stats.total_submissions)  sum_total_submissions,
sum(sub_stats.total_accepted_submissions)  sum_total_accepted_submissions,

sum(stats.total_views) sum_total_views,
sum(stats.total_unique_views) sum_total_unique_views


from Contests cnt
inner join Colleges clg on cnt.contest_id =  clg.contest_id
inner join Challenges chalng on chalng.college_id = clg.college_id
inner join View_Stats stats on stats.challenge_id =  chalng.challenge_id
inner join Submission_Stats sub_stats on sub_stats.challenge_id =  chalng.challenge_id

-- where (sum_total_submissions+sum_total_accepted_submissions+sum_total_views+sum_total_unique_views) !=0


"""problem : 1
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters.
Your result cannot contain duplicates.

"""
-- select distinct(city)

-- from station 
-- where lower(substring(city,-1,1)) in ('a','e','i','o','u') and  lower(substring(city,1,1)) in ('a','e','i','o','u')

"""problem 2:

Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name.
 If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.),
  secondary sort them by ascending ID.
"""
-- select name
-- from students 
-- where marks > 75
-- order by right(name,3),id asc