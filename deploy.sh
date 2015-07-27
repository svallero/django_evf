#!/bin/bash
  set -e
  LOGFILE=/var/log/evf.log
  LOGDIR=$(dirname $LOGFILE)
  # Number of worker processes. 
  # Should be no less than the number of cores available and a popular formula
  # is 1 + 2 * number of cores. 
  NUM_WORKERS=5

  USER=evf

  GROUP=evf

  cd /root/evf/django_evf

  # Activate the virtualenv - replace the path with the path to wherever your venv lives.
  source /root/evf/django_evf/venv/bin/activate

  test -d $LOGDIR || mkdir -p $LOGDIR

  # Finally, the invocation
  gunicorn evf.wsgi:application -w $NUM_WORKERS \
      --user=$USER --group=$GROUP --log-level=debug \
      --log-file=$LOGFILE 2>>$LOGFILE
