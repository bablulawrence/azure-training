# Azure Cosmos DB

## Introduction

- Fully managed NoSQL database for modern app development.
- Single-digit millisecond response times, and automatic and instant scalability, guarantee speed at any scale.
- Business continuity is assured with SLA-backed availability and enterprise-grade security.
- App development is faster and more productive thanks to turnkey multi region data distribution anywhere in the world, open source APIs and SDKs for popular languages

[Introduction](https://docs.microsoft.com/en-us/azure/cosmos-db/introduction)

## Cosmos DB APIs

- SQL API
- Table API
- Cassandra API
- MongoDB API
- Gremlin API

[CosmosDB APIs](https://docs.microsoft.com/en-us/azure/cosmos-db/choose-api)

## Cosmos DB Resource Model

- Azure Cosmos container is the fundamental unit of scalability.
- You can virtually have an unlimited provisioned throughput (RU/s) and storage on a container.
- Azure Cosmos DB transparently partitions your container using the logical partition key that you specify in order to elastically scale your provisioned throughput and storage

[Resource Model](https://docs.microsoft.com/en-us/azure/cosmos-db/account-databases-containers-items)

## Global Distribution

- Azure Cosmos DB is a globally distributed database system that allows you to read and write data from the local replicas of your database.  - Azure Cosmos DB transparently replicates the data to all the regions associated with your Cosmos account.
- Azure Cosmos DB is a globally distributed database service that's designed to provide low latency, elastic scalability of throughput, well-defined semantics for data consistency, and high availability.

[Global Distribution](https://docs.microsoft.com/en-us/azure/cosmos-db/distribute-data-globally)

## Consistency Levels

- Strong - A client never sees an uncommitted or partial write
- Bounded staleness - The reads might lag behind writes by at most "K" versions (that is, "updates") of an item or by "T" time interval, whichever is reached first
- Session - In session consistency, within a single client session reads are guaranteed to honor the consistent-prefix, monotonic reads, monotonic writes, read-your-writes, and write-follows-reads guarantees
- Consistent prefix - Consistent prefix consistency level guarantees that reads never see out-of-order writes
- Eventual - In eventual consistency, there's no ordering guarantee for reads. In the absence of any further writes, the replicas eventually converge

[Consistency Levels](https://docs.microsoft.com/en-us/azure/cosmos-db/consistency-levels)
