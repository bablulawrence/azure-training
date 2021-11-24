import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://cosmosdb-sql-779.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'pVJQhrTJv0SQeQNWNhP2IoxbztPIPXAYVM2N4tCMbzzJFx1fzjv6gGbO24FulV2QVMZrd0y4aMZSgq2bop832A=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}