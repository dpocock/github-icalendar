#!/usr/bin/env python

"""
.. module:: main
   :synopsis: Render Github issues as iCalendar feed
.. moduleauthor:: Daniel Pocock http://danielpocock.com

"""

# Copyright (C) 2015, Daniel Pocock http://danielpocock.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import flask
import github
import yaml
import icalendar
import logging
import os

log = logging.getLogger(__name__)
def setup_logging():
    log.setLevel(logging.DEBUG)
    console_out = logging.StreamHandler()
    console_out.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    console_out.setFormatter(formatter)
    log.addHandler(console_out)

def display(cal):
    return cal.to_ical().replace('\r\n', '\n').strip()

def make_uid(issue):
    return "%s-%s.issue.github.com" % (issue.number, issue.id)

def make_title(repo_title, issue):
    return "%s #%s: %s" % (repo_title, issue.number, issue.title)

def make_reporter(issue):
    return "%s@users.github.com" % issue.user.login

def fetch_issues_by_repo(github_client, repo_name):

    repo_name_parts = repo_name.split('/')
    repo_title = repo_name_parts[1]
    repo = github_client.get_repo(repo_name)

    items = []
    for issue in repo.get_issues(state='open'):
        try:
            todo = icalendar.Todo()
            todo['uid'] = make_uid(issue)
            todo['summary'] = make_title(repo_title, issue)
            todo['description'] = issue.body
            todo['url'] = issue.html_url
            todo['created'] = issue.created_at
            todo['last-modified'] = issue.updated_at
            todo['status'] = 'NEEDS-ACTION'
            todo['organizer'] = make_reporter(issue)
            items.append(todo)

        except Exception:
            log.error("Failed to parse %r", t, exc_info=True)
            return None
    return items

app = flask.Flask(__name__)
conf = None

@app.route("/")
def ics_feed():
    if conf is None:
        log.error("No configuration available")
        return flask.Response(status_code=500, status='Missing configuration')

    github_client = github.Github(
            conf['api_token'],
            user_agent='Github-iCalendar')
    cal = icalendar.Calendar()
    cal.add('prodid', '-//danielpocock.com//GithubIssueFeed//')
    cal.add('version', '1.0')
    for repo_details in conf['repositories']:
        repo_name = repo_details['repository']
        log.debug("trying repository: %s" % (repo_name))
        items = fetch_issues_by_repo(github_client, repo_name)
        if items is None:
            log.error("Error parsing Github data for %s" % repo_name)
            return flask.Response(status_code=500,
                status='Error parsing Github data')
        for item in items:
            cal.add_component(item)
    log.debug("done, writing response to stream")
    return flask.Response("%s" % display(cal),
        mimetype='text/calendar')

if __name__ == '__main__':
    setup_logging()
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('config_filename')
    args = arg_parser.parse_args()
    with open(args.config_filename) as f:
        conf = yaml.load(f)
        log.info("Config loaded")
    app.run(host=conf['bind_address'], port=conf['bind_port'])
    #app.run(host=conf['bind_address'], port=conf['bind_port'], debug=True)

