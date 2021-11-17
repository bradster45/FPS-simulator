from initialize.generation import initialise_match


def run():
    match = initialise_match()
    match.simulate_gunfights(400)
    match.show_leaderboard()
    pass


run()
