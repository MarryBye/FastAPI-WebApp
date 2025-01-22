CREATE TABLE "accounts" (
	"id"	INTEGER,
	"login"	TEXT UNIQUE,
	"password"	TEXT,
	"nickname"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);