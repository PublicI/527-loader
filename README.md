# 527 Loader

Loads [IRS 527 data](https://forms.irs.gov/app/pod/dataDownload/dataDownload) into a Postgres database.

To run:
```bash
chmod +x load.sh
export PGHOST=<database host> PGDATABASE=<database name> PGUSER=<database user> PGPASSWORD=<database password>
./load.sh
```

Or you can establish a [pgpass file](https://www.postgresql.org/docs/9.4/libpq-pgpass.html) if you don't want to give specify your password.

Based on a [2015 project](https://github.com/jsfenfen/irs_527) by Jacob Fenton.
