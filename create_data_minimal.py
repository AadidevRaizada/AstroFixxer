#!/usr/bin/env python3
# Minimal data generator that doesn't require submodules

def create_minimal_jsdb():
    """Create minimal jsdb.js with essential astronomical objects"""
    
    # Essential stars and objects for basic functionality
    stars_data = [
        # Bright stars
        {"RA": 101.287, "DE": -16.716, "AM": -1.46, "name": "Sirius", "t": "S"},
        {"RA": 88.793, "DE": 7.407, "AM": 0.13, "name": "Rigel", "t": "S"},
        {"RA": 79.172, "DE": 45.998, "AM": 0.08, "name": "Capella", "t": "S"},
        {"RA": 95.988, "DE": 9.647, "AM": 0.50, "name": "Betelgeuse", "t": "S"},
        {"RA": 213.915, "DE": 19.182, "AM": -0.04, "name": "Arcturus", "t": "S"},
        {"RA": 279.234, "DE": 38.784, "AM": 0.03, "name": "Vega", "t": "S"},
        {"RA": 310.358, "DE": 45.280, "AM": 0.77, "name": "Deneb", "t": "S"},
        {"RA": 37.955, "DE": 89.264, "AM": 1.98, "name": "Polaris", "t": "S"},
        
        # Messier objects
        {"RA": 56.75, "DE": 24.117, "AM": 1.6, "name": "M45", "t": "Oc", "s": 110},
        {"RA": 83.633, "DE": 22.514, "AM": 3.4, "name": "M42", "t": "Ne", "s": 85},
        {"RA": 10.685, "DE": 41.269, "AM": 3.4, "name": "M31", "t": "Ga", "s": 190},
        
        # Constellations
        {"RA": 83.633, "DE": 22.514, "name": "Orion", "t": "Ca", "AM": -1},
        {"RA": 201.298, "DE": -11.161, "name": "Virgo", "t": "Ca", "AM": -1},
        {"RA": 202.761, "DE": 47.042, "name": "Ursa Major", "t": "Ca", "AM": -1},
        
        # Planets (positions will be calculated dynamically)
        {"RA": 0, "DE": 0, "AM": -1, "name": "Mercury", "t": "P"},
        {"RA": 0, "DE": 0, "AM": -1, "name": "Venus", "t": "P"},
        {"RA": 0, "DE": 0, "AM": -1, "name": "Mars", "t": "P"},
        {"RA": 0, "DE": 0, "AM": -1, "name": "Jupiter", "t": "P"},
        {"RA": 0, "DE": 0, "AM": -1, "name": "Saturn", "t": "P"},
        {"RA": 0, "DE": 0, "AM": -1, "name": "Moon", "t": "P"}
    ]
    
    # Create index
    index = {"S": 0, "Oc": 0, "Ne": 0, "Ga": 0, "Ca": 0, "P": 0, "U": len(stars_data)}
    
    # Create name index
    names = []
    name_indices = []
    for i, obj in enumerate(stars_data):
        if "name" in obj:
            names.append(obj["name"].upper())
            name_indices.append(i)
    
    name_index = {"names": names, "index": name_indices}
    
    # Generate JavaScript
    js_content = f"""//Generated minimal database for AstroFixxer
// types: 'S' - star,'Ca' - constellation,  'Oc' - open cluster, 'Gc' = globular cluster, 'Ga' - galaxy, 'Ne' - nebula, 'P' - Planet
var allstars_index = {index};
var allstars = {stars_data};
var constellation_lines = [];
var allstars_index_name = {name_index};
var allstars_db_specs = {{"items": {len(stars_data)}, "index_size": {len(index)}, "index_name_size": {len(names)}}};
"""
    
    with open('jsdb.js', 'w') as f:
        f.write(js_content)
    
    print("Created minimal jsdb.js with essential astronomical objects")

if __name__ == "__main__":
    create_minimal_jsdb()