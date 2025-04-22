from collections import deque
import random

def hot_potato(players, max_passes):
    queue = deque(players)

    while len(queue) > 1:
        # Generate a random number of passes
        passes = random.randint(1, max_passes)
        print(f"\n {passes} passes this round")

        # Simulate passing the "hot potato"
        for _ in range(passes):
            player = queue.popleft()
            queue.append(player)
            print(f" {player} passes the potato")

        # Remove the player holding the "hot potato"
        eliminated = queue.popleft()
        print(f" {eliminated} has been eliminated")

    # The last player remaining is the winner
    winner = queue[0]
    print(f"\n The winner is: {winner}!")
    return winner

# Test the game
if __name__ == "__main__":
    players = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
    max_passes = 6
    hot_potato(players, max_passes)
