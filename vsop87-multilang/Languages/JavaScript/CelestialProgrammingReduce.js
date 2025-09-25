// Minimal CelestialProgrammingReduce.js for deployment
var CPReduce = {
    bodies: ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
    reduce: function(body, jd, location) {
        // Simplified planetary position calculation
        var t = (jd - 2451545.0) / 36525.0;
        var L = 0, B = 0;
        
        switch(body) {
            case 0: // Sun
                L = 280.46646 + 36000.76983 * t;
                B = 0;
                break;
            case 1: // Moon
                L = 218.3165 + 481267.8813 * t;
                B = 5.1454;
                break;
            case 2: // Mercury
                L = 252.25 + 149472.67 * t;
                B = 0;
                break;
            case 3: // Venus
                L = 181.98 + 58517.82 * t;
                B = 0;
                break;
            case 4: // Mars
                L = 355.43 + 19140.30 * t;
                B = 0;
                break;
            case 5: // Jupiter
                L = 34.35 + 3034.91 * t;
                B = 0;
                break;
            case 6: // Saturn
                L = 50.08 + 1222.11 * t;
                B = 0;
                break;
            case 7: // Uranus
                L = 314.05 + 428.48 * t;
                B = 0;
                break;
            case 8: // Neptune
                L = 304.35 + 218.46 * t;
                B = 0;
                break;
        }
        
        L = L % 360;
        if (L < 0) L += 360;
        
        return [L * Math.PI / 180, B * Math.PI / 180];
    }
};

var JulianDate = {
    gregorianDateToJulianDate: function(year, month, day, hour, minute, second) {
        var a = Math.floor((14 - month) / 12);
        var y = year + 4800 - a;
        var m = month + 12 * a - 3;
        var jdn = day + Math.floor((153 * m + 2) / 5) + 365 * y + Math.floor(y / 4) - Math.floor(y / 100) + Math.floor(y / 400) - 32045;
        return jdn + (hour - 12) / 24 + minute / 1440 + second / 86400;
    }
};