# Apache Drill
cool tool to search via SQL in text files in data lakes like S3

### Apache Drill via Docker
```
docker run -i -v /Users/aortner/Playground/jupyter/Graphtheory/data:/home --name drill-1.16.0 -p 8047:8047 -t drill/apache-drill:1.16.0 /bin/bash
``` 

### Read CSV file with headers

```sql
select * from table(dfs.`path/to/data.csv`(type => 'text',
fieldDelimiter => ',', extractHeader => true))
```

### With recursive queries
Apache Drill does not support recursive queries that would be able to get the cluster directly from the edge data
e.g. https://www.fusionbox.com/blog/detail/graph-algorithms-in-a-database-recursive-ctes-and-topological-sort-with-postgres/620/
```sql
WITH RECURSIVE traverse AS (
        SELECT id FROM task
        WHERE dependent_id = 3
    UNION ALL
        SELECT task.id FROM task
        INNER JOIN traverse
        ON task.dependent_id = traverse.id
)
SELECT id FROM traverse;
```