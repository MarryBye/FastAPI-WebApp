CREATE TABLE "items" (
	"id"	INTEGER,
	"name"	TEXT DEFAULT 'N/D',
	"description"	TEXT DEFAULT 'N/D',
	"price"	REAL DEFAULT 1.99,
	"category_id"	INTEGER NOT NULL,
	"seller_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("category_id") REFERENCES "categories"("id"),
	FOREIGN KEY("seller_id") REFERENCES "sellers"("id")
);