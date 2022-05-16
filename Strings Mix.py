class Solution:
    def calculate_occurrences(self, string: str) -> dict:
        dictionary = dict()
        main_string = "".join(
            [char for char in string if char.isalpha() and char.islower()]
        )
        for key in main_string:
            if key not in dictionary:
                dictionary[key] = 1
            else:
                dictionary[key] += 1
        return {k: v for k, v in sorted(dictionary.items(), key=lambda x: x[0])}

    def merged_unique_string(self, dict1: dict, dict2: dict) -> str:
        full_string: str = "".join([str(key) for key in dict1.keys()]) + "".join(
            [str(key) for key in dict2.keys()]
        )
        final_string = str()
        for char in full_string:
            if char not in final_string:
                final_string += char
        return final_string

    @classmethod
    def mix(self, s1: str, s2: str) -> None:
        occurrence_s1 = self.calculate_occurrences(self, s1)
        occurrence_s2 = self.calculate_occurrences(self, s2)
        result = str()
        unique_string = self.merged_unique_string(self, occurrence_s1, occurrence_s2)
        for char in unique_string:
            if char in occurrence_s1 and char in occurrence_s2:
                if occurrence_s1[char] > occurrence_s2[char]:
                    result += f"1:{char * occurrence_s1[char]}"
                elif occurrence_s1[char] < occurrence_s2[char]:
                    result += f"2:{char * occurrence_s2[char]}"
                else:
                    result += f"=:{char * occurrence_s1[char]}"
                result += "/"

        print('"' + result + '"')


Solution.mix("Are the kids at home? aaaaa fffff", "Yes they are here! aaaaa fffff")


# output
# "=:aaaaaa/2:eeeee/=:fffff/=:hh/2:rr/=:s/1:tt/"

# {'a': 6, 'd': 1, 'e': 3, 'f': 5, 'h': 2, 'i': 1, 'k': 1, 'm': 1, 'o': 1, 'r': 1, 's': 1, 't': 2}
# {'a': 6, 'e': 5, 'f': 5, 'h': 2, 'r': 2, 's': 1, 't': 1, 'y': 1}
