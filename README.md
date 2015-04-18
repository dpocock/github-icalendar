Github iCalendar issue feed
===========================

Obtain list of open Github issues for your projects as an
iCalendar feed of VTODO items.

[Official repository](https://github.com/dpocock/github-icalendar/)

Github iCalendar is written in Python and uses the
[Flask](http://flask.pocoo.org/) micro web application framework. 
If you'd prefer a PHP based solution, a clone of this script written in 
PHP is available [here](https://github.com/gpolitis/php-github-icalendar/).

Would you like to see native iCalendar support in Github?
---------------------------------------------------------

Although it is not hard to download this script and run it yourself,
you may prefer to connect directly to https://api.github.com with
your favourite iCalendar client.

[Contact Github support](mailto:support@github.com?subject=Github+iCalendar)
and click the Star button on the page for this project to register your
vote for native iCalendar support in the Github API.

Usage
-----

Install the dependencies on your system, on a Debian or Ubuntu system you
may execute a command like this to get everything you need:

    sudo apt-get install python-yaml python-icalendar python-flask python-pygithub

Create an API token on GitHub [using these instructions](https://help.github.com/articles/creating-an-access-token-for-command-line-use/)

Create a configuration file, for example:

    api_token: 6b36b3d7579d06c9f8e88bc6fb33864e4765e5fac4a3c2fd1bc33aad
    bind_address: ::0
    bind_port: 5000
    filter: all

By default, you will see todo items for open issues in all repositories
that you have access to.  If you want to limit the list to specific
repositories, list them in the configuration file and any others will
be ignored:

    api_token: 6b36b3d7579d06c9f8e88bc6fb33864e4765e5fac4a3c2fd1bc33aad
    bind_address: ::0
    bind_port: 5000
    filter: all
    repositories:
    - repository: your-user-name/your-project
    - repository: your-user-name/another-project

The `filter` parameter has the same meaning as the `filter` parameter
in the [Github issues API](https://developer.github.com/v3/issues/)
although if it is not specified, Github-iCalendar uses `all` as the
default.

Start the process:

    $ ./github_icalendar/main.py github-ics.cfg

In your iCalendar client (such as Mozilla Thunderbird with the
Mozilla Lightning plugin) you just have to add a new remote calendar
using the http://host:port URL where your github-icalendar instance
is running.

Copyright notice
----------------

Copyright (C) 2015, Daniel Pocock http://danielpocock.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

