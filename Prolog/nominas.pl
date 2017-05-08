%hc -> hora catedra
%hn -> honorarios

%semanas del semestre
semestre(18).

%categoria, tipo_contrato, valor * hora
categoria('asistente', 'hc', 200000).
categoria('auxiliar', 'tco', 150000).
categoria('planta', 'mto', 500000).

%nombre_profesor, tipo_contrato, categoria, horas_trabajadas(semanalmente)
docente('alejandro', 'hc', 'asistente', 40).
docente('carlos','mto', 'planta', 80).

%tipo_contrato, valor_horas_extra
adicional('tco', 1.25).
adicional('mto', 1.16).
adicional('hc', 1).
adicional('hn', 1).

salario(A,Y) :- categoria(C,T,V),docente(A,T,C,H),adicional(T,Z),semestre(S),Y is ((V*(H*S))*Z).
