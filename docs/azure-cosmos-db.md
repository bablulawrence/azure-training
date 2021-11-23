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

[Getting Started with Table API](https://willvelida.medium.com/getting-started-with-the-table-api-in-azure-cosmos-db-1509fd52e46b)
