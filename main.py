#!/usr/bin/env python
""" Command line client for querying BigQuery """

from apiclient.discovery import build
from apiclient.errors import HttpError

from oauth2client.client import GoogleCredentials


def main(project_id):
    # [START build_service]
    # Grab the application's default credentials from the environment.
    credentials = GoogleCredentials.get_application_default()
    # Construct the service object for interacting with the BigQuery API.
    bigquery_service = build('bigquery', 'v2', credentials=credentials)
    # [END build_service]

    try:
        # [START run_query]
        query_request = bigquery_service.jobs()
        query_data = {
            'query': ('SELECT TOP(corpus, 10) as title, '
                      'COUNT(*) as unique_words '
                      'FROM [publicdata:samples.shakespeare];')
        }

        query_response = query_request.query(
            projectId=project_id,
            body=query_data).execute()
        # [END run_query]

        # [START print_results]
        print('Query Results:')
        for row in query_response['rows']:
            print('\t'.join(field['v'] for field in row['f']))
        # [END print_results]
        print ('cacheHit: {0}'.format(query_response['cacheHit']))
    except HttpError as err:
        print('Error: {}'.format(err.content))
        raise err


if __name__ == '__main__':
    # The id of the project to run queries under.
    #project_id = input("Enter the project ID: ")
    project_id = open('/credentials/project_id').read().strip()
    main(project_id)
