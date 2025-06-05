// GeoJSON data for crime locations in India
const indiaGeoJson = {
    "type": "FeatureCollection",
    "features": [
        // Mumbai
        {
            "type": "Feature",
            "properties": {
                "city": "Mumbai",
                "type": "Theft",
                "severity": "High",
                "description": "Mobile phone theft at railway station"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [72.8777, 19.0760]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Mumbai",
                "type": "Assault",
                "severity": "Medium",
                "description": "Confrontation at market"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [72.8866, 19.0834]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Mumbai",
                "type": "Robbery",
                "severity": "High",
                "description": "Armed robbery at jewelry store"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [72.8644, 19.0554]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Mumbai",
                "type": "Vehicle Theft",
                "severity": "Medium",
                "description": "Two-wheeler stolen from parking lot"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [72.8557, 19.0685]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Mumbai",
                "type": "Burglary",
                "severity": "Medium",
                "description": "House break-in reported in residential area"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [72.8693, 19.0822]
            }
        },
        
        // Delhi
        {
            "type": "Feature",
            "properties": {
                "city": "Delhi",
                "type": "Theft",
                "severity": "Medium",
                "description": "Pickpocketing incident in busy market"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [77.2090, 28.6139]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Delhi",
                "type": "Assault",
                "severity": "High",
                "description": "Physical altercation in public space"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [77.2100, 28.6235]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Delhi",
                "type": "Robbery",
                "severity": "High",
                "description": "Street robbery at night"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [77.2295, 28.6129]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Delhi",
                "type": "Vehicle Theft",
                "severity": "Low",
                "description": "Car stolen from shopping mall"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [77.2200, 28.6050]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Delhi",
                "type": "Burglary",
                "severity": "Medium",
                "description": "Apartment break-in during daytime"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [77.2180, 28.6333]
            }
        },
        
        // Bangalore
        {
            "type": "Feature",
            "properties": {
                "city": "Bangalore",
                "type": "Theft",
                "severity": "Low",
                "description": "Laptop theft from coffee shop"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [77.5946, 12.9716]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Bangalore",
                "type": "Assault",
                "severity": "Medium",
                "description": "Dispute escalated to violence"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [77.6066, 12.9666]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Bangalore",
                "type": "Robbery",
                "severity": "Medium",
                "description": "Mugging near tech park"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [77.6040, 12.9865]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Bangalore",
                "type": "Vehicle Theft",
                "severity": "Low",
                "description": "Motorcycle stolen overnight"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [77.5900, 12.9550]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Bangalore",
                "type": "Burglary",
                "severity": "High",
                "description": "Office break-in with equipment stolen"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [77.6030, 12.9780]
            }
        },
        
        // Chennai
        {
            "type": "Feature",
            "properties": {
                "city": "Chennai",
                "type": "Theft",
                "severity": "Medium",
                "description": "Phone snatching incident"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [80.2707, 13.0827]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Chennai",
                "type": "Assault",
                "severity": "Low",
                "description": "Minor altercation reported"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [80.2800, 13.0900]
            }
        },
        
        // Kolkata
        {
            "type": "Feature",
            "properties": {
                "city": "Kolkata",
                "type": "Robbery",
                "severity": "High",
                "description": "Armed robbery at store"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [88.3639, 22.5726]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Kolkata",
                "type": "Vehicle Theft",
                "severity": "Medium",
                "description": "Car stolen from residential area"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [88.3700, 22.5800]
            }
        },
        
        // Hyderabad
        {
            "type": "Feature",
            "properties": {
                "city": "Hyderabad",
                "type": "Burglary",
                "severity": "Medium",
                "description": "Home invasion during night"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [78.4867, 17.3850]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Hyderabad",
                "type": "Theft",
                "severity": "Low",
                "description": "Wallet stolen in crowded area"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [78.4900, 17.3900]
            }
        },
        
        // Pune
        {
            "type": "Feature",
            "properties": {
                "city": "Pune",
                "type": "Assault",
                "severity": "Medium",
                "description": "Assault reported near college campus"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [73.8567, 18.5204]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Pune",
                "type": "Vehicle Theft",
                "severity": "Low",
                "description": "Scooter theft from parking"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [73.8600, 18.5300]
            }
        },
        
        // Ahmedabad
        {
            "type": "Feature",
            "properties": {
                "city": "Ahmedabad",
                "type": "Burglary",
                "severity": "High",
                "description": "Shop break-in with significant loss"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [72.5714, 23.0225]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Ahmedabad",
                "type": "Robbery",
                "severity": "Medium",
                "description": "Purse snatching in market area"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [72.5800, 23.0300]
            }
        },
        
        // Lucknow
        {
            "type": "Feature",
            "properties": {
                "city": "Lucknow",
                "type": "Theft",
                "severity": "Low",
                "description": "Minor theft at local shop"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [80.9462, 26.8467]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Lucknow",
                "type": "Assault",
                "severity": "Medium",
                "description": "Physical confrontation reported"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [80.9500, 26.8500]
            }
        },
        
        // Jaipur
        {
            "type": "Feature",
            "properties": {
                "city": "Jaipur",
                "type": "Robbery",
                "severity": "Medium",
                "description": "Tourist robbed near monument"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [75.7873, 26.9124]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "city": "Jaipur",
                "type": "Burglary",
                "severity": "High",
                "description": "Hotel room burglary reported"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [75.7900, 26.9200]
            }
        }
    ]
}; 