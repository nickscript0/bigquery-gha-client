#!/usr/bin/env python
""" Command line client for querying BigQuery """

from apiclient.discovery import build
from apiclient.errors import HttpError

from oauth2client.client import GoogleCredentials

QUERY1 = """
SELECT repository_url, COUNT(*) as star_count,
  STRFTIME_UTC_USEC(created_at, '%m') as month,
  STRFTIME_UTC_USEC(created_at, '%Y') as year
  FROM (
  TABLE_QUERY([githubarchive:month],
    'REGEXP_MATCH(table_id, r"^201[1-4][01]\d")'

  ))
WHERE type = 'WatchEvent' AND
  repository_url in ('https://github.com/angular/angular.js', 'https://github.com/emberjs/ember.js', 'https://github.com/lhorie/mithril.js', 'https://github.com/facebook/react', 'https://github.com/aurelia/framework', 'https://github.com/jashkenas/backbone', 'https://github.com/kmalakoff/knockback', 'https://github.com/meteor/meteor', 'https://github.com/ampersandjs/ampersand', 'https://github.com/leaddyno/intercooler-js', 'https://github.com/bluespire/durandal', 'https://github.com/deftsjs/deftjs', 'https://github.com/rappid/rappid.js', 'https://github.com/angular/angular.dart', 'https://github.com/componentjs/component', 'https://github.com/chaplinjs/chaplin', 'https://github.com/flams/olives', 'https://github.com/elabs/serenade.js', 'https://github.com/marionettejs/backbone.marionette', 'https://github.com/rhysbrettbowen/plastronjs', 'https://github.com/knockout/knockout', 'https://github.com/atmajs/maskjs', 'https://github.com/mutualmobile/lavaca', 'https://github.com/epitome-mvc/epitome', 'https://github.com/enyojs/enyo', 'https://github.com/quirkey/sammy', 'https://github.com/ariatemplates/ariatemplates', 'https://github.com/jquery/jquery', 'https://github.com/meteor/meteor', 'https://github.com/jashkenas/backbone', 'https://github.com/facebook/react', 'https://github.com/polymer/polymer', 'https://github.com/flightjs/flight', 'https://github.com/derbyjs/derby', 'https://github.com/ractivejs/ractive', 'https://github.com/socketstream/socketstream', 'https://github.com/yyx990803/vue', 'https://github.com/spine/spine', 'https://github.com/yui/yui3', 'https://github.com/lhorie/mithril.js', 'https://github.com/batmanjs/batman', 'https://github.com/elm-lang/elm-compiler', 'https://github.com/walmartlabs/thorax', 'https://github.com/montagejs/montage', 'https://github.com/telerik/kendo-ui-core', 'https://github.com/bitovi/canjs', 'https://github.com/kmalakoff/knockback', 'https://github.com/google/closure-compiler', 'https://github.com/paulmillr/exoskeleton', 'https://github.com/ampersandjs/ampersand', 'https://github.com/gwtproject/gwt', 'https://github.com/dojo/dojo', 'https://github.com/hay/stapes', 'https://github.com/somajs/somajs', 'https://github.com/firebase/angularfire', 'https://github.com/mozart/mozart2', 'https://github.com/pathikrit/dijon')
GROUP BY repository_url, month, year
ORDER BY year, month, star_count DESC;
"""

QUERY_ORIG = """
SELECT TOP(corpus, 10) as title,
          COUNT(*) as unique_words
          FROM [publicdata:samples.shakespeare];
"""


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
            'query': (QUERY1)
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
