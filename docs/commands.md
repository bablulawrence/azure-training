### Gremlin Queries

```
g.addV('person').property('id', 'bablu').property('firstName', 'Bablu').property('lastName', 'Lawrence').property('pk', 'pk')
g.addV('person').property('id', 'ranjith').property('firstName', 'Ranjith').property('lastName', 'Mohan').property('pk', 'pk')
g.addV('city').property('id', 'bengaluru').property('state', 'Karnataka').property('country', 'India').property('pk', 'pk')
g.addV('city').property('id', 'chennai').property('state', 'Tamilnadu').property('country', 'India').property('pk', 'pk')
g.V('bablu').addE('knows').to(g.V('ranjith'))
g.V('bablu').addE('livesin').to(g.V('bengaluru'))
```

### Azure Resource Manager

az deployment group create --resource-group rg-training --template-file template.json --parameters '@parameters.json'

az storage account create -n storage776 -g rg-training -l southeastasia --sku Standard_LRS

New-AzStorageAccount -ResourceGroupName rg-training -Name storage775 -Location southeastasia -SkuName Standard_RAGRS -Kind StorageV2
