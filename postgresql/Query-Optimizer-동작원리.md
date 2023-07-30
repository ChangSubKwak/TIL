## CBO(Cost Based Optimizer)
- PostgreSQL은 CBO를 제공
- RBO(Rule Based Optimizer) Index가 존재하면 무조건 Seq Scan을 사용하는 방식이나, 서서히 사라지는 추세

### COST란?
- 단위는 없음
- 계산방식 : IO 비용 + CPU 비용
- Seq Scan 시 비용 계산 예제 코드
```SQL
drop table t1;
create table t1 (c1 integer, c2 integer);
insert into t1 select i, mod(i, 10) from generate_series(1,100000) a(i);
analyze t1;

-- 443, 1000
select relpages, reltuples from pg_class where relname='t1';

-- cost=0.00..1443.00
explain select * from t1;

-- io_cost = 443, cpu_cost = 10000
select relpages * current_setting('seq_page_cost')::float as io_cost,
       reltuples * current_setting('cpu_tuple_cost')::float as cpu_cost
from pg_catalog.pg_class 
where relname = 't1';
```

  
