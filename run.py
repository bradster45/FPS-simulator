from db.models import MatchSimulationThread
from initialize.generation import initialise_match


# initial match setup
match = initialise_match()
match.simulate_match()

match.map.display_board()

thread = MatchSimulationThread(match)
thread.running_speed = 2.0
thread.start()
