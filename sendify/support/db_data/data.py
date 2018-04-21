PRODUCTS_DATA = {
                    '1':
                        {
                            'product_type': 'letter',
                            "def_weight": 0.1,
                            "def_width": 1,
                            "def_height": 1,
                            "def_length": 1

                        },
                    '2':
                        {
                            'product_type': 'package',
                            "def_weight": 5,
                            "def_width": 5,
                            "def_height": 5,
                            "def_length": 5

                        },
                    '3':
                        {

                            'product_type': 'pallet',
                            "def_weight": 20,
                            "def_width": 20,
                            "def_height": 20,
                            "def_length": 20

                        },
                }

EXPECTED_TIME_DATA = {
                    '1':
                        {
                            "origin_city": "Stockholm",
                            "destination_city": "Kiev",
                            "transit_time": "20 hours",
                            "carrier_id": 1,
                            "distance": 1200

                        },
                    '2':
                        {
                            "origin_city": "Stockholm",
                            "destination_city": "Krakow",
                            "transit_time": "21 hours",
                            "carrier_id": 1,
                            "distance": 1000

                        },
                    '3':
                        {
                            "origin_city": "Kiev",
                            "destination_city": "Stockholm",
                            "transit_time": "20 hours",
                            "carrier_id": 1,
                            "distance": 1200

                        },
                    '4':
                        {
                            "origin_city": "Krakow",
                            "destination_city": "Stockholm",
                            "transit_time": "21 hours",
                            "carrier_id": 1,
                            "distance": 1000

                        },
                    '5':
                        {
                            "origin_city": "Stockholm",
                            "destination_city": "Kiev",
                            "transit_time": "30 hours",
                            "carrier_id": 2,
                            "distance": 1200

                        },
                    '6':
                        {
                            "origin_city": "Stockholm",
                            "destination_city": "Krakow",
                            "transit_time": "31 hours",
                            "carrier_id": 2,
                            "distance": 1000

                        },
                    '7':
                        {
                            "origin_city": "Kiev",
                            "destination_city": "Stockholm",
                            "transit_time": "30 hours",
                            "carrier_id": 2,
                            "distance": 1200

                        },
                    '8':
                        {
                            "origin_city": "Krakow",
                            "destination_city": "Stockholm",
                            "transit_time": "31 hours",
                            "carrier_id": 2,
                            "distance": 1000

                        },
                    '9':
                        {
                            "origin_city": "Stockholm",
                            "destination_city": "Kiev",
                            "transit_time": "40 hours",
                            "carrier_id": 3,
                            "distance": 1200

                        },
                    '10':
                        {
                            "origin_city": "Stockholm",
                            "destination_city": "Krakow",
                            "transit_time": "41 hours",
                            "carrier_id": 3,
                            "distance": 1000

                        },
                    '11':
                        {
                            "origin_city": "Kiev",
                            "destination_city": "Stockholm",
                            "transit_time": "40 hours",
                            "carrier_id": 3,
                            "distance": 1200

                        },
                    '12':
                        {
                            "origin_city": "Krakow",
                            "destination_city": "Stockholm",
                            "transit_time": "41 hours",
                            "carrier_id": 3,
                            "distance": 1000

                        },

                }


CARRIERS_DATA = {
    '1':
        {
            'carrier_name': 'DHL Express',
            'price_per_km': 40,
            'price_per_kg': 40
        },

    '2':
        {
            'carrier_name': 'FedEx Corporation',
            'price_per_km': 20,
            'price_per_kg': 20
        },

    '3':
        {
            'carrier_name': 'Royal Mail',
            'price_per_km': 10,
            'price_per_kg': 10
        }
}

