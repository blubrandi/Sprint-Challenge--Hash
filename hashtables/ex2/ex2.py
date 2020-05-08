#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):

    ticket_list = {}
    route = []

    for ticket in tickets:
        ticket_list[ticket.source] = ticket.destination

    next_flight = ticket_list["NONE"]

    while next_flight != "NONE":
        route.append(next_flight)
        next_flight = ticket_list[next_flight]

    route.append("NONE")
    
    return route








    # turn list into dictionary with the source as the key and the dest as value

    # if the source (key) is None set that as the starting ticket
    # current_flight = ticket_list["NONE"]
    
    # the destination None will be the end ticket
    # while source is not None, if next ticket source is starting

    # ticket_list = dict.fromkeys(tickets)
    # print(ticket_list)
    #
    # starting_ticket =
    #
    # for ticket in ticket_list:
    #     print(ticket.source, ticket.destination)
    #
    #     while ticket.source is None:


    # return route
