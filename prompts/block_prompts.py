prompt1 = """
<Start>

Block 1: Die Überschrift und Call-to-Action
Beschreibung: Der Held muss in 10 Sekunden erkennen, was der Mentor anbietet, welchen Nutzen es hat und was der Held als Nächstes tun sollte. Verdichte deine Kommunikation zu einer Hauptbotschaft  - verpackt in eine spannende Geschichte.
Die Headline ist **fettgedruckt** und maximal prägnant - also kurz**.** Die Headline ist 1 bis maximal 2 Sätze lang und muss den Leser maximal fesseln. Die Headline besteht aus der Call-to-Action und hebt den Mehrwert für den Nutzer hervor. Schreibe danach 2-5 Sätze für die Subheadline in normaler Schriftart.

Fasse zuletzt die Headline und Subheadline in 3 bullett points übersichtlich zusammen.

Verwende diese Informationen: [M] - Call-to-Action

Block 2: Logobar
Beschreibung: Füge hier [testimonials / logos] hinzu

Block 3: Das Problem des Helden

Beschreibung: Starte mit einer Headline. Die Headline fasst in 1-2 Sätzen zusammen, wer der Held ist, was sein Problem ist, und wie der Mentor das Problem löst. 
Die Headline ist **fettgedruckt** und maximal prägnant - also kurz.
Beschreibe danach kurz den Charakter des Helden, sein äußeres Problem und den Mentor-Plan.
Zuletzt kommt eine Auflistung. In der Auflistung ist der Titel jeweils ein Äußeres Problem des Kunden, und darunter ein kurzer Text dazu, wie der Mentor Plan das Problem löst.
Das Format sieht so aus:
**Äußeres Problem 1:** Beschreibung wie der Mentorplan das Problem löst

**Äußeres Problem 2:** Beschreibung wie der Mentorplan das Problem löst

usw.
Verwende so viele Elemente in der Liste wie es sinnvolle äußere Probleme des Kunden gibt.
Maximal aber 5.
Verwende diese Informationen: [A] - Charakter, [D] - Äußeres Problem, [J] Mentor-Plan

Block 4: Traum

Beschreibung: Beschreibe den Traum des Helden mit einer Headline. Die Headline fasst in 1-2 Sätzen zusammen, was der Traum des Helden ist.
Die Headline ist **fettgedruckt** und maximal prägnant - also kurz
Schreibe danach einen kurzen Text und beschreibe den Traum des Helden näher in 3-5 Sätzen.
Fasse zuletzt die Träume des Helden in 3 bullett points übersichtlich zusammen.
Verwende diese Informationen: [C] - Traum

<Ende>

Die Struktur der Landing-Page ist also:

Block 1: [M] 

Block 2: -

Block 3: [A], [D], [J] 

Block 4: [C]

"""

