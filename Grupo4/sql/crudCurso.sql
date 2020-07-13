#crud curso
select * from curso
insert into curso(nombreCurso, salon_idsalon) values('Computacion',1)
insert into curso(nombreCurso, salon_idsalon) values('ingles',2)
update curso set nombreCurso ='quimica' where idcurso = 5
delete from curso where idcurso = 6;