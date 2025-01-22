SELECT 
    t.id, t.name 
FROM 
    tags AS t, 
    item_tags AS i_t
WHERE 
    t.id = i_t.tag_id
AND
    t.item_id = ?