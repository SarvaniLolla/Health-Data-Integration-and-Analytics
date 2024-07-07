from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import *

# Azure credentials
credential = DefaultAzureCredential()

# Initialize Data Factory client
client = DataFactoryManagementClient(credential, '<your_subscription_id>')

# Define the pipeline parameters and activities
parameters = {}
activities = []

# Define data sources (e.g., Blob storage, SQL Database)
source_data = AzureBlobSourceLinkedService(connection_string='DefaultEndpointsProtocol=https;AccountName=<storage_account_name>;AccountKey=<account_key>')
source = BlobSource(skip_header_line_count=1)

# Define data sink (Azure SQL Database)
sink_data = AzureSqlSinkLinkedService(server_name='<azure_sql_server_name>.database.windows.net',
                                       database_name='<database_name>',
                                       table_name='<table_name>',
                                       username='<username>',
                                       password='<password>')

sink = SqlSink(sink_writer=sink_data)

# Define copy activity
copy_activity = CopyActivity(name='CopyFromBlobToSql',
                             source=source,
                             sink=sink,
                             enable_staging=True)

activities.append(copy_activity)

# Define pipeline
pipeline = PipelineResource(activities=activities)

# Create or update pipeline
client.pipelines.create_or_update('<your_resource_group>', '<your_data_factory_name>', '<pipeline_name>', pipeline)

print("Pipeline created successfully.")
