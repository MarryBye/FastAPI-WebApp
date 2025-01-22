CREATE TABLE "admins" (
	"id"	INTEGER,
	"account_id"	INTEGER UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("account_id") REFERENCES "accounts"("id")
);