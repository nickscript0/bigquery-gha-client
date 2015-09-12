# bigquery-gha-client
Python client for working with the Bigquery GitHub Archive

## Usage
```
docker-compose run main /bin/bash
python3 main.py
```

## Notes
### What's free
* "You aren't charged for queries that return an error, or for cached queries."
* From https://cloud.google.com/bigquery/pricing#free

### How to ensure cached queries
* If you use the jobs.insert() function to run a query, you can ensure that the job returns a query result from the cache, if it exists, by setting the createDisposition property of the job configuration to CREATE_NEVER.
 * If the query result doesn't exist in the cache, a NOT_FOUND error returns.
* If using the BigQuery API, the cacheHit property in the query result is set to true.
* From https://cloud.google.com/bigquery/querying-data#querycaching

### Practical examples of cached query checking
#### Jobs: query (synchronous)
https://cloud.google.com/bigquery/docs/reference/v2/jobs/query
```

POST https://www.googleapis.com/bigquery/v2/projects/projectId/queries

Ensure "cacheHit": boolean is True in the response
```

#### Jobs: insert (asynchronous)
https://cloud.google.com/bigquery/docs/reference/v2/jobs/insert
https://cloud.google.com/bigquery/docs/reference/v2/jobs#resource
```

Set the following in the job configuration to CREATE_NEVER:
configuration.query.createDisposition
configuration.load.createDisposition
```

### How to create a service key to use Application Default credentials
https://cloud.google.com/docs/authentication#preparation
