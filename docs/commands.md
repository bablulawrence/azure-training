### Gremlin Queries

```
g.addV('person').property('id', 'bablu').property('firstName', 'Bablu').property('lastName', 'Lawrence').property('pk', 'pk')
g.addV('person').property('id', 'ranjith').property('firstName', 'Ranjith').property('lastName', 'Mohan').property('pk', 'pk')
g.addV('city').property('id', 'bengaluru').property('state', 'Karnataka').property('country', 'India').property('pk', 'pk')
g.addV('city').property('id', 'chennai').property('state', 'Tamilnadu').property('country', 'India').property('pk', 'pk')
g.V('bablu').addE('knows').to(g.V('ranjith'))
g.V('bablu').addE('livesin').to(g.V('bengaluru'))
```
