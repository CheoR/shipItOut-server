create table api_Container (
	id INT,
	container VARCHAR(50),
	equipment_size VARCHAR(7),
	container_status_id INT,
	is_damaged BOOLEAN,
	is_need_inspection BOOLEAN,
	is_overweight BOOLEAN,
	is_in_use BOOLEAN,
	notes TEXT
);
insert into api_Container (
		id,
		container,
		equipment_size,
		container_status_id,
		is_damaged,
		is_need_inspection,
		is_overweight,
		is_in_use,
		notes
	)
values (
		1,
		'WUSA2162',
		'40ST',
		4,
		true,
		true,
		false,
		true,
		'Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem. Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci.'
	);
insert into api_Container (
		id,
		container,
		equipment_size,
		container_status_id,
		is_damaged,
		is_need_inspection,
		is_overweight,
		is_in_use,
		notes
	)
values (
		2,
		'KFJL3381',
		'40OG',
		3,
		true,
		false,
		true,
		false,
		'Vestibulum quam sapien, varius ut, blandit non, interdum in, ante.'
	);
insert into api_Container (
		id,
		container,
		equipment_size,
		container_status_id,
		is_damaged,
		is_need_inspection,
		is_overweight,
		is_in_use,
		notes
	)
values (
		3,
		'TOTX0380',
		'20ST',
		3,
		true,
		false,
		true,
		true,
		'Fusce consequat.'
	);
insert into api_Container (
		id,
		container,
		equipment_size,
		container_status_id,
		is_damaged,
		is_need_inspection,
		is_overweight,
		is_in_use,
		notes
	)
values (
		4,
		'GNXI3314',
		'40ST',
		2,
		true,
		true,
		false,
		false,
		'Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.'
	);
insert into api_Container (
		id,
		container,
		equipment_size,
		container_status_id,
		is_damaged,
		is_need_inspection,
		is_overweight,
		is_in_use,
		notes
	)
values (
		5,
		'BZAJ1118',
		'40OG',
		3,
		true,
		false,
		false,
		false,
		'In congue. Etiam justo. Etiam pretium iaculis justo.'
	);