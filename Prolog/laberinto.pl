%Laberinto a resolver
%   012345678
%
%0  111111111
%1  100010001
%2  10x000101
%3  100000y01
%4  100010001
%5  100001011
%6  111111111

conecta([1,1],[2,2]).
conecta([1,1],[1,2]).
conecta([1,2],[1,3]).
conecta([1,3],[2,3]).
conecta(inicio,[2,3]).
conecta(inicio,[3,2]).
conecta([2,3],[3,3]).
conecta([2,4],[2,5]).
conecta([2,4],[3,4]).
conecta([2,5],[3,5]).
conecta([3,1],[4,1]).
conecta([3,1],[3,2]).
conecta([3,2],[4,2]).
conecta([3,2],[3,3]).
conecta([3,3],[4,3]).
conecta([3,4],[3,5]).
conecta([3,5],[4,5]).
conecta([3,6],fin).
conecta([4,6],fin).

filas([X,Z],[X,W]) :- conecta([X,Z],[X,W]).
columnas([Z,Y],[W,Y]) :- conecta([Z,Y],[W,Y]).

resolver :- filas(inicio,[_,_]), columnas([_,_],fin).
