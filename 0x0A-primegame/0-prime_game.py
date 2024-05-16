def isWinner(x, nums):
    """
    Determine the winner of each game round.

    Args:
    x (int): Number of rounds.
    nums (list): List of integers, where each integer n,
    represents the upper limit of the set for each round.

    Returns:
    str: The name of the player that won the most rounds,
    OR None if the result is a tie.
    """

    def sieve_of_eratosthenes(max_num):
        """
        Generate a list indicating prime status,
        for numbers from 0 to max_num.
        """
        is_prime = [True] * (max_num + 1)
        p = 2
        while (p * p <= max_num):
            if is_prime[p]:
                for i in range(p * p, max_num + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False # 0 and 1 are not prime nums
        return is_prime

    # Find the maximum value of n to use in the Sieve of Eratosthenes
    max_n = max(nums)

    # Get the prime status of each number up to max_n
    is_prime = sieve_of_eratosthenes(max_n)

    # To keep track of the number of rounds won by Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Function to count the number of prime moves possible
    def count_prime_moves(n):
        count = 0
        for num in range(2, n + 1):
            if is_prime[num]:
                count += 1
                # Mark multiples of this prime as non-prime
                for multiple in range(num * 2, n + 1, num):
                    is_prime[multiple] = False
        return count

    # Simulate each round
    for n in nums:
        # We need to recompute the prime array for each game
        is_prime = sieve_of_eratosthenes(n)

        prime_moves = count_prime_moves(n)

        # If prime_moves is even,Ben win because Maria can't make the last move
        # If prime_moves is odd, Maria wins because she makes the last move
        if prime_moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
