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
                    min = 99999999
                    min_name = ''
                    for queue_name, queue in queue_dict.items():
                        if queue_name == "queue0":
                            continue
                        if queue.get_length() < min:
                            min = queue.get_length()
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


working_day = {
    '8:00-9:00': 1/150,
    '9:00-10:00': 1/170,
    '10:00-11:00': 1/225,
    '11:00-12:00': 1/250,
    '12:00-13:00': 1/300,
    '13:00-14:00': 1/250,
    '14:00-15:00': 1/150,
    '15:00-16:00': 1/100,
    '16:00-17:00': 1/70,
    '17:00-18:00': 1/50,
    '18:00-19:00': 1/70,
    '19:00-20:00': 1/150,
    '20:00-21:00': 1/200,
    '21:00-22:00': 1/250,
    '22:00-23:00': 1/350
}

day_off = {
    '8:00-9:00': 1/200,
    '9:00-10:00': 1/200,
    '10:00-11:00': 1/190,
    '11:00-12:00': 1/180,
    '12:00-13:00': 1/170,
    '13:00-14:00': 1/160,
    '14:00-15:00': 1/150,
    '15:00-16:00': 1/130,
    '16:00-17:00': 1/130,
    '17:00-18:00': 1/130,
    '18:00-19:00': 1/150,
    '19:00-20:00': 1/200,
    '20:00-21:00': 1/250,
    '21:00-22:00': 1/250,
    '22:00-23:00': 1/200
}

pre_holiday = {
    '8:00-9:00': 1/300,
    '9:00-10:00': 1/280,
    '10:00-11:00': 1/250,
    '11:00-12:00': 1/220,
    '12:00-13:00': 1/190,
    '13:00-14:00': 1/160,
    '14:00-15:00': 1/140,
    '15:00-16:00': 1/120,
    '16:00-17:00': 1/100,
    '17:00-18:00': 1/80,
    '18:00-19:00': 1/60,
    '19:00-20:00': 1/40,
    '20:00-21:00': 1/80,
    '21:00-22:00': 1/150,
    '22:00-23:00': 1/100
}

for i in range(10):
    print(day(5, day_off))