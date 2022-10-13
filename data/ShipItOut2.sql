CREATE TABLE "User" (
  "id" int PRIMARY KEY,
  "first_name" varchar,
  "last_name" varchar,
  "username" varchar,
  "email" email,
  "password" password,
  "groups" varchar,
  "user_permissions" varchar,
  "is_superuser" boolean,
  "is_active" boolean,
  "is_staff" boolean,
  "last_login" datetime,
  "date_joined" datetime
);

CREATE TABLE "AppUser" (
  "id" pk,
  "user_id" int,
  "company" varchar,
  "role" varchar,
  "phone" phone,
  "account_type" enum
);

CREATE TABLE "Booking" (
  "id" int,
  "booking" varchar,
  "agent_id" pk,
  "carrier_id" int,
  "voyage_id" int,
  "loading_port_id" int,
  "unloading_port_id" int,
  "loading_origin_address" address,
  "unloading_destination_address" address,
  "pickup_address" address,
  "delivery_address" address,
  "pickup_appt" date,
  "delivery_appt" date,
  "port_cutoff" date,
  "rail_cutoff" date,
  "are_documents_ready" boolean,
  "are_dues_paid" boolean,
  "has_issue" boolean,
  "booking_status" enum,
  "booking_notes" longtext
);

CREATE TABLE "Container" (
  "id" int,
  "container" varchar,
  "booking_id" int,
  "equipment_type" varchar,
  "equipment_location" enum,
  "is_container_damaged" boolean,
  "is_needs_inspection" boolean,
  "is_overweight" boolean,
  "is_in_use" boolean,
  "container_notes" longtext
);

CREATE TABLE "Port" (
  "id" pk,
  "name" varchar,
  "code" varchar
);

CREATE TABLE "Vessel" (
  "id" pk,
  "name" varchar
);

CREATE TABLE "Voyage" (
  "id" pk,
  "voyage" varchar,
  "vessel_id" int,
  "service" enum
);

CREATE TABLE "Product" (
  "id" pk,
  "container_id" int,
  "product" varchar,
  "weight" float,
  "is_product_damaged" boolean,
  "is_fragile" boolean,
  "is_reefer" boolean,
  "is_haz" boolean,
  "product_notes" longtext
);

ALTER TABLE "User" ADD FOREIGN KEY ("id") REFERENCES "AppUser" ("user_id");

ALTER TABLE "Booking" ADD FOREIGN KEY ("agent_id") REFERENCES "AppUser" ("id");

ALTER TABLE "Booking" ADD FOREIGN KEY ("carrier_id") REFERENCES "AppUser" ("id");

ALTER TABLE "Booking" ADD FOREIGN KEY ("voyage_id") REFERENCES "Voyage" ("id");

ALTER TABLE "Booking" ADD FOREIGN KEY ("loading_port_id") REFERENCES "Port" ("id");

ALTER TABLE "Booking" ADD FOREIGN KEY ("unloading_port_id") REFERENCES "Port" ("id");

ALTER TABLE "Container" ADD FOREIGN KEY ("booking_id") REFERENCES "Booking" ("id");

ALTER TABLE "Product" ADD FOREIGN KEY ("container_id") REFERENCES "Container" ("id");

ALTER TABLE "Voyage" ADD FOREIGN KEY ("vessel_id") REFERENCES "Vessel" ("id");
