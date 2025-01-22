CREATE TABLE "items_tags" (
	"id"	INTEGER,
	"item_id"	INTEGER NOT NULL,
	"tag_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("item_id") REFERENCES "items"("id"),
	FOREIGN KEY("tag_id") REFERENCES "tags"("id")
);