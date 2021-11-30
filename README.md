# Azure Cosmos DB

## Overview

### Introduction

- Fully managed NoSQL database for modern app development.
- Single-digit millisecond response times, and automatic and instant scalability, guarantee speed at any scale.
- Business continuity is assured with SLA-backed availability and enterprise-grade security.
- App development is faster and more productive thanks to turnkey multi region data distribution anywhere in the world, open source APIs and SDKs for popular languages

[Introduction](https://docs.microsoft.com/en-us/azure/cosmos-db/introduction)

### Cosmos DB APIs

- SQL API
- Table API
- Cassandra API
- MongoDB API
- Gremlin API

[CosmosDB APIs](https://docs.microsoft.com/en-us/azure/cosmos-db/choose-api)

### Cosmos DB Resource Model

- Azure Cosmos container is the fundamental unit of scalability.
- You can virtually have an unlimited provisioned throughput (RU/s) and storage on a container.
- Azure Cosmos DB transparently partitions your container using the logical partition key that you specify in order to elastically scale your provisioned throughput and storage

[Resource Model](https://docs.microsoft.com/en-us/azure/cosmos-db/account-databases-containers-items)

### Global Distribution

- Azure Cosmos DB is a globally distributed database system that allows you to read and write data from the local replicas of your database. - Azure Cosmos DB transparently replicates the data to all the regions associated with your Cosmos account.
- Azure Cosmos DB is a globally distributed database service that's designed to provide low latency, elastic scalability of throughput, well-defined semantics for data consistency, and high availability.

[Global Distribution](https://docs.microsoft.com/en-us/azure/cosmos-db/distribute-data-globally)

### Consistency Levels

- Strong - A client never sees an uncommitted or partial write
- Bounded staleness - The reads might lag behind writes by at most "K" versions (that is, "updates") of an item or by "T" time interval, whichever is reached first
- Session - In session consistency, within a single client session reads are guaranteed to honor the consistent-prefix, monotonic reads, monotonic writes, read-your-writes, and write-follows-reads guarantees
- Consistent prefix - Consistent prefix consistency level guarantees that reads never see out-of-order writes
- Eventual - In eventual consistency, there's no ordering guarantee for reads. In the absence of any further writes, the replicas eventually converge

[Consistency Levels](https://docs.microsoft.com/en-us/azure/cosmos-db/consistency-levels)

## Cosmos DB API Detail

Following are some of ways you can add data to Cosmos DB.

- You add data to Cosmos DB programmatically using one the SDKs provided - .NET, Java, Node.js and Python.

- Add data using tools like Cosmos DB Data Explorer, Azure Storage Explorer.

- Use Azure Data Factory, Azure Databricks etc.

### SQL API

There are basically two ways to read data using SQL API.

- **Point reads** - You can do a key/value lookup on a single item ID and partition key. The item ID and partition key combination is the key and the item itself is the value. For a 1 KB document, point reads typically cost 1 request unit with a latency under 10 ms. _Point reads return a single item_.

- **SQL queries** - You can query data by writing queries using SQL. Queries always cost at least 2.3 request units and, in general, will have a higher and more variable latency than point reads. _Queries can return many items_

[Querying with SQL](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-getting-started)

[Data Explorer](https://docs.microsoft.com/en-us/azure/cosmos-db/data-explorer)

[Copy using ADF](https://docs.microsoft.com/en-us/azure/data-factory/connector-azure-cosmos-db?tabs=data-factory)

### Table API

- Azure Cosmos DB provides the Table API for applications that are written for Azure Table storage and that need premium capabilities like:
  - Turnkey global distribution.
  - Dedicated throughput worldwide (when using provisioned throughput).
  - Single-digit millisecond latencies at the 99th percentile.
  - Guaranteed high availability.
  - Automatic secondary indexing.
  - Azure Tables SDKs are available for .NET, Java, Python, Node.js, and Go. These SDKs can be used to target either Table Storage or Cosmos DB Tables.
  - _Applications written for Azure Table storage using the Azure Tables SDKs can be migrated to the Azure Cosmos DB Table API with no code changes to take advantage of premium capabilities_.

[Table API Introduction](https://docs.microsoft.com/en-us/azure/cosmos-db/table/introduction)

[Getting started with Table API](https://willvelida.medium.com/getting-started-with-the-table-api-in-azure-cosmos-db-1509fd52e46b)

[Getting started with Python](https://docs.microsoft.com/en-gb/azure/cosmos-db/table/how-to-use-python)

### Gremlin API

- Azure Cosmos DB provides a graph database service via the Gremlin API on a fully managed database service designed for any scale.
- You can query the graphs with millisecond latency and evolve the graph structure easily
- Azure Cosmos DB's Gremlin API is built based on the [Apache TinkerPop](https://tinkerpop.apache.org), a graph computing framework.
- The Gremlin API in Azure Cosmos DB uses the Gremlin query language.

#### Scenarios where Gremlin API can be useful

- Social networks/Customer 365
- Recommendation engines
- Geospatial
- Internet of Things

[Introduction to Gremlin API](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction)

[Build .Net Application Using Gremlin API](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/create-graph-dotnet)

[Create Graph using Python](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/create-graph-python)

### MongoDB API

- The Azure Cosmos DB API for MongoDB makes it easy to use Cosmos DB as if it were a MongoDB database.
- You can leverage your MongoDB experience and continue to use your favorite MongoDB drivers, SDKs, and tools by pointing your application to the API for MongoDB account's connection string

[Introduction to MongoDB API](https://docs.microsoft.com/en-us/azure/cosmos-db/mongodb/mongodb-introduction)

[Migrate existing MongoDB Node.Js App](https://docs.microsoft.com/en-us/azure/cosmos-db/mongodb/create-mongodb-nodejs)

[MongoDB Shell](https://docs.mongodb.com/manual/reference/mongo-shell/)

# Azure Data Explorer

- Azure Data Explorer is a fully managed, high-performance, big data analytics platform that makes it easy to analyze high volumes of data in near real time.

- The Azure Data Explorer toolbox gives you an end-to-end solution for data ingestion, query, visualization, and management.

- By analyzing structured, semi-structured, and unstructured data across time series, and by using Machine Learning, Azure Data Explorer makes it simple to extract key insights, spot patterns and trends, and create forecasting models.

[Azure Data Explorer Overview](https://docs.microsoft.com/en-us/azure/data-explorer/data-explorer-overview)

[Cosmos DB and Data Explorer Integration](https://github.com/Azure/azure-kusto-labs/tree/master/cosmosdb-adx-integration)

# Azure Synapse Analytics

- Azure Synapse is an enterprise analytics service that accelerates time to insight across data warehouses and big data systems.

- Azure Synapse brings together the best of SQL technologies used in enterprise data warehousing, Spark technologies used for big data, Data Explorer for log and time series analytics, Pipelines for data integration and ETL/ELT, and deep integration with other Azure services such as Power BI, CosmosDB, and AzureML

- Synapse Studio provides a single way for enterprises to build solutions, maintain, and secure all in a single user experience
  - Perform key tasks: ingest, explore, prepare, orchestrate, visualize
  - Monitor resources, usage, and users across SQL, Spark, and Data Explorer
  - Use Role-based access control to simplify access to analytics resources
  - Write SQL, Spark or KQL code and integrate with enterprise CI/CD processes

![Overview](https://github.com/bablulawrence/azure-training/blob/main/docs/azure-synapse.jpg)

[Azure Synapse Analytics Overview](https://docs.microsoft.com/en-in/azure/synapse-analytics/overview-what-is)

[Azure Synapse Analytics: A Data Lakehouse](https://www.youtube.com/watch?v=mbHFKS8yf48)

# Azure Databricks

- Azure Databricks is a data analytics platform optimized for the Microsoft Azure cloud services platform.

- Azure Databricks offers three environments for developing data intensive applications: Databricks SQL, Databricks Data Science & Engineering, and Databricks Machine Learning.

- Databricks SQL provides an easy-to-use platform for analysts who want to run SQL queries on their data lake, create multiple visualization types to explore query results from different perspectives, and build and share dashboards

- Databricks Data Science & Engineering provides an interactive workspace that enables collaboration between data engineers, data scientists, and machine learning engineers

- Databricks Machine Learning is an integrated end-to-end machine learning environment incorporating managed services for experiment tracking, model training, feature development and management, and feature and model serving

![Overview](https://github.com/bablulawrence/azure-training/blob/main/docs/azure-databricks.png)

[Azure Databricks Overview](https://docs.microsoft.com/en-in/azure/databricks/scenarios/what-is-azure-databricks)

[Azure Databricks Product Info](https://databricks.com/product/azure)

[Mounting ADLS Gen2](https://docs.databricks.com/data/data-sources/azure/adls-gen2/azure-datalake-gen2-sp-access.html)

[NYC Taxi Data](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

# Creating and managing Azure Resources

- Azure Resource Manager is the deployment and management service for Azure.

- It provides a management layer that enables you to create, update, and delete resources in your Azure account. You use management features, like access control, locks, and tags, to secure and organize your resources after deployment.

- When a user sends a request from any of the Azure tools, APIs, or SDKs, Resource Manager receives the request. It authenticates and authorizes the request. Resource Manager sends the request to the Azure service, which takes the requested action.

- Because all requests are handled through the same API, you see consistent results and capabilities in all the different tools

[Azure Resource Manager Overview](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview)

[Azure Portal](https://azure.microsoft.com/en-in/features/azure-portal/)

[Azure CLI](https://docs.microsoft.com/en-us/cli/azure/what-is-azure-cli)

[Azure Resource Manager PowerShell](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resources-powershell)

[Using Azure Resource Manager Python SDK](https://docs.microsoft.com/en-us/samples/azure-samples/resource-manager-python-resources-and-groups/manage-azure-resources-and-resource-groups-with-python/)

[Azure Resource Manager REST API](https://docs.microsoft.com/en-us/rest/api/resources/)
