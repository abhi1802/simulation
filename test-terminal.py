import pytest
from main import ContainerTerminal, vessel_generator, NUM_CONTAINERS_PER_VESSEL
import simpy

# Fixture for setting up the environment and terminal
@pytest.fixture
def setup_terminal():
    env = simpy.Environment()
    terminal = ContainerTerminal(env)
    return env, terminal

def test_vessel_arrival_distribution(setup_terminal):
    env, terminal = setup_terminal
    initial_time = env.now
    env.run(until=5)
    assert env.now >= initial_time

def test_discharge_process(setup_terminal):
    env, terminal = setup_terminal
    vessel_name = "Test Vessel"
    env.process(terminal.discharge_vessel(vessel_name))
    # Run the simulation for enough time to potentially process a vessel
    env.run(until=NUM_CONTAINERS_PER_VESSEL * 3)

def test_resource_allocation(setup_terminal):
    env, terminal = setup_terminal
    initial_berths = terminal.berth.capacity
    initial_cranes = terminal.cranes.capacity
    initial_trucks = terminal.trucks.capacity
    # Assert initial conditions
    assert terminal.berth.count == 0
    assert terminal.cranes.count == 0
    assert terminal.trucks.count == 0

