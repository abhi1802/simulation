import simpy
import random

# Constants
MEAN_ARRIVAL_TIME = 5 * 60  # Average time between arrivals in minutes
CONTAINERS_PER_VESSEL = 150  # Number of containers per vessel
QUAY_CRANE_MOVE_TIME = 3  # Time it takes to move one container in minutes
TRUCK_ROUND_TRIP_TIME = 6  # Round trip time for a truck in minutes
SIMULATION_TIME = 24 * 60  # Simulation time in minutes (e.g., 1 day)

class ContainerTerminal:
    def __init__(self, env):
        self.env = env
        self.berth = simpy.Resource(env, capacity=2)
        self.cranes = simpy.Resource(env, capacity=2)
        self.trucks = simpy.Resource(env, capacity=3)

    def discharge_vessel(self, vessel_name):
        # Simulate berthing the vessel
        with self.berth.request() as berth_req:
            yield berth_req
            print(f'{env.now}: {vessel_name} has berthed.')
            
            # Simulate discharging containers
            for _ in range(CONTAINERS_PER_VESSEL):
                yield from self.move_container(vessel_name)
            
            print(f'{env.now}: {vessel_name} has departed.')

    def move_container(self, vessel_name):
        with self.cranes.request() as crane_req, self.trucks.request() as truck_req:
            yield crane_req & truck_req
            yield self.env.timeout(QUAY_CRANE_MOVE_TIME)
            print(f'{env.now}: A container has been moved from {vessel_name}.')

def vessel_generator(env, terminal):
    while True:
        yield env.timeout(random.expovariate(1 / MEAN_ARRIVAL_TIME))
        vessel_name = f'Vessel {env.now//60:.0f}:{env.now%60:02.0f}'
        print(f'{env.now}: {vessel_name} arrives.')
        env.process(terminal.discharge_vessel(vessel_name))

env = simpy.Environment()
terminal = ContainerTerminal(env)
env.process(vessel_generator(env, terminal))
env.run(until=SIMULATION_TIME)
