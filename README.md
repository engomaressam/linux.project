# Linux shell scripting: an incremental backup script and a forecast-accuracy pipeline

Two small Bash projects from the IBM *Linux Commands and Shell Scripting* course.

## `backup.sh`: back up what changed in the last 24 hours

```bash
./backup.sh <target_directory> <destination_directory>
```

Validates both arguments, finds every file in the target directory modified in the last 24 hours, archives them into `backup-<unix-timestamp>.tar.gz` and moves the archive to the destination. `backup-[1758127096].tar.gz` is a sample run over `important-documents/`.

## `practice_project/`: weather forecast vs. actuals

A cron-driven pipeline that logs a daily forecast and the observed temperature, then scores the forecast:

- `fc_accuracy.sh` reads `rx_poc.log`, computes the forecast error for the latest day and appends a row to `historical_fc_accuracy.tsv` with an accuracy band (excellent / good / fair / poor).
- `cron_instructions.txt` schedules the daily log and the scoring job.
- `historical_fc_accuracy.tsv` is the accumulated result.

The two PDFs are the write-ups submitted for the course.
