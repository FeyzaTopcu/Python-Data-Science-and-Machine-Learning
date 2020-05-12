from test import db, Human

""" ###CREATE
db.create_all()
human1 = Human('Arin', 25)

human2 = Human('Mahmut',32)

human3=Human('Hayriye',20)


db.session.add_all([human1,human2,human3])
db.session.commit()

print(human1.id)
print(human2.id)

### """


### READ
""" 
humanx = Human.query.get(2)
print(humanx.name) """

##UPDATE

""" first_human = Human.query.get(1)
first_human.age=55

db.session.add(first_human)
db.session.commit()

print(first_human) """

##DELETE
sec_human= Human.query.get(2)
db.session.delete(sec_human)
db.session.commit()

print(Human.query.get(2))