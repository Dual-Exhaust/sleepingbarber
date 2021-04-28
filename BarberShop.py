import random
import time
from threading import Thread, Event
import logging

# sets the logging level to INFO, default is WARNING
# also formats the logging to show time
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')


class Barber:
    # event class works with threads
    barberAction = Event()

    # makes the thread wait
    def sleep(self):
        self.barberAction.wait()

    # awakens the thread waiting for the barber to wake up
    def wake_up(self):
        self.barberAction.set()

    # sleeps the thread for a certain amount of time while the barber is busy giving a haircut
    def cut_hair(self, customer):
        # sets the internal flag back to false, blocking the thread from further action until the haircut is done
        self.barberAction.clear()

        logging.info('%s is getting a haircut.', customer)
        # Cuts hair for 45 to 60 seconds
        time.sleep(random.randrange(15, 30))
        logging.info('%s is done with their haircut.', customer)


class BarberShop:
    # list of people waiting to get their haircut
    waiting = []

    def __init__(self, barb, seats):
        self.barber = barb
        self.seats = seats

    def open_shop(self):
        logging.info('Barber shop is opening. There are %s seats available.', self.seats)
        thr = Thread(target=self.start_work)
        thr.start()

    def start_work(self):
        while True:
            # checks if there is anyone waiting
            if len(self.waiting) > 0:
                # get the first person waiting and then remove them from the list
                person = self.waiting[0]
                del self.waiting[0]
                # tell the barber to cut the persons hair
                self.barber.cut_hair(person)
            else:
                logging.info('There is nobody waiting for a haircut so the barber falls asleep.')
                # the barber goes to sleep, 'pauses' the thread
                barber.sleep()
                # when someone enters the thread is awakened, picking up here
                logging.info('A customer has entered and the barber wakes up.')

    def enter_shop(self, customer):
        logging.info('%s entered the waiting room.', customer)

        # checks if the waiting room is full
        if len(self.waiting) == self.seats:
            logging.info('There are no seats available so %s leaves.', customer)
        else:
            logging.info('%s finds a seat in the waiting room.', customer)
            # add a new customer to the waiting list
            self.waiting.append(customer)
            barber.wake_up()


if __name__ == '__main__':
    people = ['Peter', 'Quagmire', 'Joe', 'Cleveland']
    barber = Barber()
    barberShop = BarberShop(barber, seats=2)
    barberShop.open_shop()

    while len(people) > 0:
        # get customer from the list of customers
        person = people.pop()
        # customer enters the shop
        barberShop.enter_shop(person)
        # time in between customers
        time.sleep(random.randrange(3, 10))
