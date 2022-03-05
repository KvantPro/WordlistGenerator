# WordlistGenerator
Python so slow...
# Usage
```Python
from WG import WordlistGenerator

passwd = WordlistGenerator(2) # Two args: (leght, words) words not necessary
for i in range(passwd.len_password):
    print(passwd.next())
```
