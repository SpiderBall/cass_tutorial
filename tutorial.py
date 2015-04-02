from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('demo')

session.execute("""
 
insert into users (lastname, age, city, email, firstname) values ('Jones', 35, 'Austin', 'bob@example.com', 'Bob')
 
""")

result = session.execute("select * from users where lastname='Jones' ")[0]
print result.firstname, result.age

session.execute("update users set age = 36 where lastname = 'Jones'")
result = session.execute("select * from users where lastname='Jones' ")[0]
print result.firstname, result.age
 
session.execute("delete from users where lastname = 'Jones'")
result = session.execute("select * from users")
for x in result: print x.age
