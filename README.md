# bigquery-gha-client
Python client for working with the Bigquery GitHub Archive

## Usage
```
docker-compose run main /bin/bash
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
