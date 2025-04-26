# Indonesian Slangwords Dictionary

Kamus slangwords bahasa Indonesia dalam format CSV yang mudah diakses dan dikembangkan bersama.

## 📁 Struktur Data

File `indonesian-slangwords.csv` berisi:

```csv
Slang,Meaning
abis,habis
wtb,beli
masi,masih
```


## Python Usage
```python
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/refanz/indonesian-slangwords/master/data/indonesian-slangwords.csv")
print(df[df['Slang'] == 'LOL']['Meaning'].values[0])
```

## Direct CSV Access
https://raw.githubusercontent.com/refanz/indonesian-slangwords/master/data/indonesian-slangwords.csv