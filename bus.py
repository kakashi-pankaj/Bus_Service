pickup = ['jaipur', 'jodhpur', 'delhi', 'pune', 'bangalore']
drop = ['jaipur', 'mumbai', 'delhi', 'pune', 'gurugram']
tickets = []


class Ticket:

    def __init__(self, source, destination, name, age):
        self.source = source
        self.destination = destination
        self.name = name
        self.age = age

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)


class BusService:

    def add_ticket(self, ticket: Ticket):
        if type(ticket) == Ticket:
            if ticket.source not in pickup:
                print("Invalid source location")
            elif ticket.destination not in drop:
                print("Invalid destination location")
            elif not(ticket.name.isalpha()):
                print("Name can only contain Alphabets")
            elif not (0 < ticket.age < 100):
                print(' Invalid age')
            else:
                tickets.append(ticket)
                pnr = service.pnr(ticket)
                print('Ticket created successfully')
                print(f'Your pnr is {pnr}')

        else:
            print('Invalid ticket type')

    def cancel_ticket(self, ticket: Ticket):
        if type(ticket) == Ticket:
            if ticket in tickets:
                tickets.remove(ticket)
            else:
                print('ticket not in database')
        else:
            print('invalid ticket type')

    def update_ticket(self):
        pass

    def pnr(self, ticket):
        ind = tickets.index(ticket)
        pnr = int(100) + ind
        for i in tickets:
            if i == ticket:
                ticket['pnr'] = pnr
        return pnr


def check_availability():
    tpickup = input('Enter source location: ')
    tdrop = input('Enter destination location: ')
    if tpickup == tdrop:
        print('Source and destination cannot be same')
    else:
        if tpickup in pickup and tdrop in drop:
            print("Bus route is available")
        else:
            print("Bus route is not available")


def get_user_input():
    tpickup = input('Enter pickup location: ')
    tdrop = input('Enter drop location: ')
    tname = input('Enter passenger name: ')
    tage = int(input('Enter passenger age: '))
    return Ticket(source=tpickup, destination=tdrop, name=tname, age=tage)


def add_ticket():
    ticket = get_user_input()
    service.add_ticket(ticket)


def cancel_ticket():
    pass


def update_ticket():
    pass


def all_tickets():
    print(tickets)


def choice():
    ch = input('Do you want to continue? [yes/y/no/n]')
    if ch.lower() in ['yes', 'y', 'no', 'n']:
        if ch.lower() in ['no', 'n']:
            return False
        else:
            return True
    else:
        print('Invalid input')
        choice()


if __name__ == '__main__':

    service = BusService()
    flag = True
    while flag:
        print('''
        1. Check bus availability between routes
        2. Add bus ticket
        3. Cancel bus ticket
        4. update bus ticket 
        5. print all tickets
        ''')

        operations = {
            1: check_availability,
            2: add_ticket,
            3: cancel_ticket,
            4: update_ticket,
            5: all_tickets
        }
        op = int(input('Choose Operation: '))
        operations.get(op)()
        flag = choice()
