Github iCalendar issue feed
===========================

Obtain list of open Github issues for your projects as an
iCalendar feed of VTODO items.

[Official repository](https://github.com/dpocock/github-icalendar/)

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
    repositories:
    - repository: your-user-name/your-project
    - repository: your-user-name/another-project

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

