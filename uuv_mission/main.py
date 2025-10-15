from dynamic import Submarine, ClosedLoop, Mission
from control import Controller

sub = Submarine()
controller = Controller()
closed_loop = ClosedLoop(sub, controller)

mission = Mission.from_csv("../data/mission.csv")

trajectory = closed_loop.simulate_with_random_disturbances(mission)
trajectory.plot_completed_mission(mission)
