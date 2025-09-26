AstroFixxer — Open-Source Star-Hopping Tracker + “AstroGuide” Voice Assistant

Smart India Hackathon 2025 – Student Innovation (Space Technology)
Problem Statements: SIH25142, SIH25125

A lightweight, phone-mounted star-hopping assistant that turns any telescope into a guided instrument. AstroFixxer is a web app (PWA) you can install on your phone, align on a bright object, and then “hop” to faint targets with precise Alt/Az deltas—augmented by an optional multilingual voice assistant (AstroGuide) for real-time explanations of sky events.

1) About our problem statement

Access barrier: Automated star-tracking mounts (GoTo/plate-solving rigs) are expensive, complex, and out of reach for most students and hobbyists in India.

What’s needed: A low-cost, phone-first solution that works offline, guides a manual telescope accurately, and teaches astronomy on the fly—ideal for schools, clubs, and first-time observers.

Why now (market signal): India had ~659 million smartphone users in 2025—an enormous base that can support phone-mounted astronomy tools. Meanwhile, leading stargazing apps like Stellarium Mobile show 10M+ installs globally, underscoring demand for handheld sky-navigation tools. 


2) Our solution (methodology & working)

AstroFixxer adapts the proven AstroHopper approach to deliver accurate star hopping with commodity smartphone sensors—no camera plate solving required.

How it works (field workflow):

Mount the phone to the telescope with the screen parallel to the tube (not a camera AR view).

Align once on a bright star/planet near your target. The app records the current pointing using the phone’s gyroscope + gravity sensors (and compass when available).

Pick a target (by tapping or searching). The app computes ∆Alt / ∆Az to nudge the telescope toward the object.

Follow the deltas until they reach ≈0 — you’re on target. Re-align as needed since phone gyros drift over time.

(Optional) AstroGuide answers “What’s up now?” and explains events (e.g., conjunctions, ISS passes) in plain language.

Under the hood:

Ephemerides: Planets and solar-system bodies from VSOP87 tables. 


Deep-sky: Object IDs/positions from OpenNGC (NGC/IC). 


Constellations: Line art and metadata from the Western Constellations Atlas dataset. 


Progressive Web App: Offline cache; runs as a single HTML/JS page. (Approach documented in AstroHopper.) 

AstroFixxer is ideal for manual Dobsonians and small refractors where a cheap, robust “digital setting circles” experience is transformative. 


3) Our technology stack

Languages: HTML, CSS, JavaScript (vanilla, client-rendered)

Runtime: Browser/PWA (Service Worker, Web Manifest)

Sensors & Web APIs: DeviceOrientation (gyro, gravity), Geolocation

Astronomy data:

OpenNGC (NGC/IC positions & metadata) — CC-BY-SA-4.0. 
GitHub

VSOP87 (planet ephemerides; multilang JS tables). 
GitHub
+1

Western Constellations Atlas of Space (constellation lines). 
GitHub

App architecture: Single-page web app; offline-first; no server required for core use

Hosting/CI: Vercel (static deploy)

Planned add-ons:

AstroGuide (Rasa Open Source) for multilingual voice queries & function-calling to app APIs

3D-printed phone mount kit and alignment jig

4) Market feasibility

Open source core, paid hardware add-on. We will keep AstroFixxer free & open with extensive docs and lesson plans. Revenue comes from 3D-printed kits (phone mount, balancing ring, finder bracket) and optional classroom packs.

Demand proxies:

India’s smartphone base (~659M users in 2025) provides a massive reachable audience for phone-mounted astronomy utilities. 


Leading mobile planetariums demonstrate multi-million installs (e.g., Stellarium Mobile 10M+ on Google Play), indicating strong hobbyist interest. 


Global reports project steady growth for astrophotography gear markets, implying rising amateur participation (directional indicator; source: industry research). 


⚠️ Note on Indian counts: Hard numbers for “how many Indians do astronomy/astrophotography” are not officially tracked. We therefore use conservative proxies (smartphone reach, app installs, equipment market growth) to justify feasibility. Where possible, we will augment with primary metrics (downloads by region, school/club adoption, kit sales).

5) Impact & benefits

Education at scale: Brings practical sky-navigation to schools & clubs without buying GoTo mounts.

Inclusion: Works offline, supports multilingual voice (planned), and runs on low-cost Android devices.

Skill building: Teaches celestial coordinate systems, star hopping, and observing technique—not just “tap to GoTo.”

Community: Open data and open code encourage contributions, localizations, and new observing lists tailored to India’s skies.

Sustainability: Simple phone mount + manual scopes extends the life of existing equipment rather than replacing it.

Quick start

Open the deployed app: https://astro-fixxer.vercel.app/astrofixxer.html

Tap Install (PWA) in your browser to add it to your home screen.

Grant location and motion sensor access (required for alignment).

Align on a bright object, select a target, and follow the Alt/Az deltas to zero.

iOS tip: since iOS 13, motion sensors require a user gesture to enable; if you see “No Gyro”, tap the on-screen button to grant access. (Behavior documented in the AstroHopper readme.) 


Roadmap

 Rasa-powered AstroGuide (Hindi/English first)

 In-app “What’s up tonight?” events feed (conjunctions, ISS passes, meteor showers)

 Guided school lesson plans & printable worksheets

 3D-printed kit: STL files + BOM + vendor links

 Accessibility: high-contrast mode, screen-reader hints

Citations & credits

We stand on the shoulders of excellent open-source work:

AstroHopper by Artyom Beilis — core method (“digital setting circles” via smartphone gyroscope/gravity) and PWA architecture. Licensed GPL-3.0.

GitHub: https://github.com/artyom-beilis/skyhopper

App page: https://artyom-beilis.github.io/astrohopper.html


OpenNGC — NGC/IC database (CC-BY-SA-4.0) by Mattia Verga, built from NED, HyperLEDA, SIMBAD, HEASARC, etc.

https://github.com/mattiaverga/OpenNGC


VSOP87-multilang — planetary ephemerides tables/code by Greg Miller and contributors.

https://github.com/gmiller123456/vsop87-multilang


Western Constellations Atlas of Space — constellations line data & workflow by Eleanor Lutz.

https://github.com/eleanorlutz/western_constellations_atlas_of_space


Market/context sources referenced above:

India smartphone users ~659M (June 18, 2025). 
Exploding Topics

Stellarium Mobile Google Play listing (10M+ downloads). 
Google Play

Global/India astrophotography camera market signals (industry research). 
Dataintelo
+1

License

Please note that upstream AstroHopper is GPL-3.0 and certain datasets carry their own licenses (e.g., OpenNGC CC-BY-SA-4.0). If you redistribute modified bundles, ensure your distribution respects the original licenses. 

Contributing

Issues and PRs are welcome—especially for localizations, observing lists tailored to India, and classroom materials.