from linked_list import LinkedList
from client import Client, if_client


def check_queues(queue_dict):
    for queue_name, queue in queue_dict.items():
        if queue.get_length() != 0:
            return 1
    return 0


def iteration(regular_checkout_status, self_checkout_status, queue_dict, waiting_time):
    for idx, checkout_status in enumerate(regular_checkout_status):
        if checkout_status <= 0 and queue_dict[f'queue{idx + 1}'].get_length() != 0:
            regular_checkout_status[idx] = queue_dict[f'queue{idx + 1}'].head.data
            queue_dict[f'queue{idx + 1}'].remove_at(0)

    for idx, checkout_status in enumerate(self_checkout_status):
        if checkout_status <= 0 and queue_dict['queue0'].get_length() != 0:
            self_checkout_status[idx] = queue_dict['queue0'].head.data
            queue_dict[f'queue0'].remove_at(0)

    for queue_name, queue in queue_dict.items():
        if queue.get_length() > 0:
            waiting_time += queue.get_length()

    self_checkout_status = [x - 1 if x > 0 else 0 for x in self_checkout_status]
    regular_checkout_status = [x - 1 if x > 0 else 0 for x in regular_checkout_status]

    return regular_checkout_status, self_checkout_status, queue_dict, waiting_time


def day(k, alpha_dict):
    waiting_time = 0
    clients = 0

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
            clients += 1

            client = Client()
            client.client_age()
            client.client_checkout_choice()
            client.client_service_time()

            if client.checkout_choice == 1:
                if 0 in self_checkout_status:
                    self_checkout_status[self_checkout_status.index(0)] = client.service_time
                else:
                    queue_dict['queue0'].insert_at_end(client.service_time)

            elif client.checkout_choice == 0:
                if 0 in regular_checkout_status:
                    regular_checkout_status[regular_checkout_status.index(0)] = client.service_time
                else:
                    min_name = ''
                    mini = 9999999
                    for queue_name, queue in queue_dict.items():
                        if queue_name == "queue0":
                            continue
                        if queue.get_length() < mini:
                            mini = queue.get_length()
                            min_name = queue_name

                    queue_dict[min_name].insert_at_end(client.service_time)

        regular_checkout_status, self_checkout_status, queue_dict, waiting_time = iteration(regular_checkout_status,
                                                                                            self_checkout_status,
                                                                                            queue_dict, waiting_time)

    while self_checkout_status != [0 for x in range(6)] or regular_checkout_status != [0 for x in range(k)] or \
            check_queues(queue_dict):
        regular_checkout_status, self_checkout_status, queue_dict, waiting_time = iteration(regular_checkout_status,
                                                                                            self_checkout_status, queue_dict,
                                                                                            waiting_time)

    return waiting_time/clients

