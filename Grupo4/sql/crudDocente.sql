select * from docente
insert into docente(nombreDocente, apellidosDocente,curso_idcurso) values('Luciano','Ramirez',7)
insert into docente(nombreDocente, apellidosDocente,curso_idcurso) values('Javier','Bermudez',8)
insert into docente(nombreDocente, apellidosDocente,curso_idcurso) values('lucia','Rodriguez',5)
update docente set nombreDocente ='Xavier' where iddocente=2
delete from docente where iddocente=8