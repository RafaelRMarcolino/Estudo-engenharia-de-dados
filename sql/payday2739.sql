-- The Central Bank of Financing lost many registers after a server failure that happened last October. The collection dates for the parcels where lost.

-- The bank requested your help to select the names and day of month in which each client must pay theirs parcel.

-- OBS: The day of month must be an integer.

SELECT name, cast(EXTRACT(DAY FROM payday) AS INT) as day
FROM loan
