import random as r


def if_client(alpha):
    if r.random() < alpha:
        return 1
    else:
        return 0


class Client:
    time_ratio_dict = {'10': 1.2, '20': 1.4, '30': 1.6, '40': 1.8, '50': 2.0, '60': 2.2, '70': 2.4, '80': 2.6,
                       '90': 2.8}

    def __init__(self):
        self.age = None
        self.service_time = None
        self.checkout_choice = None
        self.age_str = None

    def client_age(self):
        self.age = round(r.gauss(40, 20))
        self.age_str = str(self.age)
        if self.age < 10:
            self.client_age()
        if self.age > 99:
            self.client_age()

    def client_checkout_choice(self):
        prob = -0.8*self.age + 80
        if r.random() < prob:
            self.checkout_choice = 1
        else:
            self.checkout_choice = 0

    def client_service_time(self):
        if self.checkout_choice == 1:
            self.service_time = round(r.gauss(400, 100)*self.__class__.time_ratio_dict[f'{self.age_str[0]}0'])
        elif self.checkout_choice == 0:
            self.service_time = round(r.gauss(400, 100))

