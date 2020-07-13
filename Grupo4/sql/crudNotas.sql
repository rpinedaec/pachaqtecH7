select * from notas
insert into notas(descNotas, alumno_idalumno, periodo_idperiodo, docente_iddocente, curso_idcurso)
			values(14,1,1,1,1)
insert into notas(descNotas, alumno_idalumno, periodo_idperiodo, docente_iddocente, curso_idcurso)
			values(15,1,1,1,1)
insert into notas(descNotas, alumno_idalumno, periodo_idperiodo, docente_iddocente, curso_idcurso)
			values(12,1,4,1,1)            
update notas set descNotas = 13 where idnotas=4
delete from notas where idnotas=4    