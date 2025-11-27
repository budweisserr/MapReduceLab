from src.core.job.reducer import Reducer

class VowelConsReducer(Reducer):
    def reduce(self, key, values, emit):
        total_v = 0
        total_c = 0
        count = 0

        for v in values:
            total_v += v["vowels"]
            total_c += v["cons"]
            count   += v["count"]

        if total_v + total_c == 0:
            return

        vowels_pct = round((total_v / (total_v + total_c)) * 100, 2)
        cons_pct   = round((total_c / (total_v + total_c)) * 100, 2)

        emit(key, {"Відсоток голосних": vowels_pct, "Відсоток приголосних": cons_pct})