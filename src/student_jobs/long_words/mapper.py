import string
from src.core.job.mapper import Mapper

class LongWordsMapper(Mapper):
    def map(self, record, emit):
        cleaned = record.translate(str.maketrans("", "", string.punctuation))
        for word in cleaned.lower().split():
            if len(word) > 5:
                emit(word, 1)