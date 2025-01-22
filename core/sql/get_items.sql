SELECT 
	items.id,
	items.name,
	items.description,
	items.price,
	group_concat( concat(items.seller_id, "|", accounts.nickname) ) AS seller,
	group_concat( concat(tags.id, "|", tags.name) ) AS tags_list
FROM
	items
LEFT JOIN
	items_tags ON items_tags.item_id = items.id
LEFT JOIN
	tags ON items_tags.tag_id = tags.id
LEFT JOIN
	accounts ON items.seller_id = accounts.id
GROUP BY
	items.id