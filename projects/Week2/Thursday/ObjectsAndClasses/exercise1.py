class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0


    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

    def print_contact_info(self):
        print self.name
        print self.email
        print self.phone

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        return len(self.friends)

    def greeting_count(self):
        print len(self.people_greeted)

    def __repr__(self):
        return '' % (self.name, self.email, self.phone)



sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
sonny.greet(jordan)
jordan.greet(sonny)

sonny.print_contact_info

sonny.add_friend('jordan')

sonny.num_friends()

sonny.greeting_count()

