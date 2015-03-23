# all the data we need about Civilization 5
# partly scraped from http://www.civfanatics.com/ and http://civilization.wikia.com/wiki/Civilization_V
# otherwise written by hand

# TODO: serve my own images

# info on civilization names, abilities, leaders, unique units/improvements/buildings
civs = [{'unique1': 'B17', 'unique2': 'Minuteman', 'name': 'America', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/washington.png" width="150" height="150" />', 'ability_name': 'Manifest Destiny', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/america.png" width="150" height="150" />', 'ability_desc': 'All land military units have +1 sight. 50% discount when purchasing tiles.', 'leader': 'Washington'},
        {'unique1': 'Camel Archer', 'unique2': 'Bazaar', 'name': 'Arabia', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/harunalrashid.png" width="150" height="150" />', 'ability_name': 'Ships of the Desert', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/arabia.png" width="150" height="150" />', 'ability_desc': "Caravans gain 50% extended range. Your trade routes spread the home city's religion twice as effectively. Oil resources are doubled.", 'leader': 'Harun al-Rashid'},
        {'unique1': 'Siege Tower', 'unique2': 'Royal Library', 'name': 'Assyria', 'leader_image': '<img src="http://images4.wikia.nocookie.net/__cb20130324151254/civilization/images/5/51/Ashurbanipal_%28Civ5%29.png" width="110" height="120" />', 'ability_name': 'Treasures of Nineveh', 'civ_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/CIVILIZATION_ASSYRIA.png" width="150" height="150" />', 'ability_desc': 'When a city is conquered, gain a free Technology already discovered by its owner. Gaining a city through a trade deal does not count, and it can only happen once per enemy city.', 'leader': 'Ashurbanipal'},
        {'unique1': 'Hussar', 'unique2': 'Coffee House', 'name': 'Austria', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/maria.png" width="150" height="150" />', 'ability_name': 'Diplomatic Marriage', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/austria.png" width="150" height="150" />', 'ability_desc': 'Can spend Gold to annex or puppet a City-State that has been your ally for 5 turns.', 'leader': 'Maria Theresa'},
        {'unique1': 'Jaguar', 'unique2': 'Floating Gardens', 'name': 'Aztecs', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/montezuma.png" width="150" height="150" />', 'ability_name': 'Sacrificial Captives', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/aztec.png" width="150" height="150" />', 'ability_desc': 'Gains Culture for the empire from each enemy unit killed.', 'leader': 'Montezuma'},
        {'unique1': 'Bowman', 'unique2': 'Walls of Babylon', 'name': 'Babylon', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/nebuchadnezzar.png" width="150" height="150" />', 'ability_name': 'Ingenuity', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/babylon.png" width="150" height="150" />', 'ability_desc': 'Receive free Great Scientist when you discover Writing. Earn Great Scientists 50% faster.', 'leader': 'Nebuchadnezzar II'},
        {'unique1': 'Pracinha', 'unique2': 'Brazilwood Camp', 'name': 'Brazil', 'leader_image': '<img src="http://images2.wikia.nocookie.net/__cb20130705142150/civilization/images/f/f8/Pedro_II_%28Civ5%29.png" width="110" height="115" />', 'ability_name': 'Carnival', 'civ_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/CIVILIZATION_BRAZIL.png" width="150" height="150" />', 'ability_desc': 'Tourism output is +100% during their Golden Ages. Earn Great Artists, Musicians, and Writers 50% faster during their Golden Ages.', 'leader': 'Pedro II'},
        {'unique1': 'Cataphract', 'unique2': 'Dromon', 'name': 'Byzantium', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/theodora.png" width="150" height="150" />', 'ability_name': 'Patriarchate of Constantinople', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/byzantium.png" width="150" height="150" />', 'ability_desc': 'Choose one more Belief than normal when you found a Religion.', 'leader': 'Theodora'},
        {'unique1': 'African Forest Elephant', 'unique2': 'Quinquereme', 'name': 'Carthage', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/dido.png" width="150" height="150" />', 'ability_name': 'Phoenician Heritage', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/carthage.png" width="150" height="150" />', 'ability_desc': 'All coastal Cities get a free Harbor. Units may cross mountains after the first Great General is earned, taking 50 HP damage if they end a turn on a mountain.', 'leader': 'Dido'},
        {'unique1': 'Pictish Warrior', 'unique2': 'Ceilidh Hall', 'name': 'Celts', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/boudicca.png" width="150" height="150" />', 'ability_name': 'Druidic Lore', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/celts.png" width="150" height="150" />', 'ability_desc': '+1 Faith per city with an adjacent unimproved Forest. Bonus increases to +2 Faith in Cities with 3 or more adjacent unimproved Forest tiles.', 'leader': 'Boudicca'},
        {'unique1': 'Chu-Ko-Nu', 'unique2': 'Paper Maker', 'name': 'China', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/wuzetian.png" width="150" height="150" />', 'ability_name': 'Art of War', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/china.png" width="150" height="150" />', 'ability_desc': 'The Great General combat bonus is increased by 15%, and their spawn rate is increased by 50%.', 'leader': 'Wu Zetian'},
        {'unique1': 'Berserker', 'unique2': 'Norwegian Ski Infantry', 'name': 'Denmark', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/haraldbluetooth.png" width="150" height="150" />', 'ability_name': 'Viking Fury', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/denmark.png" width="150" height="150" />', 'ability_desc': 'Embarked units have +1 Movement and pay just 1 movement point to move from sea to land. Melee units pay no movement point cost to pillage.', 'leader': 'Harald Bluetooth'},
        {'unique1': 'War Chariot', 'unique2': 'Burial Tomb', 'name': 'Egypt', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/ramesses.png" width="150" height="150" />', 'ability_name': 'Monument Builders', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/egypt.png" width="150" height="150" />', 'ability_desc': '+20% Production towards Wonder construction.', 'leader': 'Ramesses II'},
        {'unique1': 'Longbowman', 'unique2': 'Ship of the Line', 'name': 'England', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/elizabeth.png" width="150" height="150" />', 'ability_name': 'Sun Never Sets', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/england.png" width="150" height="150" />', 'ability_desc': '+2 Movement for all naval units. Receives 1 extra Spy.', 'leader': 'Elizabeth'},
        {'unique1': 'Mehal Sefari', 'unique2': 'Stele', 'name': 'Ethiopia', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/selassie.png" width="150" height="150" />', 'ability_name': 'Spirit of Adwa', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/ethiopia.png" width="150" height="150" />', 'ability_desc': 'Combat bonus (+20%) when fighting units from a Civilization with more Cities than Ethiopia.', 'leader': 'Haile Selassie'},
        {'unique1': 'Musketeer', 'unique2': 'Chateau', 'name': 'France', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/napoleon.png" width="150" height="150" />', 'ability_name': 'City of Light', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/france.png" width="150" height="150" />', 'ability_desc': 'Museum and World Wonder theming bonuses are doubled in their capital.', 'leader': 'Napoleon'},
        {'unique1': 'Panzer', 'unique2': 'Hanse', 'name': 'Germany', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/bismarck.png" width="150" height="150" />', 'ability_name': 'Furor Teutonicus', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/germany.png" width="150" height="150" />', 'ability_desc': 'Upon defeating a Barbarian unit inside an encampment, there is a 67% chance you earn 25 Gold and they join your side. Pay 25% less for land unit maintenance.', 'leader': 'Bismarck'},
        {'unique1': 'Companion Cavalry', 'unique2': 'Hoplite', 'name': 'Greece', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/alexander.png" width="150" height="150" />', 'ability_name': 'Hellenic League', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/greece.png" width="150" height="150" />', 'ability_desc': 'City-State Influence degrades at half and recovers at twice the normal rate. ', 'leader': 'Alexander'},
        {'unique1': 'Horse Archer', 'unique2': 'Battering Ram', 'name': 'Huns', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/attila.png" width="150" height="150" />', 'ability_name': 'Scourge of God', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/huns.png" width="150" height="150" />', 'ability_desc': 'Raze Cities at double speed. Borrow City names from other in-game Civs. Start with Animal Husbandry technology. +1 Production per Pasture.', 'leader': 'Attila'},
        {'unique1': 'Slinger', 'unique2': 'Terrace Farm', 'name': 'Inca', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/pachacuti.png" width="150" height="150" />', 'ability_name': 'Great Andean Road', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/inca.png" width="150" height="150" />', 'ability_desc': 'Units ignore terrain costs when moving into any tile with Hills. No maintenance costs for improvements in Hills; half cost elsewhere.', 'leader': 'Pachacuti'},
        {'unique1': 'War Elephant', 'unique2': 'Mughal Fort', 'name': 'India', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/gandhi.png" width="150" height="150" />', 'ability_name': 'Population Growth', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/india.png" width="150" height="150" />', 'ability_desc': 'Unhappiness from number of Cities doubled, Unhappiness from number of Citizens halved.', 'leader': 'Gandhi'},
        {'unique1': 'Kris Swordsman', 'unique2': 'Candi', 'name': 'Indonesia', 'leader_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/LEADER_GAJAH_MADA.png" width="150" height="150" />', 'ability_name': 'Spice Islanders', 'civ_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/CIVILIZATION_INDONESIA.png" width="150" height="150" />', 'ability_desc': 'The first 3 cities founded on continents other than where Indonesia started each provide 2 unique Luxury Resources (and can never be razed).', 'leader': 'Gajah Mada'},
        {'unique1': 'Mohawk Warrior', 'unique2': 'Longhouse', 'name': 'Iroquois', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/hiawatha.png" width="150" height="150" />', 'ability_name': 'The Great Warpath', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/iroquois.png" width="150" height="150" />', 'ability_desc': 'Units move through Forest and Jungle in friendly territory as if they were Roads. These tiles can be used to establish City Connections upon researching The Wheel. Caravans move along Forest and Jungle as if they were Roads.', 'leader': 'Hiawatha'},
        {'unique1': 'Samurai', 'unique2': 'Zero', 'name': 'Japan', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/odanobunga.png" width="150" height="150" />', 'ability_name': 'Bushido', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/japan.png" width="150" height="150" />', 'ability_desc': 'Units fight as though they were at full strength even when damaged. +1 Culture from each Fishing Boat and +2 Culture from each Atoll', 'leader': 'Oda Nobunaga'},
        {'unique1': 'Turtle Ship', 'unique2': "Hwach'a", 'name': 'Korea', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/sejong.png" width="150" height="150" />', 'ability_name': 'Scholars of the Jade Hall', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/korea.png" width="150" height="150" />', 'ability_desc': '+2 science for all specialists and for all Great Person tile improvements. Receive a tech boost each time a scientific building/Wonder is built in the Korean capital.', 'leader': 'Sejong'},
        {'unique1': 'Atlatlist', 'unique2': 'Pyramid', 'name': 'Maya', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/pacal.png" width="150" height="150" />', 'ability_name': 'The Long Count', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/maya.png" width="150" height="150" />', 'ability_desc': 'After researching Theology, receive a bonus Great Person at the end of every Maya Long Count calendar cycle (every 394 years). Each bonus person can only be chosen once.', 'leader': 'Pacal'},
        {'unique1': 'Keshik', 'unique2': 'Khan', 'name': 'Mongolia', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/genghiskhan.png" width="150" height="150" />', 'ability_name': 'Mongol Terror', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/mongolia.png" width="150" height="150" />', 'ability_desc': 'Combat Strength +30% when fighting City-State units or attacking a City-State itself. All mounted units have +1 Movement.', 'leader': 'Genghis Khan'},
        {'unique1': 'Berber Cavalry', 'unique2': 'Kasbah', 'name': 'Morocco', 'leader_image': '<img src="http://www.civfanatics.com/gallery/files/2/3/2/4/9/9/ahmadalmansur.png" width="150" height="150" />', 'ability_name': 'Gateway to Africa', 'civ_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/CIVILIZATION_MOROCCO.png" width="150" height="150" />', 'ability_desc': 'Receives +3 Gold and +1 Culture for each Trade Route with a different civ or City-State. The Trade Route owners receive +2 Gold for each Trade Route sent to Morocco.', 'leader': 'Ahmad al-Mansur'},
        {'unique1': 'Sea Beggar', 'unique2': 'Polder', 'name': 'Netherlands', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/william.png" width="150" height="150" />', 'ability_name': 'Dutch East India Company', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/netherlands.png" width="150" height="150" />', 'ability_desc': 'Retains 50% of the Happiness benefits from a Luxury Resource if your last copy of it is traded away.', 'leader': 'William'},
        {'unique1': 'Janissary', 'unique2': 'Sipahi', 'name': 'Ottomans', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/suleiman.png" width="150" height="150" />', 'ability_name': 'Barbary Corsairs', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/ottomans.png" width="150" height="150" />', 'ability_desc': 'All melee naval units have the Prize Ships promotion, allowing them to capture defeated ships. Pay only one-third the usual cost for naval unit maintenance.', 'leader': 'Suleiman'},
        {'unique1': 'Immortal', 'unique2': "Satrap's Court", 'name': 'Persia', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/darius.png" width="150" height="150" />', 'ability_name': 'Achaemenid Legacy', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/persia.png" width="150" height="150" />', 'ability_desc': 'Golden Ages last 50% longer. During a Golden Age, units recieve +1 Movement and a +10% Combat Strength bonus.', 'leader': 'Darius I'},
        {'unique1': 'Winged Hussar', 'unique2': 'Ducal Stable', 'name': 'Poland', 'leader_image': '<img src="http://images3.wikia.nocookie.net/__cb20130706023815/civilization/images/d/d6/Casimir_III_%28Civ5%29.png" width="110" height="130" />', 'ability_name': 'Solidarity', 'civ_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/CIVILIZATION_POLAND.png" width="150" height="150" />', 'ability_desc': 'Receive a free Social Policy at the start of each new Era.', 'leader': 'Casimir III'},
        {'unique1': 'Maori Warrior', 'unique2': 'Moai', 'name': 'Polynesia', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/kamehameha.png" width="150" height="150" />', 'ability_name': 'Wayfinding', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/polynesia.png" width="150" height="150" />', 'ability_desc': 'Can embark and move over Oceans immediately. +1 Sight when embarked. +10% Combat Strength bonus if within 2 tiles of a Moai.', 'leader': 'Kamehameha'},
        {'unique1': 'Nau', 'unique2': 'Feitoria', 'name': 'Portugal', 'leader_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/LEADER_MARIA_I.png" width="150" height="150" />', 'ability_name': 'Mare Clausum', 'civ_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/CIVILIZATION_PORTUGAL.png" width="150" height="150" />', 'ability_desc': 'Resource diversity grants twice as much Gold for Portugal in International Trade Routes.', 'leader': 'Maria I'},
        {'unique1': 'Ballista', 'unique2': 'Legion', 'name': 'Rome', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/augustuscaesar.png" width="150" height="150" />', 'ability_name': 'The Glory of Rome', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/rome.png" width="150" height="150" />', 'ability_desc': '+25% Production towards any buildings that already exist in the Capital.', 'leader': 'Augustus Caesar'},
        {'unique1': 'Cossack', 'unique2': 'Krepost', 'name': 'Russia', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/catherine.png" width="150" height="150" />', 'ability_name': 'Siberian Riches', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/russia.png" width="150" height="150" />', 'ability_desc': 'Strategic Resources provide +1 Production and Horse, Iron and Uranium Resources provide double quantity.', 'leader': 'Catherine'},
        {'unique1': 'Pathfinder', 'unique2': 'Comanche Riders', 'name': 'Shoshone', 'leader_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/LEADER_POCATELLO.png" width="150" height="150" />', 'ability_name': 'Great Expanse', 'civ_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/CIVILIZATION_SHOSHONE.png" width="150" height="150" />', 'ability_desc': 'Founded cities start with additional territory. Units receive a combat bonus when fighting in their own territory.', 'leader': 'Pocatello'},
        {'unique1': 'Naresuan\'s Elephant', 'unique2': 'Wat', 'name': 'Siam', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/ramkhamhaeng.png" width="150" height="150" />', 'ability_name': 'Father Governs Children', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/siam.png" width="150" height="150" />', 'ability_desc': 'Food, Culture and Faith from friendly City-States increased by 50%.', 'leader': 'Ramkhamhaeng'},
        {'unique1': 'Mandekalu Cavalry', 'unique2': 'Mud Pyramid Mosque', 'name': 'Songhai', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/askia.png" width="150" height="150" />', 'ability_name': 'River Warlord', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/songhai.png" width="150" height="150" />', 'ability_desc': 'Receive triple Gold from Barbarian encampments and pillaging Cities. Land units gain the War Canoe and Amphibious promotions, strengthening them while embarked.', 'leader': 'Askia'},
        {'unique1': 'Tercio', 'unique2': 'Conquistador', 'name': 'Spain', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/isabella.png" width="150" height="150" />', 'ability_name': 'Seven Cities of Gold', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/spain.png" width="150" height="150" />', 'ability_desc': 'Gold bonus for discovering a Natural Wonder (bonus enhanced if first to discover it). Culture, happiness, and tile yields from Natural Wonders doubled.', 'leader': 'Isabella'},
        {'unique1': 'Hakkapeliitta', 'unique2': 'Carolean', 'name': 'Sweden', 'leader_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/leaders/big/gustavusadolphus.png" width="150" height="150" />', 'ability_name': 'Nobel Prize', 'civ_image': '<img src="http://forums.civfanatics.com/images/war_academy/civ5/civs/big/sweden.png" width="150" height="150" />', 'ability_desc': 'Gain 90 Influence with a Great Person gift to a City-State. When declaring friendship, Sweden and their friend gain a +10% boost to Great Person generation.', 'leader': 'Gustavus Adolphus'},
        {'unique1': 'Merchant of Venice', 'unique2': 'Great Galleass', 'name': 'Venice', 'leader_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/LEADER_ENRICO_DANDOLO.png" width="150" height="150" />', 'ability_name': 'Serenissima', 'civ_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/CIVILIZATION_VENICE.png" width="150" height="150" />', 'ability_desc': 'Cannot gain settlers nor annex cities. Double the normal number of Trade Routes available. A Merchant of Venice appears after researching Optics. May purchase in puppeted cities.', 'leader': 'Enrico Dandolo'},
        {'unique1': 'Impi', 'unique2': 'Ikanda', 'name': 'Zulus', 'leader_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/LEADER_SHAKA.png" width="150" height="150" />', 'ability_name': 'Iklwa', 'civ_image': '<img src="http://www.dndjunkie.com/civilopedia/images/large/CIVILIZATION_ZULU.png" width="150" height="150" />', 'ability_desc': 'Melee units cost 50% less maintenance; all military units require 25% less XP to earn a promotion. ', 'leader': 'Shaka'}]

# info victory types
victories = [{'name': 'Science Victory', 'desc': 'Build and launch a spaceship headed for Alpha Centauri'},
             {'name': 'Time Victory', 'desc': 'Have the most points when the game finishes in the year 2050 AD'},
             {'name': 'Domination Victory', 'desc': 'Control every civilization\'s capital as well as your own'},
             {'name': 'Cultural Victory', 'desc': 'Amass enough tourism to become influential on every other civilization in the game'},
             {'name': 'Diplomatic Victory', 'desc': 'Win a majority vote for World Leader'}]

# religion names
religions = [{'name': 'Buddhism'},
             {'name': 'Catholicism'},
             {'name': 'Confucianism'},
             {'name': 'Eastern Orthodoxy'},
             {'name': 'Hinduism'},
             {'name': 'Islam'},
             {'name': 'Judaism'},
             {'name': 'Protestantism'},
             {'name': 'Shinto'},
             {'name': 'Sikhism'},
             {'name': 'Taoism'},
             {'name': 'Tengriism'},
             {'name': 'Zoroastrianism'}]

# info pantheon beliefs
pantheons = [{'name': 'Ancestor Worship', 'desc': '+1 Culture from Shrines'},
             {'name': 'Dance of the Aurora', 'desc': '+1 Faith from Tundra tiles without Forest (Resource tiles on Tundra without Forest also qualify)'},
             {'name': 'Desert Folklore', 'desc': '+1 Faith from Desert tiles (All types, including Flood plains and Oasis, as well as Resource tiles on desert)'},
             {'name': 'Earth Mother', 'desc': '+1 Faith for each Copper, Iron, and Salt resource'},
             {'name': 'Faith Healers', 'desc': '+30 HP healed per turn if adjacent to a friendly city'},
             {'name': 'Fertility Rites', 'desc': '10% faster Growth rates'},
             {'name': 'God of Craftsmen', 'desc': '+1 Production in cities with Population of 3+'},
             {'name': 'God of the Open Sky', 'desc': '+1 Culture from Pastures'},
             {'name': 'God of the Sea', 'desc': '+1 Production from Fishing Boats'},
             {'name': 'God of War', 'desc': 'Gain Faith if you win a battle within 4 tiles from your city'},
             {'name': 'Goddess of Festivals', 'desc': '+1 Culture and +1 Faith for each Wine and Incense'},
             {'name': 'Goddess of Love', 'desc': '+1 Happiness from cities with Population of 6+'},
             {'name': 'Goddess of Protection', 'desc': '+30% increase in city Ranged Combat Strength'},
             {'name': 'Goddess of the Hunt', 'desc': '+1 Food from Camps'},
             {'name': 'God-King', 'desc': 'Palace provides +1 Culture, Faith, Gold, Production, and Science'},
             {'name': 'Messenger of the Gods', 'desc': '+2 Science in cities with a City Connection'},
             {'name': 'Monument to the Gods', 'desc': '+15% Production for Ancient/Classical Wonders'},
             {'name': 'One with Nature', 'desc': '+4 Faith from Natural Wonders'},
             {'name': 'Oral Tradition', 'desc': '+1 Culture from Plantations'},
             {'name': 'Religious Idols', 'desc': '+1 Culture and +1 Faith for each Gold and Silver'},
             {'name': 'Religious Settlements', 'desc': '15% faster border growth'},
             {'name': 'Sacred Path', 'desc': '+1 Culture from Jungle tiles (Resource tiles in a Jungle also qualify)'},
             {'name': 'Sacred Waters', 'desc': '+1 Happiness from cities on rivers'},
             {'name': 'Stone Circles', 'desc': '+2 Faith from Quarries'},
             {'name': 'Sun God', 'desc': '+1 Food for each Bananas, Citrus, and Wheat resource'},
             {'name': 'Tear of the Gods', 'desc': '+2 Faith for each Gems or Pearls resource'}]

# info on follower beliefs
follower_beliefs = [{'name': 'Ceremonial Burial', 'desc': '+1 Happiness for every City following this religion<br /> +1 Happiness for every 2 Cities following this religion'},
                    {'name': 'Church Property', 'desc': '+2 Gold for each City following this religion'},
                    {'name': 'Initiation Rites', 'desc': '+100 Gold when each City first converts to this religion'},
                    {'name': 'Interfaith Dialogue', 'desc': 'Gain Science when a Missionary spreads this religion to cities of other religions'},
                    {'name': 'Papal Primacy', 'desc': '+15 to Influence resting point with City-States following this religion'},
                    {'name': 'Peace Loving', 'desc': '+1 Happiness for every 8 followers of this religion in non-enemy foreign cities'},
                    {'name': 'Pilgrimage', 'desc': '+2 Faith for each foreign City following this religion'},
                    {'name': 'Tithe', 'desc': '+1 Gold for every 4 followers of this religion'},
                    {'name': 'World Church', 'desc': '+1 Culture for every 5 followers of this religion in other civilizations'}]

# info on founder beliefs
founder_beliefs = [{'name': 'Asceticism', 'desc': 'Shrines provide +1 Happiness in cities with 3 followers'},
                   {'name': 'Cathedrals', 'desc': 'Use Faith to purchase Cathedrals'},
                   {'name': 'Choral Music', 'desc': 'Temples provide +2 Culture in cities with 5 followers'},
                   {'name': 'Divine Inspiration', 'desc': 'Each World Wonder provides +2 Faith in city'},
                   {'name': 'Feed the World', 'desc': 'Shrines and Temples provide +1 Food each in city'},
                   {'name': 'Guruship', 'desc': '+2 Production if city has a Specialist'},
                   {'name': 'Holy Warriors', 'desc': 'Use Faith to purchase pre-Industrial land units'},
                   {'name': 'Liturgical Drama', 'desc': 'Amphitheaters provide +1 Faith in cities with 3 followers'},
                   {'name': 'Monasteries', 'desc': 'Use Faith to purchase Monasteries'},
                   {'name': 'Mosques', 'desc': 'Use Faith to purchase Mosques'},
                   {'name': 'Pagodas', 'desc': 'Use Faith to purchase Pagodas'},
                   {'name': 'Peace Gardens', 'desc': 'Gardens provide +2 Happiness in city'},
                   {'name': 'Religious Art', 'desc': 'Hermitage provides +8 Culture in city<br /> Hermitage provides +5 Culture and +5 Tourism'},
                   {'name': 'Religious Center', 'desc': 'Temples provide +2 Happiness in cities with 5 followers'},
                   {'name': 'Religious Community', 'desc': '+1% Production for each follower (Max +15%)'},
                   {'name': 'Swords into Plowshares', 'desc': '15% faster Growth rate for city if not at war'}]

# info on enhancer beliefs
enhancer_beliefs = [{'name': 'Defender of the Faith', 'desc': '+20% Combat Strength near friendly cities that follow this religion'},
                    {'name': 'Holy Order', 'desc': 'Missionaries and Inquisitors cost 30% less Faith'},
                    {'name': 'Itinerant Preachers', 'desc': 'Religion spreads to cities 30% further away'},
                    {'name': 'Just War', 'desc': '+20% Combat Strength near enemy cities that follow this religion'},
                    {'name': 'Messiah', 'desc': 'Prophets 25% stronger and earned with 25% less Faith'},
                    {'name': 'Missionary Zeal', 'desc': 'Missionary conversion strength +25%'},
                    {'name': 'Religious Texts', 'desc': 'Religion spreads 34% faster (68% with Printing Press)<br /> Religion spreads 25% faster (50% with Printing Press)'},
                    {'name': 'Religious Unity', 'desc': 'Religion spreads to friendly City-States at double rate'},
                    {'name': 'Reliquary', 'desc': 'Gain 50 Faith each time a Great Person is expended'}]

# info on early game policy trees
policy_trees = [{'name':'Liberty', 'desc':'Best for civilizations which desire rapid expansion. Adopting Liberty will provide 1 Culture in every city. Adopting all policies in the Liberty tree will grant a free Great Person of your choice near the Capital.'},
                {'name':'Tradition', 'desc':'Best for small empires. Adopting Tradition greatly increases the rate of border expansion in cities, grants 3 Culture in the Capital and unlocks building the Hanging Gardens wonder. Adopting all Policies in the Tradition tree will grant +15% Growth in all cities and a free Aqueduct in your first four cities. It also allows the purchase of Great Engineers with Faith starting in the Industrial Era.'},
                {'name':'Honor', 'desc':'Improves the effectiveness of one\'s army in a variety of ways. Adopting Honor gives a +33% combat bonus against Barbarians, and notifications will be provided when new Barbarian Encampments spawn in revealed territory. Gain Culture for the empire from each barbarian unit killed. Unlocks building the Statue of Zeus wonder. Adopting all policies in the Honor tree will grant Gold for each enemy unit killed. It also allows the purchase of Great Generals with Faith starting from the Industrial Era.'}]

# info on ideologies
ideologies = [{'name':'Order', 'desc':'Best for large, expansionist (but not necessarily aggressive) empires. Its tenets are primarily on a per-city basis and, as such, this Ideology encourages you to expand quickly even in the late game. Go grab all that unclaimed land and make a civilization that will stand the test of time!'},
              {'name':'Autocracy', 'desc':'Undeniably the best Ideology for aggressive, militaristic empires which seek a Domination Victory first. Its tenets allow you to maintain a large army, produce military units faster, conquer and pacify cities more easily, and even improve the fighting capabilities of your army. Its other tenets also appear aggressive in nature, so go forth and leave none left standing!'},
              {'name':'Freedom', 'desc':'Best for relatively small, peaceful empires, because it has a number of tenets that enhance the city population, the performance of Specialists (of all types), and also of Great People, including their tile improvements. It also has a good means of defense, making it the choice of civilizations which favor a defensive playstyle.'}]
