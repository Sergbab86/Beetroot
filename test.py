class Client:
    def __init__(self, name: str, last_name: str, birth_year: int, total: int, city: str):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.total = total
        self.city = city


class VipClient(Client):
    def __init__(self, name, last_name, birth_year, total, city, birth_date, vip_level: int):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.total = total
        self.city = city
        self.birth_date = birth_date
        self.vip_level = vip_level
        self.birth_year = None
        # super().__init__(name, last_name, birth_year, total, city)

    def __str__(self):
        return f"{self.name} {self.last_name}, {self.birth_year}, {self.total}, {self.city}, {self.birth_date}, {self.vip_level}"

    def __repr__(self):
        return f"{type(self.name)}"  # , type(self.last_name), type(self.birth_year), type(self.total), type(self.city), \
        # type(self.birth_date), type(self.vip_level)

    def change_vip(self, vip_level: int):
        self.vip_level = vip_level


first_client = VipClient("Vika", "Panina", 2000, 100000, "Kyiv", "01-01-2000", 5)
# print(first_client)
print(str(first_client))
# print(str(Client))
print(repr(first_client))
first_client.change_vip(4)
print(str(first_client))
