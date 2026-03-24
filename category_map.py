CATEGORY_MAP = {
    # Joogid
    'Energiajoogid': {'rimi': ['SH-3-4'], 'selver': ['54'], 'prisma': ['joogid/energia-ja-spordijoogid'], 'barbora': ['joogid/karastusjoogid/energiajoogid']},
    'Spordijoogid': {'rimi': ['SH-3-10'], 'selver': ['57'], 'prisma': ['joogid/energia-ja-spordijoogid']},
    'Karastusjoogid': {'rimi': ['SH-3-7'], 'selver': ['53'], 'prisma': ['joogid/karastusjoogid'], 'barbora': ['joogid/karastusjoogid/limonaadid']},
    'Maitsestamata vesi gaseerimata': {'rimi': ['SH-3-12-8'], 'selver': ['50'], 'prisma': ['joogid/vesi'], 'barbora': ['joogid/veed/gaseerimata-veed']},
    'Maitsestamata vesi gaseeritud': {'rimi': ['SH-3-12-9'], 'selver': ['50'], 'prisma': ['joogid/vesi'], 'barbora': ['joogid/veed/gaseeritud-veed']},
    'Maitsestatud vesi': {'rimi': ['SH-3-12-10', 'SH-3-12-11'], 'selver': ['50'], 'prisma': ['joogid/vesi']},
    'Jäätee': {'rimi': ['SH-3-5'], 'selver': ['51'], 'prisma': ['joogid/karastusjoogid']},
    'Mahlad': {'rimi': ['SH-12-20-1', 'SH-12-20-2', 'SH-12-20-3', 'SH-12-20-4', 'SH-12-20-5', 'SH-12-20-6', 'SH-12-20-7'], 'selver': ['51'], 'prisma': ['joogid/mahlad']},
    'Smuutid': {'rimi': ['SH-12-8-35'], 'selver': ['49'], 'prisma': ['joogid/mahlad']},
    'Kakao': {'rimi': ['SH-13-5'], 'selver': ['26'], 'prisma': ['joogid/kakao']},

    # Alkohol
    'Hele õlu': {'rimi': ['SH-1-6-1'], 'selver': ['30'], 'prisma': ['joogid/olled']},
    'Tume õlu': {'rimi': ['SH-1-6-2'], 'selver': ['30'], 'prisma': ['joogid/olled']},
    'Import õlu': {'rimi': ['SH-1-6-3'], 'selver': ['30'], 'prisma': ['joogid/olled']},
    'Alkoholivaba õlu': {'rimi': ['SH-3-1'], 'selver': ['55'], 'prisma': ['joogid/olled']},
    'Alkoholivaba siider': {'rimi': ['SH-3-2'], 'selver': ['55'], 'prisma': ['joogid/siidrid']},
    'Viin': {'rimi': ['SH-1-13'], 'selver': ['38'], 'prisma': ['joogid/kange-alkohol'], 'barbora': ['joogid/kange-alkohol/viinad']},
    'Rumm': {'rimi': ['SH-1-7'], 'selver': ['42'], 'prisma': ['joogid/kange-alkohol']},
    'Viski': {'rimi': ['SH-1-14'], 'selver': ['40'], 'prisma': ['joogid/kange-alkohol']},
    'Džinn': {'rimi': ['SH-1-2'], 'selver': ['39'], 'prisma': ['joogid/kange-alkohol']},
    'Liköör': {'rimi': ['SH-1-5'], 'selver': ['44'], 'prisma': ['joogid/kange-alkohol'], 'barbora': ['joogid/kange-alkohol/likoorid']},
    'Punane vein': {'rimi': ['SH-1-11-3'], 'selver': ['31'], 'prisma': ['joogid/veinid'], 'barbora': ['joogid/punased-ja-roosad-veinid/muud-punased-veinid', 'joogid/punased-ja-roosad-veinid/cabernet-sauvignon', 'joogid/punased-ja-roosad-veinid/gruusia-veinid']},
    'Valge vein': {'rimi': ['SH-1-11-6'], 'selver': ['32'], 'prisma': ['joogid/veinid'], 'barbora': ['joogid/valged-veinid/muud-valged-veinid', 'joogid/valged-veinid/chardonnay', 'joogid/valged-veinid/pinot-grigio', 'joogid/valged-veinid/riesling', 'joogid/valged-veinid/gruusia-veinid-valged']},
    'Roosa vein': {'rimi': ['SH-1-11-5'], 'selver': ['33'], 'prisma': ['joogid/veinid']},
    'Siider': {'rimi': ['SH-1-8'], 'selver': ['30'], 'prisma': ['joogid/siidrid']},
    'Tekiila': {'rimi': ['SH-1-9'], 'selver': ['45'], 'prisma': ['joogid/kange-alkohol']},

    # Piimatooted
    'Piim': {'rimi': ['SH-11-8-37'], 'selver': ['234'], 'prisma': ['piim-munad-ja-rasvad/piim-ja-hapupiim'], 'barbora': ['piimatooted-ja-munad/piimad/piimad']},
    'Jogurtid': {'rimi': ['SH-11-2-5', 'SH-11-2-8'], 'selver': ['236'], 'prisma': ['piim-munad-ja-rasvad/jogurtid']},
    'Joogijogurtid': {'rimi': ['SH-11-2-6'], 'selver': ['236'], 'prisma': ['piim-munad-ja-rasvad/jogurtid']},
    'Kohukesed': {'rimi': ['SH-11-2-7'], 'selver': ['237'], 'prisma': ['piim-munad-ja-rasvad/kohupiim-puding-ja-magustoit'], 'barbora': ['piimatooted-ja-munad/kohupiimatooted/kohukesed']},
    'Kohupiimad': {'rimi': ['SH-11-4-21'], 'selver': ['235'], 'prisma': ['piim-munad-ja-rasvad/kohupiim'], 'barbora': ['piimatooted-ja-munad/kohupiimatooted/kohupiimad']},
    'Kodujuustud': {'rimi': ['SH-11-4-20'], 'selver': ['235'], 'prisma': ['piim-munad-ja-rasvad/kohupiim']},
    'Või': {'rimi': ['SH-11-9-41'], 'selver': ['240'], 'prisma': ['piim-munad-ja-rasvad/rasvad']},
    'Margariinid': {'rimi': ['SH-11-9-40'], 'selver': ['240'], 'prisma': ['piim-munad-ja-rasvad/rasvad']},
    'Munad': {'rimi': ['SH-11-7-29'], 'selver': ['239'], 'prisma': ['piim-munad-ja-rasvad/munad']},

    # Juustud
    'Feta ja mozzarella': {'rimi': ['SH-11-3-10'], 'selver': ['245'], 'prisma': ['juustud/tuki-ja-viilujuustud']},
    'Määrdejuustud': {'rimi': ['SH-11-3-15'], 'selver': ['244'], 'prisma': ['juustud/toidu-ja-gurmeejuustud']},
    'Viilutatud juust': {'rimi': ['SH-11-3-17'], 'selver': ['243'], 'prisma': ['juustud/tuki-ja-viilujuustud']},

    # Liha
    'Värske kana, broiler': {'rimi': ['SH-8-9-25'], 'selver': ['220'], 'prisma': ['liha-ja-taimsed-valgud/broiler-ja-kalkun', 'liha-ja-taimsed-valgud/kana-broiler-ja-kalkun']},
    'Seahakkliha': {'rimi': ['SH-8-2-7'], 'selver': ['222'], 'prisma': ['liha-ja-taimsed-valgud/hakkliha']},
    'Seguhakkliha': {'rimi': ['SH-8-2-5'], 'selver': ['222'], 'prisma': ['liha-ja-taimsed-valgud/hakkliha']},
    'Veisehakkliha': {'rimi': ['SH-8-2-1'], 'selver': ['222'], 'prisma': ['liha-ja-taimsed-valgud/hakkliha']},
    'Kanahakkliha': {'rimi': ['SH-8-2-3'], 'selver': ['222'], 'prisma': ['liha-ja-taimsed-valgud/hakkliha']},
    'Värske sealiha': {'rimi': ['SH-8-14-25'], 'selver': ['219'], 'prisma': ['liha-ja-taimsed-valgud/sealiha']},
    'Veise-, lamba- ja ulukiliha': {'rimi': ['SH-8-21'], 'selver': ['221'], 'prisma': ['liha-ja-taimsed-valgud/veiseliha', 'liha-ja-taimsed-valgud/lambaliha-ja-ulukid']},
    'Grillvorstid': {'rimi': ['SH-8-1-25'], 'selver': ['226'], 'prisma': ['liha-ja-taimsed-valgud/vorstid-viinerid-ja-peekon'], 'barbora': ['liha-kala-valmistoit/lihatooted/grillvorstid']},
    'Verivorstid': {'rimi': ['SH-8-1-20'], 'selver': ['226'], 'prisma': ['liha-ja-taimsed-valgud/vorstid-viinerid-ja-peekon']},
    'Pool- ja täissuitsuvorstid': {'rimi': ['SH-8-13'], 'selver': ['223'], 'prisma': ['liha-ja-taimsed-valgud/singi-ja-vorstiloigud']},
    'Keeduvorstid': {'rimi': ['SH-8-4'], 'selver': ['223'], 'prisma': ['liha-ja-taimsed-valgud/vorstid-viinerid-ja-peekon'], 'barbora': ['liha-kala-valmistoit/lihatooted/keeduvorstid']},
    'Viinerid': {'rimi': ['SH-8-22'], 'selver': ['223'], 'prisma': ['liha-ja-taimsed-valgud/vorstid-viinerid-ja-peekon'], 'barbora': ['liha-kala-valmistoit/lihatooted/viinerid-ja-sardellid']},
    'Sink, peekon': {'rimi': ['SH-8-11-20'], 'selver': ['224'], 'prisma': ['liha-ja-taimsed-valgud/singi-ja-vorstiloigud'], 'barbora': ['liha-kala-valmistoit/lihatooted/sink-peekon-ja-rulaadid']},
    'Pasteet': {'rimi': ['SH-8-18'], 'selver': ['225'], 'prisma': ['liha-ja-taimsed-valgud/singi-ja-vorstiloigud']},

    # Kala
    'Konservis tuunikala': {'rimi': ['SH-8-5-8'], 'selver': ['231'], 'prisma': ['kala-ja-mereannid/muud-kalatooted']},
    'Konservis sprotid': {'rimi': ['SH-8-5-7'], 'selver': ['231'], 'prisma': ['kala-ja-mereannid/muud-kalatooted']},
    'Külmutatud kalatooted': {'rimi': ['SH-4-2-11'], 'selver': ['285'], 'prisma': ['kulmutatud-toidud/kulmutatud-liha-ja-kala'], 'barbora': ['kulmutatud-tooted/kulmutatud-liha-ja-kalatooted/kulmutatud-kalatooted']},

    # Leib ja pagar
    'Rukkileib': {'rimi': ['SH-6-3-15'], 'selver': ['248'], 'prisma': ['leivad-kupsised-ja-kupsetised/leivad'], 'barbora': ['leivad-saiad-kondiitritooted/leivad-ja-saiad/leivad']},
    'Peenleib': {'rimi': ['SH-6-3-14'], 'selver': ['248'], 'prisma': ['leivad-kupsised-ja-kupsetised/leivad']},
    'Röstsai': {'rimi': ['SH-6-7-21'], 'selver': ['249'], 'prisma': ['leivad-kupsised-ja-kupsetised/leivad'], 'barbora': ['leivad-saiad-kondiitritooted/leivad-ja-saiad/rostsaiad']},
    'Sai': {'rimi': ['SH-6-7-22'], 'selver': ['249'], 'prisma': ['leivad-kupsised-ja-kupsetised/kupsetusleti-tooted'], 'barbora': ['leivad-saiad-kondiitritooted/leivad-ja-saiad/saiad-ja-sepikud']},
    'Sepik': {'rimi': ['SH-6-8'], 'selver': ['250'], 'prisma': ['leivad-kupsised-ja-kupsetised/leivad']},
    'Saiakesed ja pirukad': {'rimi': ['SH-6-1-6'], 'selver': ['255'], 'prisma': ['leivad-kupsised-ja-kupsetised/kupsetised']},
    'Näkileivad': {'rimi': ['SH-6-4-10'], 'selver': ['251'], 'prisma': ['leivad-kupsised-ja-kupsetised/kuivikud-ja-nakileivad'], 'barbora': ['leivad-saiad-kondiitritooted/leivad-ja-saiad/nakileivad']},
    'Magusad küpsised': {'rimi': ['SH-9-5-5'], 'selver': ['275'], 'prisma': ['leivad-kupsised-ja-kupsetised/kupsised']},
    'Soolased küpsised': {'rimi': ['SH-9-5-6'], 'selver': ['275'], 'prisma': ['leivad-kupsised-ja-kupsetised/kupsised']},

    # Kuivained
    'Makaronid': {'rimi': ['SH-13-14-20', 'SH-13-14-87'], 'selver': ['11'], 'prisma': ['kuivtooted-ja-kupsetamine/riis-pasta-ja-nuudlid']},
    'Riis': {'rimi': ['SH-13-15-90', 'SH-13-15-91'], 'selver': ['13'], 'prisma': ['kuivtooted-ja-kupsetamine/riis-pasta-ja-nuudlid']},
    'Kaerahelbed': {'rimi': ['SH-13-2-9'], 'selver': ['15'], 'prisma': ['kuivtooted-ja-kupsetamine/helbed-krobinad-ja-muslid']},
    'Kruubid ja tangud': {'rimi': ['SH-13-18-100', 'SH-13-18-102', 'SH-13-18-103'], 'selver': ['12'], 'prisma': ['kuivtooted-ja-kupsetamine/riis-pasta-ja-nuudlid']},
    'Nisujahu': {'rimi': ['SH-13-4-21'], 'selver': ['10'], 'prisma': ['kuivtooted-ja-kupsetamine/jahud-ja-kupsetussegud']},
    'Suhkur': {'rimi': ['SH-13-13-85'], 'selver': ['263'], 'prisma': ['kuivtooted-ja-kupsetamine/suhkur-magusained-ja-mesi']},

    # Kohv ja tee
    'Jahvatatud kohv': {'rimi': ['SH-13-9-44'], 'selver': ['24'], 'prisma': ['joogid/kohv-ja-kohvifiltrid'], 'barbora': ['joogid/kohv-tee-kakao/jahvatatud-kohvid']},
    'Lahustuv kohv': {'rimi': ['SH-13-9-47'], 'selver': ['24'], 'prisma': ['joogid/kohv-ja-kohvifiltrid']},
    'Must tee': {'rimi': ['SH-13-17-95'], 'selver': ['25'], 'prisma': ['joogid/tee']},
    'Roheline tee': {'rimi': ['SH-13-17-97'], 'selver': ['25'], 'prisma': ['joogid/tee']},
    'Puuviljatee': {'rimi': ['SH-13-17-96'], 'selver': ['374'], 'prisma': ['joogid/tee']},
    'Taimetee': {'rimi': ['SH-13-17-98'], 'selver': ['374'], 'prisma': ['joogid/tee']},

    # Kastmed ja õlid
    'Majonees': {'rimi': ['SH-11-6-27'], 'selver': ['268'], 'prisma': ['olid-vurtsid-maitseained/majonees', 'olid-vurtsid-maitseained/salatikastmed']},
    'Sinep': {'rimi': ['SH-13-6-30'], 'selver': ['268'], 'prisma': ['olid-vurtsid-maitseained/ketsupid-ja-sinepid']},
    'Tomatiketšup': {'rimi': ['SH-13-6-32'], 'selver': ['269'], 'prisma': ['olid-vurtsid-maitseained/ketsupid-ja-sinepid']},
    'Tomatikastmed': {'rimi': ['SH-13-6-31'], 'selver': ['269'], 'prisma': ['olid-vurtsid-maitseained/maitsekastmed-ja-pastad']},
    'Päevalilleõli': {'rimi': ['SH-13-19-110'], 'selver': ['267'], 'prisma': ['olid-vurtsid-maitseained/olid']},
    'Rapsiõli': {'rimi': ['SH-13-19-111'], 'selver': ['267'], 'prisma': ['olid-vurtsid-maitseained/olid']},

    # Maiustused ja snäkid
    'Piimašokolaad': {'rimi': ['SH-9-9-20'], 'selver': ['283'], 'prisma': ['maiustused-ja-suupisted/sokolaadid'], 'barbora': ['kauasailivad-toidukaubad/sokolaadid/piimasokolaadid']},
    'Tume šokolaad': {'rimi': ['SH-9-9-22'], 'selver': ['283'], 'prisma': ['maiustused-ja-suupisted/sokolaadid']},
    'Šokolaadibatoonid': {'rimi': ['SH-9-9-21'], 'selver': ['283'], 'prisma': ['maiustused-ja-suupisted/sokolaadid'], 'barbora': ['kauasailivad-toidukaubad/sokolaadid/sokolaadibatoonid']},
    'Kartulikrõpsud': {'rimi': ['SH-9-8-15'], 'selver': ['278'], 'prisma': ['maiustused-ja-suupisted/kropsud-ja-muud-naksid']},
    'Kummikommid': {'rimi': ['SH-9-3-2'], 'selver': ['272'], 'prisma': ['maiustused-ja-suupisted/kommikotid'], 'barbora': ['kauasailivad-toidukaubad/kommid-ja-maiustused/kummikommid-ja-natsukommid']},
    'Pastillid': {'rimi': ['SH-9-7'], 'selver': ['273'], 'prisma': ['maiustused-ja-suupisted/pastillid'], 'barbora': ['kauasailivad-toidukaubad/kommid-ja-maiustused/natsud-ja-pastillid']},
    'Närimiskumm': {'rimi': ['SH-9-3-5'], 'selver': ['273'], 'prisma': ['maiustused-ja-suupisted/narimiskummid']},
    'Pähklid': {'rimi': ['SH-9-4-10'], 'selver': ['277'], 'prisma': ['kuivtooted-ja-kupsetamine/seemned-pahklid-ja-kuivatatud-puuviljad']},

    # Jäätised
    'Pulgajäätised': {'rimi': ['SH-4-1-9'], 'selver': ['289'], 'prisma': ['kulmutatud-toidud/jaatised'], 'barbora': ['kulmutatud-tooted/jaatised-ja-jaakuubikud/pulgajaatised']},
    'Koonusjäätised': {'rimi': ['SH-4-1-4'], 'selver': ['289'], 'prisma': ['kulmutatud-toidud/jaatised'], 'barbora': ['kulmutatud-tooted/jaatised-ja-jaakuubikud/topsi-ja-koonusjaatised']},
    'Perejäätised': {'rimi': ['SH-4-1-8'], 'selver': ['289'], 'prisma': ['kulmutatud-toidud/jaatised'], 'barbora': ['kulmutatud-tooted/jaatised-ja-jaakuubikud/perejaatised']},

    # Külmutatud
    'Külmutatud lihatooted': {'rimi': ['SH-4-4'], 'selver': ['286'], 'prisma': ['kulmutatud-toidud/kulmutatud-liha-ja-kala'], 'barbora': ['kulmutatud-tooted/kulmutatud-liha-ja-kalatooted/kulmutatud-lihatooted']},
    'Külmutatud köögiviljad': {'rimi': ['SH-4-3-14'], 'selver': ['287'], 'prisma': ['kulmutatud-toidud/kulmutatud-koogiviljad'], 'barbora': ['kulmutatud-tooted/kulmutatud-koogiviljad-seened-ja-marjad/kulmutatud-koogiviljad-ja-seened']},
    'Külmutatud pitsa': {'rimi': ['SH-4-5-19'], 'selver': ['286'], 'prisma': ['kulmutatud-toidud/kulmutatud-pitsad']},
    'Külmutatud leivatooted': {'rimi': ['SH-4-6-21'], 'selver': ['288'], 'prisma': ['kulmutatud-toidud/kulmutatud-kupsetised-ja-leivad'], 'barbora': ['kulmutatud-tooted/kulmutatud-kondiitritooted/kulmutatud-leivad-ja-saiad']},
    'Külmutatud tainad': {'rimi': ['SH-4-6-24'], 'selver': ['288'], 'prisma': ['kulmutatud-toidud/kulmutatud-kupsetised-ja-leivad'], 'barbora': ['kulmutatud-tooted/kulmutatud-kondiitritooted/kulmutatud-taignad']},
    'Pelmeenid': {'rimi': ['SH-4-7-25'], 'selver': ['286'], 'prisma': ['kulmutatud-toidud/kulmutatud-eined'], 'barbora': ['kulmutatud-tooted/kulmutatud-pooltooted/kulmutatud-pelmeenid-ja-vareenikud']},

    # Köögiviljad
    'Köögiviljad': {
        'rimi': ['SH-12-1-1', 'SH-12-1-2', 'SH-12-1-3', 'SH-12-1-4', 'SH-12-1-5',
                 'SH-12-1-6', 'SH-12-1-26', 'SH-12-2-7', 'SH-12-2-8', 'SH-12-2-9',
                 'SH-12-2-10', 'SH-12-2-11', 'SH-12-2-12', 'SH-12-2-13', 'SH-12-2-14'],
        'selver': ['213'],
        'prisma': ['puu-ja-koogiviljad/juurviljad', 'puu-ja-koogiviljad/koogiviljad'],
        'barbora': ['koogiviljad-puuviljad/koogiviljad-ja-aedviljad/kartulid-porgandid-ja-kapsad',
                    'koogiviljad-puuviljad/koogiviljad-ja-aedviljad/paprikad-ja-baklazaanid',
                    'koogiviljad-puuviljad/koogiviljad-ja-aedviljad/peedid-ja-muud-juurviljad',
                    'koogiviljad-puuviljad/koogiviljad-ja-aedviljad/tomatid-ja-kurgid'],
    },
    'Seened': {'rimi': ['SH-12-7'], 'selver': ['214'], 'prisma': ['puu-ja-koogiviljad/seened'], 'barbora': ['koogiviljad-puuviljad/seened/varsked-seened']},
    'Õun ja pirn': {'rimi': ['SH-12-5-27'], 'selver': ['210'], 'prisma': ['puu-ja-koogiviljad/puuviljad'], 'barbora': ['koogiviljad-puuviljad/puuviljad-ja-marjad/ounad-ja-pirnid']},
    'Marjad': {'rimi': ['SH-12-4-19', 'SH-12-4-22', 'SH-12-4-23'], 'selver': ['217'], 'prisma': ['puu-ja-koogiviljad/marjad'], 'barbora': ['koogiviljad-puuviljad/puuviljad-ja-marjad/viinamarjad-ja-marjad']},

    # Hügieen ja kosmeetika
    'Tualettpaber': {'rimi': ['SH-10-26'], 'selver': ['103'], 'prisma': ['kodu-ja-majapidamistarbed/majapidamispaberid']},
    'Majapidamispaber': {'rimi': ['SH-10-10-51'], 'selver': ['102'], 'prisma': ['kodu-ja-majapidamistarbed/majapidamispaberid']},
    'Salvrätikud': {'rimi': ['SH-10-4-8'], 'selver': ['104'], 'prisma': ['kodu-ja-majapidamistarbed/majapidamispaberid']},
    'Šampoonid': {'rimi': ['SH-2-5-32'], 'selver': ['78'], 'prisma': ['kosmeetika-ja-hugieen/juuksed-ja-juuksehooldus']},
    'Palsamid': {'rimi': ['SH-2-5-29'], 'selver': ['78'], 'prisma': ['kosmeetika-ja-hugieen/juuksed-ja-juuksehooldus']},
    'Dušigeelid': {'rimi': ['SH-2-6-33'], 'selver': ['83'], 'prisma': ['kosmeetika-ja-hugieen/seebid-ja-pesuvahendid']},
    'Dušigeelid meestele': {'rimi': ['SH-2-6-35'], 'selver': ['83'], 'prisma': ['kosmeetika-ja-hugieen/seebid-ja-pesuvahendid']},
    'Hambaharjad': {'rimi': ['SH-2-11-66'], 'selver': ['70'], 'prisma': ['kosmeetika-ja-hugieen/suuhooldus'], 'barbora': ['enesehooldustooted/suuhugieen/hambaharjad']},
    'Hambapastad': {'rimi': ['SH-2-11-68'], 'selver': ['69'], 'prisma': ['kosmeetika-ja-hugieen/suuhooldus']},
    'Näokreemid': {'rimi': ['SH-2-9-53'], 'selver': ['72'], 'prisma': ['kosmeetika-ja-hugieen/naohooldus'], 'barbora': ['enesehooldustooted/naohooldustooted/naokreemid']},
    'Näopuhastus': {'rimi': ['SH-2-9-55'], 'selver': ['73'], 'prisma': ['kosmeetika-ja-hugieen/naohooldus'], 'barbora': ['enesehooldustooted/naohooldustooted/naopuhastus']},
    'Kehakreemid': {'rimi': ['SH-2-6-38'], 'selver': ['84'], 'prisma': ['kosmeetika-ja-hugieen/nahahooldus'], 'barbora': ['enesehooldustooted/kehahooldustooted/kehakreemid-kehaolid']},
    'Hügieenisidemed': {'rimi': ['SH-2-4-18'], 'selver': ['91'], 'prisma': ['kosmeetika-ja-hugieen/intiimhugieen-ja-intiimtooted'], 'barbora': ['enesehooldustooted/intiimhugieeni-vahendid/hugieenisidemed']},
    'Tampoonid': {'rimi': ['SH-2-4-23'], 'selver': ['91'], 'prisma': ['kosmeetika-ja-hugieen/intiimhugieen-ja-intiimtooted']},
    'Patareid': {'rimi': ['SH-10-15-72'], 'selver': ['122'], 'prisma': ['kodumasinad-ja-elektroonika/lambid-patareid-ja-taskulambid'], 'barbora': ['kodukaubad-ja-vaba-aeg/koduelektroonika/patareid']},

    # Kodukeemia
    'Nõudepesuvahendid käsipesu': {'rimi': ['SH-10-12-57'], 'selver': ['108'], 'prisma': ['kodu-ja-majapidamistarbed/noudepesu']},
    'Pesugeelid': {'rimi': ['SH-10-14-62'], 'selver': ['114'], 'prisma': ['kodu-ja-majapidamistarbed/riiete-pesemine', 'kodu-ja-vaba-aeg/pesupesemine'], 'barbora': ['puhastustarbed-ja-lemmikloomatooted/pesupesemisvahendid/pesugeelid']},
    'Pesuloputusvahend': {'rimi': ['SH-10-14-61'], 'selver': ['114'], 'prisma': ['kodu-ja-majapidamistarbed/riiete-pesemine'], 'barbora': ['puhastustarbed-ja-lemmikloomatooted/pesupesemisvahendid/pesuloputusvahendid']},
    'Üldpuhastusvahendid': {'rimi': ['SH-10-18-81-1'], 'selver': ['110'], 'prisma': ['kodu-ja-majapidamistarbed/koristus-ja-puhastusained', 'kodu-ja-vaba-aeg/kodupuhastusvahendid'], 'barbora': ['puhastustarbed-ja-lemmikloomatooted/kodukeemia/uldpuhastusvahendid']},
    'Tualeti puhastusvahendid': {'rimi': ['SH-10-18-80-1'], 'selver': ['110'], 'prisma': ['kodu-ja-majapidamistarbed/koristus-ja-puhastusained'], 'barbora': ['puhastustarbed-ja-lemmikloomatooted/kodukeemia/wc-poti-puhastusvahendid']},
    'Põranda puhastusvahendid': {'rimi': ['SH-10-18-79'], 'selver': ['110'], 'prisma': ['kodu-ja-majapidamistarbed/koristus-ja-puhastusained']},
    'Prügikotid': {'rimi': ['SH-10-16'], 'selver': ['112'], 'prisma': ['kodu-ja-majapidamistarbed/majapidamisplast']},

    # Lemmikloomad
    'Kassi konservid': {'rimi': ['SH-7-1-1'], 'selver': ['315'], 'prisma': ['lemmikloomad/kassitoit'], 'barbora': ['puhastustarbed-ja-lemmikloomatooted/lemmikloomakaubad/kasside-konservid-ja-eined']},
    'Kuiv kassitoit': {'rimi': ['SH-7-1-3'], 'selver': ['315'], 'prisma': ['lemmikloomad/kassitoit']},
    'Koera konservid': {'rimi': ['SH-7-2-4'], 'selver': ['316'], 'prisma': ['lemmikloomad/koeratoit']},
    'Kuiv koeratoit': {'rimi': ['SH-7-2-6'], 'selver': ['316'], 'prisma': ['lemmikloomad/koeratoit']},
    'Kassiliiv': {'rimi': ['SH-7-3-7'], 'selver': ['319'], 'prisma': ['lemmikloomad/kassiliiv'], 'barbora': ['puhastustarbed-ja-lemmikloomatooted/lemmikloomakaubad/lemmiklooma-allapanu']},
}