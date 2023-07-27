from faker import Faker

fake = Faker()


class VisitCard:
    list = []

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.list.append(self)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    @property
    def label_length(self):
        chars_number = len(self.first_name + self.last_name)
        return chars_number


class BaseContact(VisitCard):
    def __init__(self, first_name, last_name, email, phone):
        super().__init__(first_name, last_name, email)
        self.phone = phone

    def contact(self):
        print(
            f"Wybieram numer {self.phone} i dzwonie do {self.first_name} {self.last_name}"
        )


class BusinessContact(BaseContact):
    def __init__(
        self, first_name, last_name, email, phone, position, company, business_phone
    ):
        super().__init__(first_name, last_name, email, phone)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.position} {self.company}"

    def contact(self):
        print(
            f"Wybieram numer {self.business_phone} i dzwonie do {self.first_name} {self.last_name}"
        )


nowy = BaseContact("Tomasz", "Wer", "tomwer@wp.pl", "54741458")
nowy_business = BusinessContact(
    "Ania",
    "Smietana",
    "547452145",
    "ert@wp.pl",
    "tenisistka",
    "wimbleddon ltd",
    "555666999",
)

nowy.contact()
nowy_business.contact()
print(nowy_business.label_length)


def create_contacts(kind_of_visitcard, number_of_cards):
    if kind_of_visitcard == "basecontact":
        for card in range(number_of_cards):
            person = BaseContact(
                fake.first_name(), fake.name(), fake.safe_email(), fake.phone_number()
            )
    elif kind_of_visitcard == "businesscontact":
        for card in range(number_of_cards):
            person = BusinessContact(
                fake.first_name(),
                fake.name(),
                fake.safe_email(),
                fake.phone_number(),
                fake.job(),
                fake.company(),
                fake.phone_number(),
            )


pierwszy = create_contacts("businesscontact", 4)

for i in VisitCard.list:
    print(i)
