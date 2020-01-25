-- Pregunta
-- ===========================================================================
--
-- Para responder la pregunta use el archivo `data.csv`.
--
-- Genere una relación con el apellido y su longitud. Ordene por longitud y
-- por apellido. Obtenga la siguiente salida.
--
--   Hamilton,8
--   Garrett,7
--   Holcomb,7
--   Coffey,6
--   Conway,6
--
-- Escriba el resultado a la carpeta `output` del directorio actual.
--
fs -rm -f -r output;
--
u = LOAD 'data.csv' USING PigStorage(',')
    AS (id:int,
        firstname:CHARARRAY,
        surname:CHARARRAY,
        birthday:CHARARRAY,
        color:CHARARRAY,
        quantity:INT);
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
u = FOREACH u GENERATE ($2), SIZE($2);
u = FILTER u BY surname == 'Hamilton' OR surname == 'Garrett' OR surname == 'Holcomb' OR surname == 'Coffey' OR surname == 'Conway';
u = ORDER u BY $1 DESC;


-- Escribe el archivo de salida
STORE u INTO 'output' USING PigStorage(',');