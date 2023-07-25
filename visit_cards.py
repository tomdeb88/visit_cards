from faker import Faker

fake = Faker()


class VisitCard:
    list = []

    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email
        VisitCard.list.append(self)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    def contact(self):
        return f"Kontaktuje sie z {self.first_name} {self.last_name} {self.email}"

    @property
    def how_many_chars(self):
        chars_number = len(self.first_name) + len(self.last_name)
        return chars_number


person_1 = VisitCard("Michal", "Zamojc", "Sklep", "sprzedawca", "kupmnie@op.pl")
person_2 = VisitCard("Anna", "Mailina", "Deichman", "manager", "arkauft@o2.pl")
person_3 = VisitCard("Andrzej", "Juskowiak", "ksw", "bokser", "punchme@qu.pl")
person_4 = VisitCard("Roman", "Adamowicz", "Dino", "kasjer", "cashier@df.pl")
person_5 = VisitCard("Kamil", "Xolab", "magazyn", "wozny", "woznix@rt.en")
person_6 = VisitCard("Kami", "Bolab", "agazyn", "wozny", "znix@rt.en")
person_7 = VisitCard("Zygmunt", "Zolab", "agazyn", "wozny", "xoznix@rt.en")

for i in VisitCard.list:
    print("{} {} ---- {}".format(i.first_name, i.last_name, i.email))


def make_visit_card():
    person = VisitCard(
        fake.first_name(), fake.name(), fake.company(), fake.job(), fake.safe_email()
    )
    return person


by_first_name = sorted(VisitCard.list, key=lambda name: name.first_name)

for i in by_first_name:
    print(i)

print("------------------------------------------------------------")
by_last_name = sorted(VisitCard.list, key=lambda name: name.last_name)

for i in by_last_name:
    print(i)
print("------------------------------------------------------------")
by_email = sorted(VisitCard.list, key=lambda name: name.email)

for i in by_email:
    print(i)


# lista=["monika",'oliwia',"zaneta","yabol","adam","nowak"]
# lista2=VisitCard.list

# nowa_lista=sorted()

print(person_2.contact())
print(person_1.how_many_chars)
