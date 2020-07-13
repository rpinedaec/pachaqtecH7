select * from promedio
insert into promedio(descPromedio, alumno_idalumno,curso_idcurso)
			values(14,1,1)
update promedio set descPromedio = 15 where idpromedio=1        
delete from promedio where idpromedio = 1