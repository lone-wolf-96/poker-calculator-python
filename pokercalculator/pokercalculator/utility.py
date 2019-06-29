class Utility:

    @staticmethod
    def replace_ace_for_one_if(rank_numbers):
        has_ace_and_two = all(rank_n in rank_numbers for rank_n in [2, 14])

        if (has_ace_and_two):
            rank_numbers = [1 if rank_n ==
                            14 else rank_n for rank_n in rank_numbers]
            rank_numbers.sort()

        return rank_numbers
