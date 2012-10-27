-=#Portfolioprojektet#=-

Anton Lindgren (antli117)
Yakup Yildiz (yakyi744)

------------------------------------------------------------------------------------------

Installationsanvisningar:

1. öppna terminal och skriv följande:

   git clone https://github.com/yakyil89/wtflashTDP003 portfolio

   (en mapp kommer startas där du står i terminalen med namn portfolio)

2. navigera till portfoliomappen genom att skriva:

   cd portfolio

3. starta servern genom att skriva följande när du befinner dig i portfoliomappen:

   python server.py

4. öppna valfri webbläsare och skriv i url-fältet:

   127.0.0.1:5000

------------------------------------------------------------------------------------------

Systempaketering:

static/images/ - här ligger alla bilder på hemsidan.
static/style/style.css - hemsidans stilmall.
templates/ - innehåller alla HTML-sidor.
data.json - innehåller information om projekten.
data.py - innehåller funktioner för att styra hemsidan.
log.log - här lagras information om alla anrop på sidan.
server.py - servermodulen som sköter sidanrop.

------------------------------------------------------------------------------------------

För att göra ändringar:

Öppna data.json i portfoliomappen

I denna fil representeras ett projekt av en dictionary (innehållet mellan { och }).
För varje projekt finns en uppsättning nycklar med ett varsitt tilldelat värde,
"nyckel": värde, ändra värdet för att göra ändringar i projektet.

För att lägga till ett projekt, kopiera ett existerande projekt, {abc}, och klistra in
efter sista existerande projekt (komma måste finnas mellan alla projekt). Därefter är det
bara att ändra värdena i det nya projektblocket.

"start_date" - projektets startdatum
"short_description" - kort beskrivning av projektet
"course_name" - kursnamn
"long_description" - lång beskrivning av projektet
"group_size" - antal gruppmedlemmar
"academic_credits" - antal högskolepoäng
"small_image" - namn på lilla bilden (med filnamnstilläg)
"techniques_used" - lista med använda tekniker
"project_name" - projektets namn
"course_id" - kurskod
"end_date" - slutdatum
"project_no" - projekt-id (måste vara ett heltal och unikt från alla andra projekt-id)
"big_image" - namn på stora bilden (med filnamnstilläg)

för att lägga till eller ändra bilder kan detta göras i portfolio/static/images.
(De små bilderna ska helst ha en maximal bredd av 150 pixlar och de stora 610 pixlar).

------------------------------------------------------------------------------------------

Länk till loggbok:

http://antli1.blogspot.se/