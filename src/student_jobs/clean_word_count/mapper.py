import string
from src.core.job.mapper import Mapper

class CleanWordCountMapper(Mapper):
    def map(self, record, emit):
        cleaned = record.translate(str.maketrans("", "", string.punctuation))
        for word in cleaned.lower().split():
            if word.strip():
                emit(word, 1)