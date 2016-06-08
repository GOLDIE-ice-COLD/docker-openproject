[![Stories in Ready](https://badge.waffle.io/progtologist/docker-openproject.png?label=ready&title=Ready)](https://waffle.io/progtologist/docker-openproject)
# OpenProject Dockerfile

A Dockerfile that builds [OpenProject][openproject], a free and open source
software for project management with a wide set of features and plugins and an
active community.

Comes with Vagrantfile for local testing; just use `vagrant up --no-parallel`.

## Basic usage

This is currently relying on a linked database container.  Here's an example
usage (including data-only container):

```
docker run -d --name openproject-postgres-data -v /data busybox true
docker run -d --name openproject-postgres --volumes-from openproject-postgres-data -e USER=super -e PASS=password paintedfox/postgresql
docker run -d --name openproject --link openproject-postgres:postgres -p 8080:80 -e SMTP_USERNAME=test@gmail.com -e SMTP_PASSWORD=password -e SMTP_HOST=your.smtp.server -h name.of.your.openproject.host azazel/openproject
```

Wait a little while for the database setup and migrations to run.  After a
short period the application should be available at http://localhost:8080.
You can check the database migration progress with `docker
attach--sig-proxy=false openproject`.

You can use the SMTP\_USERNAME and SMTP\_PASSWORD and SMTP\_HOST parameters to
enable using smtp to send emails. This will also fetch incoming mail from the
same host on an imap server on port 143.

## License

MIT license.

[openproject]: https://www.openproject.org/
