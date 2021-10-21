-- CREATE TABLE inner_flights(
--     id SERIAL PRIMARY KEY,
--     from_region INT,
--     to_destination INT,
--     company VARCHAR,
--     quantity INT
-- );


-- INSERT INTO inner_flights(
--     from_region,
--     to_destination,
--     company,
--     quantity
-- )
-- VALUES(
-- 02,
-- 4000,
-- 'Kettik',
-- 17
-- );



-- CREATE TABLE outter_flights(
--     id SERIAL PRIMARY KEY,
--     from_country VARCHAR,
--     to_country VARCHAR,
--     flight_type VARCHAR,
--     company VARCHAR,
--     neighbors INT
-- )

INSERT INTO outter_flights(
    from_country,
    to_country,
    flight_type,
    company,
    neighbors
)
VALUES(
'Rusia',
'USA',
'People',
'TransGleb',
12
)

