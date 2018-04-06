# mini-amazon
for the folks at RNSIT

```bash
git clone https://github.com/sunil3590/mini-amazon.git
cd mini-amazon
pip install -r requirements.txt
python run.py
```

### If you face 'port already in use' error
```bash
netstat -tulnp | grep 5000
kill -9 <process_id>
```

### To get the list of products currently saved
```python
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mini_amazon
prods = db.products_collection.find()
for prod in prods:
    print(prod)
```