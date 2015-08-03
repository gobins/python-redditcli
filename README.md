# Python CLI for Reddit API


## Description
-----------------------------
The Python-RedditCli is a Command Line Interface which can be used to call the Reddit REST API.

## Setup
-----------------------------
1. pip install python-redditcli
2. Create an app which will be used to call the API.
3. Supply the CLI parameters and you are ready to go.

## Examples
-----------------------------

redditcli --client-id <client0id> --client-secret <client-secret> --username <username> --password <password> my-account
+--------------------+--------------+
| Field              | Value        |
+--------------------+--------------+
| has_mail           | False        |
| name               | testuser    |
| created            | 1333290013.0 |
| hide_from_robots   | False        |
| gold_creddits      | 0            |
| created_utc        | 1333286413.0 |
| link_karma         | 11           |
| comment_karma      | 817          |
| over_18            | True         |
| is_gold            | False        |
| is_mod             | False        |
| gold_expiration    | None         |
| inbox_count        | 0            |
| has_verified_email | False        |
| id                 | 7brma        |
| has_mod_mail       | False        |
+--------------------+--------------+

redditcli --client-id <client0id> --client-secret <client-secret> --username <username> --password <password> my-prefs

+--------------------+--------------+
| Field              | Value        |
+--------------------+--------------+
| has_mail           | False        |
| name               | redrhymer    |
| created            | 1333290013.0 |
| hide_from_robots   | False        |
| gold_creddits      | 0            |
| created_utc        | 1333286413.0 |
| link_karma         | 11           |
| comment_karma      | 817          |
| over_18            | True         |
| is_gold            | False        |
| is_mod             | False        |
| gold_expiration    | None         |
| inbox_count        | 0            |
| has_verified_email | False        |
| id                 | 7brma        |
| has_mod_mail       | False        |
+--------------------+--------------+


## Contributing
-----------------------------
The CLI does not handle all API calls. Feel free to contribute by sending a pull request.
The CLI may also break when there is an update in the API, please raise an issue if you find any problems or needs improvements.