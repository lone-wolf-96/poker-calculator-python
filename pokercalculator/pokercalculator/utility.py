from final_class import final


@final
class Utility:

    @staticmethod
    def replace_ace_for_one_if(rank_numbers):
        has_ace_and_two = all(rank_n in rank_numbers for rank_n in [2, 14])

        if (has_ace_and_two):
            rank_numbers = sorted(
                [1 if rank_n == 14 else rank_n for rank_n in rank_numbers])

        return rank_numbers

    @staticmethod
    def get_frequency_tuple(rank_numbers):
        mode = max(rank_numbers, key=rank_numbers.count)
        return (mode, rank_numbers.count(mode))
