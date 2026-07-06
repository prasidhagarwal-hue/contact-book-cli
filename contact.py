class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        # converts object to dict so JSON can save it
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

    def __str__(self):
        return f"Name: {self.name} | Phone: {self.phone} | Email: {self.email}"