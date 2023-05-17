import streamlit as st

from prompts.baseline_prompt import generate_baseline_prompt
from prompts.block_prompts import prompt1, prompt2, prompt3

st.markdown("# Peer Plan Prompt Engineer")
st.markdown('---')
st.write('')
st.write('')
st.write('')

st.markdown('**Bitte beantworte die folgenden Fragen mit den Inhalten aus dem BLockbuster Storyskript:**')

A = st.text_input('Beschreibe Deinen idealen Kunden, den Du jemals hattest und von dem Du gerne mehr hättest - in allen Einzelheiten… z. B. Alter, Geschlecht, Lebensstil, Beruf, Familie, Hobbys, haben sie einen bestimmten Namen, den sie benutzen? usw.')

B = st.text_input('Das größte Ergebnis, zu dem ich einem Unternehmen oder einer Person helfen kann, ist? Was wünscht sich Dein idealer Kunde mehr als alles andere?')

C = st.text_input('Was sind die großen Ziele meines Kunden? Was sind seine Träume und Wünsche für die Zukunft?')

D = st.text_input('Was ist das größte Problem, das Dein idealer Kunde hat? Was sind die Top 3 Dinge, die deinen perfekten Kunden täglich frustrieren (sind es Dinge, die sie nicht tun wollen? Menschen? Umstände? Aufgaben?)?')

E = st.text_input('Was frustriert Deinen idealen Kunden am meisten? Was hält Deinen idealen Kunden nachts wach (beunruhigt, ängstlich, besorgt)?')

F = st.text_input('Was demütigt Deinen perfekten Kunden (ein Ereignis oder eine Begebenheit, die er zu vermeiden versucht)?')

G = st.text_input('Wer bist du, was machst du und wem hilfst du genau?')

H = st.text_input('Welche Werte schätzen meine Kunden in einer Geschäftsbeziehung? Was schätzen sie an meiner Arbeit am meisten?')

I = st.text_input('Was sind einige Deiner größten Errungenschaften, Auszeichnungen oder Besonderheiten? (Anzahl der Kunden, denen du geholfen hast, Auszeichnungen, die du erhalten hast, Erwähnung in großen Publikationen usw.)')

J = st.text_input('Was sind die 3-5 Dinge, die deine Kunden tun müssen, um ihr Problem zu lösen oder ihr gewünschtes Ergebnis zu erreichen? Was ist die EINZIGARTIGE Methode, die dein Angebot von anderen unterscheidet? Warum ist es besser? Warum ist es anders als das, was der Kunde bereits in der Vergangenheit ausprobiert hat?')

K = st.text_input('Was sind die wichtigsten Schritte, die mein Kunde unternehmen muss? Was sind die häufigsten Hindernisse und wie kann ich meinem Kunden helfen, diese zu überwinden?')

L = st.text_input('Bietest du eine No-Risk-Garantie an? (Wenn ja, beschreibe diese in maximal ein bis zwei Sätzen)')

M = st.text_input('Was bietest du in deiner Ad an, um deinen idealen Kunden zu helfen? (Gratis-Training, kostenloses Erstgespräch etc.) Was bekommen sie, wenn sie auf deine Ad klicken? Was sind die echten Vorteile deines Angebots?')

N = st.text_input('Wie hoch sind die Kosten, wenn sie dort bleiben, wo sie jetzt sind? Wie schlimm kann es werden, wenn sie es nicht in Ordnung bringen? Was ist der Preis, wenn sie NICHT handeln und bleiben, wo sie sind? (finanziell, emotional, zeitlich, usw.)')

O = st.text_input('Was wäre das ideale Ergebnis für meinen Kunden, wenn alles nach Plan läuft? Wie würde sich das auf ihr Leben auswirken?')

P = st.text_input('Warum sollten deine idealen Kunden dein Angebot jetzt beanspruchen und nicht abwarten? Was ist der Preis, wenn sie NICHT handeln und bleiben, wo sie sind?')

st.write('')
st.write('')

st.markdown('**Bitte jetzt noch Angaben zur Zielkundensprache machen!**')
tonality = st.text_input('Wie drückt deine Zielgruppe sich aus? Welche Wörter verwendet sie? Bitte alle Merkmale hier hinzufügen.')


st.write('')
st.write('')
st.write('')

generate_prompts= st.button("Prompts erstellen")

if generate_prompts:
    
      
    promptI = generate_baseline_prompt(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, prompt1)
    promptII = generate_baseline_prompt(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, prompt2)
    promptIII = generate_baseline_prompt(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, prompt3)
        
        
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header("Prompt 1")
        st.code(promptI)
        
    with col2:
        st.header("Prompt 2")
        st.code(promptII)
        
    with col3:
        st.header("Prompt 3")
        st.code(promptIII)
    
    