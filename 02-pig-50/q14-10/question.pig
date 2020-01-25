--
-- Pregunta
-- ===========================================================================
--
-- Para responder la pregunta use el archivo `data.csv`.
--
-- Escriba el código equivalente a la siguiente consulta SQL.
--
--    SELECT
--        color
--    FROM
--        u
--    WHERE
--        color NOT LIKE 'b%';
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
data = FOREACH u GENERATE ($4);
data = FILTER data BY NOT (color MATCHES '.*b.*');


-- Escribe el archivo de salida
STORE data INTO 'output';
