#example1
import pandas as pd

datacamp = pd.DataFrame({
    'course': ['python', 'r', 'sql'],
    'level': ['advanced', 'intermediate', 'beginner'],
    'chapter': [1, 2, 3]
})

is_less = datacamp["chapter"] < 3
output = datacamp[is_less]

print(output)
