select * from periodo
insert into periodo(descperiodo) values('4to bimestre');
update periodo set descperiodo = '1er bimestre' where idperiodo = 1;
delete from periodo where idperiodo = 2;