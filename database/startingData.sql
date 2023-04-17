INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('aturing', 'b93727798b520dc10d145b53909c061f082ff14cd5f8cb4ab24c3b71bfa57d7e12e1296029be74c06a0d91ba32756f9fc978047fbe7232be67f94dfc1de9ced9', 'alan@enigma.com', 'Alan', 'Turing');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('dritchie', '67aff785bd17ac24448d491926ff7aadd8fa75e51a2f7a9bfc31889bad0adcd2989061a27ccd9eff9e5e31f2bc14b5c193727e116dc8dc48259acb3919171cd4', 'dennis@unix.com', 'Dennis', 'Ritchie');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com', 'Leslie', 'Lamport');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com', 'Barbara', 'Liskov');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('God of War; Ragnarok', 'Fimbulwinter is well underway. Kratos and Atreus must journey to each of the Nine Realms in search of answers as Asgardian forces prepare for a prophesied battle that will end the world. Along the way they will explore stunning, mythical landscapes, and face fearsome enemies in the form of Norse gods and monsters. The threat of Ragnarök grows ever closer. Kratos and Atreus must choose between their own safety and the safety of the realms.', 60.00, 100, 'static\images\God_of_War_Ragnarök_cover.jpg', 'Videogame');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Divinity Original Sin 2', 'The Divine is dead. The Void approaches. And the powers lying dormant within you are soon to awaken. Choose your role in a BAFTA-winning story, and explore a world that reacts to who you are, and the choices you make. With five races to choose from, and an adventure playable solo or as a party of up to four, lay waste to an oppressive order in a world afraid of magic. Become the God the world so desperately needs.', 40.00, 50, 'static\images\Divinity-Original-Sin-II-Cover-Art-001.jpg', 'Videogame');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('For the King', 'For The King is a strategic RPG that blends tabletop and roguelike elements in a challenging adventure that spans the realms', 20.00, 30, 'static\images\For_the_King_Cover_Art.jpg', 'Videogame');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Minecraft', 'Experience Minecraft in a whole new light—or dark. Evade the warden in the deep dark if you dare. Explore the swamps together with frogs and tadpoles. Ask an allay to collect supplies to fill the chest on your boat. Build with sculk, mud, and mangrove wood. The choices are endless, and all of them yours.', 26.00, 100, 'static\images\Minecraft_game_cover.jpeg', 'Videogame');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Prey', 'Prey is a first-person shooter with role-playing and stealth elements set in an open world environment. The player takes the role of Morgan Yu, a human aboard a space station with numerous species of hostile aliens known collectively as the Typhon.', 30.00, 75, 'static\images\Prey_cover_art.jpg', 'Videogame');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Risk of Rain 2', 'Escape a chaotic alien planet by fighting through hordes of frenzied monsters; with your friends, or on your own.', 16.00, 30, 'static\images\Risk_of_Rain_cover.jpg', 'Videogame');

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('1', 'aturing', '1', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('2', 'dritchie', '2', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('3', 'llamport', '3', 10, '2022-12-21 7:30:30', 5.50);
