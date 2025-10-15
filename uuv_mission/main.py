from dynamic import *
from control import Controller

sub = Submarine()
print(sub.get_position())
controller = Controller()
closed_loop = ClosedLoop(sub, controller)
mission = Mission.from_csv("../data/mission.csv")
print(mission) 
#trajectory = closed_loop.simulate_with_random_disturbances(mission)
#trajectory.plot_completed_mission(mission)
