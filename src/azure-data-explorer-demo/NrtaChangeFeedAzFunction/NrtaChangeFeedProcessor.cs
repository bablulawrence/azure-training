using System;
using System.Collections.Generic;
using System.Configuration;
using System.Text;
using Microsoft.Azure.Documents;
using Microsoft.Azure.EventHubs;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Build.Utilities;
using Microsoft.Extensions.Logging;
using Microsoft.WindowsAzure.Storage.Blob.Protocol;
using Newtonsoft.Json;

namespace NrtaChangeFeedAzFunction
{
    public static class NrtaChangeFeedProcessor
    {
        [FunctionName("NrtaChangeFeedProcessor")]
        public static void Run([CosmosDBTrigger(
            databaseName: "sample-db",
            collectionName: "container1",
            ConnectionStringSetting = "CosmosDBChangeFeedConnection",
            LeaseCollectionName = "leases", 
            CreateLeaseCollectionIfNotExists = true)]IReadOnlyList<Document> input, ILogger log)
        {
            try
            {
                if (input != null && input.Count > 0)
                {
                    string eventHubName = Environment.GetEnvironmentVariable("EventHubName");
                    string eventHubNamespaceConnection = Environment.GetEnvironmentVariable("EventHubConnection");

                    // Build connection string to access event hub within event hub namespace.
                    EventHubsConnectionStringBuilder eventHubConnectionStringBuilder =
                        new EventHubsConnectionStringBuilder(eventHubNamespaceConnection)
                        {
                            EntityPath = eventHubName
                        };

                    // Create event hub client to send change feed events to event hub.
                    EventHubClient eventHubClient = EventHubClient.CreateFromConnectionString(eventHubConnectionStringBuilder.ToString());

                    // Iterate through modified documents from change feed.
                    foreach (var doc in input)
                    {
                        // Convert documents to json.
                        string json = JsonConvert.SerializeObject(doc);
                        EventData data = new EventData(Encoding.UTF8.GetBytes(json));

                        // Use Event Hub client to send the change events to event hub.
                        eventHubClient.SendAsync(data);
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