prompt2 = """
<Start>

Block 5: Das Innere Problem

Beschreibung: Starte mit einer Headline die in 1-2 Sätzen zusammenfasst, was das innere Problem des Helden ist. Die Headline ist ************************fettgedruckt************************ und maximal prägnant - also kurz
Schreibe danach einen kurzen Text und beschreibe den Traum des Helden näher in 3-5 Sätzen.
Fasse zuletzt die inneren Probleme des Helden in 3 bullett points übersichtlich zusammen. Beginne die Bullett-Point Liste mit einer kurzen Einführung wie zum Beispiel: “Kennen Sie das auch?” 
Verwende diese Informationen: [E] - Inneres-Problem

Block 6: Freundschaft

Beschreibung: Starte mit einer Headline die in 1-2 Sätzen zusammenfasst, was der Held und der Mentor gemeinsam haben; beschreibe ihre Freundschaft. Die Headline ist ************************fettgedruckt************************ und maximal prägnant - also kurz
Schreibe danach einen kurzen Text und beschreibe die Freundschaft / die Gemeinsamkeiten von Held und Mentor näher in 3-5 Sätzen.
Fasse zuletzt die Freundschaft des Helden in 2-3 bullett points übersichtlich zusammen.
Verwende diese Informationen: [H] - Freundschaft

Block 7: Prozess-Plan

Beschreibung: Starte mit einer Headline die in 1-2 Sätzen zusammenfasst, wie der Prozess-Plan des Mentors aussieht und wie dieser die Probleme des Helden löst. 
Die Headline ist **fettgedruckt** und maximal prägnant - also kurz
Schreibe danach einen kurzen Text und beschreibe den Prozessplan konkret in 3-5 Sätzen.
Fasse zuletzt den Prozessplan zusammen. Verwende dafür eine Auflistung, die in einer Liste gegliedert ist, mit dem Titel für jeden Unterpunkt: 

**Schritt 1: …
Schritt 2: …**

Für jeden der Schritte fasst du noch in 1-3 Sätzen die wichtigsten Aspekte dieses Schrittes zusammen.
Verwende diese Informationen: [K] - Prozess-Plan

Block 8: Kompetenz

Beschreibung: Starte mit einer Headline die in 1-2 Sätzen zusammenfasst, was die einzigartige Kompetenz des Mentors ausmacht.
Die Headline ist **fettgedruckt** und maximal prägnant - also kurz
Schreibe danach einen kurzen Text und fasse die Kompetenz des Mentors in 3-5 Sätzen zusammen.
Fasse zuletzt die Kompetenz übersichtlich in 3-5 bullett points zusammen.

Verwende diese Informationen: [I] - Kompetenz

<Ende>

Die Struktur der Landing-Page ist also:

Block 5: [E] 

Block 6: [H]

Block 7: [K]

Block 8: [I]
"""

prompt3= """
<Start>

Block 9: Paradies / Transformation

Beschreibung: Starte mit einer Headline die in 1-2 Sätzen zusammenfasst, welches Paradies / welche Transformation der Held erlebt wenn er mit dem Mentor zusammenarbeitet.
Die Headline ist **fettgedruckt**.
Schreibe danach einen kurzen Text und beschreibe das Paradies und die Transformation näher in 3-5 Sätzen.
Fasse zuletzt das Paradies und die Transformation übersichtlich in 3-5 bullett points zusammen.

Verwende diese Informationen: [O] - Paradies/Transformation

Block 10: Call - To - Action

Beschreibung: Schreibe eine **Headline in fettgedruckter Schriftart.** 
Die Headline ist 1 bis maximal 2 Sätze lang und muss den Leser maximal fesseln. Die Headline besteht aus der Call-to-Action und hebt den Mehrwert für den Nutzer hervor. Schreibe danach 1-3 Sätze für die Subheadline in normaler Schriftart.

Verwende diese Informationen: [M] - Call-to-Action

Block 11: Verlust-Drama

Beschreibung: Starte mit einer Headline die in 1-2 Sätzen zusammenfasst, was dem helden wiederfährt, wenn er nicht mit dem Mentor zusammenarbeitet.
Die Headline ist **fettgedruckt**.
Schreibe danach einen kurzen Text und beschreibe das Verlust-Drama und die Konsequenzen näher in 3-5 Sätzen.
Fasse zuletzt das Verlust-Drama übersichtlich in 3-5 bullett points zusammen.

Leite die Auflistung mit einer kurzen Einleitung ein, mit einer kurzen Frage oder einem Satz der inhaltlich auf die Liste vorbereitet.

Verwende diese Informationen: [N] - Verlust-Drama

Block 12: Sicherheits-Plan

Beschreibung: Starte mit einer Headline die in 1-2 Sätzen zusammenfasst, wie der Held abgesichert ist, wenn er mit dem Mentor zusammenarbeitet.
Die Headline ist **fettgedruckt**.
Schreibe danach einen kurzen Text und beschreibe den Sicherheitsplan näher in 3-5 Sätzen.
Fasse zuletzt das Sicherheitsplan übersichtlich in 3-5 bullett points zusammen.

Verwende diese Informationen: [L] - Sicherheitsplan

<Ende>
"""