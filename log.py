# ! /usr/bin/env python3

import psycopg2

dbname = "news"


# 1. What are the most popular three articles of all time?
query1 = '''select articles.title, count(*)
            from articles, log
            where log.path = '/article/' || articles.slug
            group by articles.title
            order by count(*) desc
            limit 3;'''

# 2. Who are the most popular article authors of all time?
query2 = '''select authors.name, count(*)
            from log, articles, authors
            where log.path = '/article/' || articles.slug
            and articles.author = authors.id
            group by authors.name
            order by count(*) desc;'''

# 3. On which days did more than 1% of requests lead to errors?
query3 = '''select * from (select date(time),
            round(100.0*sum(case log.status
            when '200 OK' then 0 else 1 end)/count(log.status),3)
            as error
            from log
            group by date(time)
            order by error desc) as subq
            where error > 1;'''


# connect to database
def make_query(query):
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()

# results
print ("1.the most popular 3 articles: ")
print (make_query(query1))
print ("2.the most popular article authors: ")
print (make_query(query2))
print ("3.Days with greater than 1% errors: ")
print (make_query(query3))
