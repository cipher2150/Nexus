import time

from customer_simulator import CustomerSimulator
from producer import EventProducer


def main():

    simulator = CustomerSimulator(total_users=1000)

    producer = EventProducer()

    print("=" * 60)
    print(" Real-Time Customer Event Generator Started ")
    print("=" * 60)

    try:

        while True:

            event = simulator.generate_event()

            producer.send(event)

            print(event.to_dict())

            # Generate ~2 events per second
            time.sleep(0.5)

    except KeyboardInterrupt:

        print("\nStopping producer...")

    finally:

        producer.producer.close()

        print("Producer closed successfully.")


if __name__ == "__main__":
    main()