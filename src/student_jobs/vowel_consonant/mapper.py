import string
from src.core.job.mapper import Mapper

VOWELS = set("aeiouyаеєиіїоуюя")

class VowelConsMapper(Mapper):
    def map(self, record, emit):
        cleaned = record.translate(str.maketrans("", "", string.punctuation))

        for word in cleaned.lower().split():
            if len(word) == 0:
                continue

            vowel_count = sum(1 for ch in word if ch in VOWELS)
            cons_count  = sum(1 for ch in word if ch.isalpha() and ch not in VOWELS)

            emit(
                str(len(word)),
                {"vowels": vowel_count, "cons": cons_count, "count": 1}
            )