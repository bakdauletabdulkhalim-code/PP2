CREATE OR REPLACE FUNCTION search_contacts(p TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.name, pb.phone
    FROM phonebook pb
    WHERE pb.name ILIKE '%' || p || '%'
       OR pb.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_paginated(limit_val INT, offset_val INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;