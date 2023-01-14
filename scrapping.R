pacman::p_load(pacman,jsonlite,tidyverse,dplyr,httr,lubridate,date)

btc <- jsonlite::fromJSON("https://www.reddit.com/r/environment/.json")
df1 <- btc$data$children$data
df1
head(df1)
new1 <- df1[ ,c("author_fullname","title")]
utctime <- df1[ ,c("created_utc")]
new1
#utc to standart time

date <- lapply(utctime, function(x) as_datetime(x))
date2 <- as.character(date)
date3 <- as.list(date2)

new1$created <- date2

