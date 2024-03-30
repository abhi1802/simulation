import simpy
import random

# Constants
AVERAGE_ARRIVAL_TIME = 5  # Average time between vessel arrivals in hours
NUM_CONTAINERS_PER_VESSEL = 150
NUM_BERTHS = 2
NUM_CRANES = 2
NUM_TRUCKS = 3
CRANE_OPERATION_TIME = 3  # Time to move one container in minutes
TRUCK_ROUND_TRIP_TIME = 6  # Time for a round trip by truck in minutes

class ContainerTerminal:
    def __init__(self, env):
        self.env = env
        self.berth = simpy.Resource(env, NUM_BERTHS)
        self.cranes = simpy.Resource(env, NUM_CRANES)
        self.trucks = simpy.Resource(env, NUM_TRUCKS)

    def discharge_vessel(self, vessel_name):
        """Process to discharge containers from a vessel using cranes and trucks."""
        with self.berth.request() as berth_request:
            yield berth_request
            print(f"{vessel_name} has berthed at time {env.now}")
            
            for _ in range(NUM_CONTAINERS_PER_VESSEL):
                with self.cranes.request() as crane_request, self.trucks.request() as truck_request:
                    yield crane_request & truck_request
                    yield env.timeout(CRANE_OPERATION_TIME)
                    print(f"{vessel_name} has a container moved by crane at time {env.now}")
                    env.process(self.truck_transport(vessel_name))
            
            print(f"{vessel_name} has discharged all containers at time {env.now}")

    def truck_transport(self, vessel_name):
        """Simulates the truck transporting a container to the yard."""
        yield env.timeout(TRUCK_ROUND_TRIP_TIME)
        print(f"A truck has transported a container from {vessel_name} to the yard at time {env.now}")

def vessel_generator(env, terminal):
    """Generates vessels arriving at the terminal."""
    for i in range(100):  # Assuming a finite number of vessels for demonstration
        yield env.timeout(random.expovariate(1.0 / AVERAGE_ARRIVAL_TIME))
        env.process(terminal.discharge_vessel(f"Vessel {i+1}"))

env = simpy.Environment()
terminal = ContainerTerminal(env)
env.process(vessel_generator(env, terminal))
env.run(until=720)  # Run the simulation for 1 day (1440 minutes)
