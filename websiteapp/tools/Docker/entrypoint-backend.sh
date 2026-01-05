#!/bin/sh
set -e
DB_ENGINE=${DB_ENGINE:-mysql}
if [ "$DB_ENGINE" = "mysql" ]; then
    export DB_HOST=${DB_HOST:-mysql}
    export DB_PORT=${DB_PORT:-3306}
    export DB_USER=${DB_USER:-root}
    export DB_PASSWORD=${DB_PASSWORD:-123456}
    export DB_NAME=${DB_NAME:-websiteguide}
    cd /WebsiteGuide
    i=0
    until python manage.py updatedb; do
        i=$((i+1))
        if [ "$i" -ge 30 ]; then
            exit 1
        fi
        sleep 2
    done
    python manage.py useradd -u admin -p admin -s -n 管理员 || true
else
    if [ ! -f /WebsiteGuide/db.sqlite3 ]; then
        cd /WebsiteGuide
        python manage.py updatedb
        python manage.py useradd -u admin -p admin -s -n 管理员
    fi
fi
sh /WebsiteGuide/websiteapp/tools/start-api.sh
