-- Lab 11 SQL Scripts

CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(name TEXT, phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT name, phone
    FROM phonebook
    WHERE name ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$;

CREATE OR REPLACE PROCEDURE insert_or_update_user(new_name TEXT, new_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE phonebook
    SET phone = new_phone
    WHERE name = new_name;
    IF NOT FOUND THEN
        INSERT INTO phonebook(name, phone) VALUES (new_name, new_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    invalid_entries TEXT[] := ARRAY[]::TEXT[];
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF i > array_length(phones, 1) OR phones[i] IS NULL THEN
            invalid_entries := array_append(invalid_entries, names[i] || ' (no phone)');
        ELSIF phones[i] !~ '^[0-9]{10,}$' THEN
            invalid_entries := array_append(invalid_entries, names[i] || ' - ' || phones[i]);
        ELSE
            BEGIN
                INSERT INTO phonebook(name, phone) VALUES (names[i], phones[i]);
            EXCEPTION WHEN unique_violation THEN
                UPDATE phonebook SET phone = phones[i] WHERE name = names[i];
            END;
        END IF;
    END LOOP;
    
    IF array_length(invalid_entries, 1) > 0 THEN
        RAISE NOTICE 'Invalid entries: %', invalid_entries;
    ELSE
        RAISE NOTICE 'All entries successfully inserted/updated.';
    END IF;
END;
$$;

CREATE OR REPLACE FUNCTION paginate_phonebook(p_limit INT, p_offset INT)
RETURNS TABLE(name TEXT, phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT name, phone
    FROM phonebook
    ORDER BY name
    LIMIT p_limit OFFSET p_offset;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_user(name TEXT, phone TEXT)
LANGUAGE plpgsql
AS $$
DECLARE
    rows_deleted INT;
BEGIN
    DELETE FROM phonebook
    WHERE (name IS NOT NULL AND phonebook.name = name)
       OR (phone IS NOT NULL AND phonebook.phone = phone);
       
    GET DIAGNOSTICS rows_deleted = ROW_COUNT;
    
    IF rows_deleted = 0 THEN
        RAISE NOTICE 'No contact found.';
    ELSE
        RAISE NOTICE 'Deleted % contact(s).', rows_deleted;
    END IF;
END;
$$;