CREATE TABLE "User" (
  "id" int PRIMARY KEY,
  "email" email,
  "first_name" varchar,
  "last_name" varchar,
  "password" password,
  "groups" varchar,
  "user_permissions" varchar,
  "is_staff" boolean,
  "is_active" boolean,
  "is_superuser" boolean,
  "last_login" datetime,
  "date_joined" datetime
);

CREATE TABLE "AppUser" (
  "id" pk,
  "user_id" int,
  "company" varchar,
  "company_role" varchar,
  "phone" phone
);

CREATE TABLE "Booking" (
  "id" int,
  "user_id" pk,
  "booking" varchar,
  "voyage_reference_id" int,
  "container_id" int,
  "carrier_id" int,
  "loading_origin" varchar,
  "unloading_destination" varchar,
  "pickup_address" address,
  "pickup_appt" date,
  "notes" varchar,
  "port_id" int,
  "port_cutoff" date,
  "rail_cutoff" date,
  "documents_id" int,
  "dues_id" int,
  "has_issue" boolean,
  "booking_status_id" int
);

CREATE TABLE "Document" (
  "id" pk,
  "are_docs_ready" boolean
);

CREATE TABLE "Due" (
  "id" pk,
  "are_dues_paid" boolean
);

CREATE TABLE "Carrier" (
  "id" pk,
  "name" varchar
);

CREATE TABLE "Container" (
  "id" int,
  "container" varchar,
  "equipmend_size" varchar,
  "container_status_id" int,
  "is_damaged" boolean,
  "is_need_inspection" boolean,
  "is_overweight" boolean,
  "is_in_use" boolean,
  "notes" varchar
);

CREATE TABLE "Port" (
  "id" pk,
  "name" varchar,
  "location" varchar,
  "code" varchar
);

CREATE TABLE "Voyage" (
  "id" pk,
  "voyage" varchar,
  "vessel_id" int
);

CREATE TABLE "Product" (
  "id" pk,
  "commodity" varchar,
  "weight" float,
  "is_fragile" boolean,
  "is_haz" boolean,
  "is_damaged" boolean,
  "is_reefer" boolean,
  "container_id" int
);

CREATE TABLE "CntrStatus" (
  "id" pk,
  "status" varchar
);

CREATE TABLE "BkgStatus" (
  "id" pk,
  "status" varchar
);

CREATE TABLE "Vessel" (
  "id" pk,
  "name" varchar,
  "longitude" float,
  "latitude" float,
  "service_id" int
);

CREATE TABLE "Service" (
  "id" pk,
  "name" varchar
);

ALTER TABLE "User" ADD FOREIGN KEY ("id") REFERENCES "AppUser" ("user_id");

ALTER TABLE "Booking" ADD FOREIGN KEY ("user_id") REFERENCES "AppUser" ("user_id");

ALTER TABLE "Booking" ADD FOREIGN KEY ("carrier_id") REFERENCES "Carrier" ("id");

ALTER TABLE "Container" ADD FOREIGN KEY ("id") REFERENCES "Booking" ("container_id");

ALTER TABLE "Booking" ADD FOREIGN KEY ("voyage_reference_id") REFERENCES "Voyage" ("id");

ALTER TABLE "Document" ADD FOREIGN KEY ("id") REFERENCES "Booking" ("documents_id");

ALTER TABLE "Due" ADD FOREIGN KEY ("id") REFERENCES "Booking" ("dues_id");

ALTER TABLE "Booking" ADD FOREIGN KEY ("port_id") REFERENCES "Port" ("id");

ALTER TABLE "BkgStatus" ADD FOREIGN KEY ("id") REFERENCES "Booking" ("booking_status_id");

ALTER TABLE "Vessel" ADD FOREIGN KEY ("service_id") REFERENCES "Service" ("id");

ALTER TABLE "Voyage" ADD FOREIGN KEY ("vessel_id") REFERENCES "Vessel" ("id");

ALTER TABLE "Product" ADD FOREIGN KEY ("container_id") REFERENCES "Container" ("id");

ALTER TABLE "CntrStatus" ADD FOREIGN KEY ("id") REFERENCES "Container" ("container_status_id");
