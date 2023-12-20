import random as r
import numpy as np

from linked_list import LinkedList
from client import Client, if_client




def day(k, alpha_dict):
    self_checkout_status = [0 for x in range(6)]
    regular_checkout_status = [0 for x in range(k)]

    queue_dict = {}
    for x in range(k+1):
        queue_name = f"queue{x}"
        queue = LinkedList()
        queue_dict[queue_name] = queue

    for t in range(54000):

        key = int(t/3600) + 8
        alpha = alpha_dict[f'{key}:00-{key+1}:00']

        if if_client(alpha):

            client = Client()
            client.client_age()
            client.checkout_choice()
            client.service_time()

            if client.checkout_choice == 1:
                if 0 in self_checkout_status:
                    self_checkout_status[self_checkout_status.index(0)] = client.service_time
                else:
                    queue_dict['queue5'].insert_at_end(client)

            elif client.checkout_choice == 0:
                if 0 in regular_checkout_status:
                    regular_checkout_status[regular_checkout_status.index(0)] = client.service_time
                else:
                    min = 99999999
                    min_name = ''
                    for queue_name, queue in queue_dict.items():
                        if queue.get_length() < min:
                            min = queue.get_length()
                            min_name = queue_name

                    queue_dict[min_name].insert_at_end(client)

        self_checkout_status = [x - 1 if x > 0 else 0 for x in self_checkout_status]
        regular_checkout_status = [x - 1 if x > 0 else 0 for x in regular_checkout_status]

    if self_checkout_status != [0 for x in range(6)]:
        pass
    if regular_checkout_status != [0 for x in range(k)]:
        pass
