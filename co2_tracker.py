import streamlit as st
import tiktoken

enc = tiktoken.get_encoding("o200k_base")

# Raum zur Vorab-Definition von Zahlen als Rechengrundlage
co2_input = 0.0003
co2_output = 0.19
# Werte nach Andersen et al. 2026

toothbrush = 30 # Verbauch in mg für 2min elektrische Zahnbürste
one_min_phonecall = 100 # Verbrauch in mg für eine Minute Handy-Telefonie
dishwasher = 500000 # Verbrauch in mg für eine 5kg Ladung im Standard-Programm 40°
bus_meter = 37 # Verbrauch in mg für einen Meter mit dem Bus

st.header("CO2-Tracker für GenKI")

st.caption("Tom Weidensdorfer (tom.weidensdorfer@tu-dresden.de)  \n*Team Digitale Lehre des Bereichs Geistes- und Sozialwissenschaften der Technischen Universität Dresden*")

st.write("Dieses Tool dient dazu, ein Gefühl dafür zu vermitteln, wie viel CO2 die Verwendung von generativer künstlicher Intelligenz verbraucht. Dafür können eigene Prompts, die auf ChatGPT und Co. eingegeben wurden, inklusive des generierten Outputs hier eingegeben werden. Das Tool rechnet automatisch den Verbrauch aus und rechnet diesen anschließend in alltägliche Beispiele um.")

st.divider()

st.subheader("User-Input")
st.text_area("Kopiere hier deinen Original-Prompt hinein.", value="", key="user_input")

st.subheader("Output")
st.text_area("Kopiere hier den kompletten Output hinein, den du von der verwendeten GenKI ausgegeben bekommen hast.", value="", key="ai_output")

tokens_input = enc.encode(st.session_state["user_input"])
tokens_output = enc.encode(st.session_state["ai_output"])

verbrauch_input = len(tokens_input) * co2_input
verbrauch_output = len(tokens_output) * co2_output
verbrauch_gesamt = verbrauch_input + verbrauch_output

st.divider()

st.subheader("CO2-Verbrauch")

a, b = st.columns(2, border=True)

a.write("**Input:**")
a.metric(label="Anzahl Tokens", value=len(tokens_input))
a.metric(label="CO2-Verbrauch", value=(str(round(verbrauch_input, 5)) + "mg CO2"))
b.write("**Output:**")
b.metric(label="Anzahl Tokens", value=len(tokens_output))
b.metric(label="CO2-Verbrauch", value=(str(round(verbrauch_output, 5)) + "mg CO2"))

st.metric(label="CO2-Verbrauch insgesamt", value=(str(round(verbrauch_gesamt, 5)) + "mg CO2"), border=True)

st.space(size="xxsmall")

st.write("**Das entspricht:**")
st.write("🪥", str(round((verbrauch_gesamt/toothbrush)/2*60, 2)), "Sekunden eine elektrische Zahnbürste laufen lassen.")
st.write("📞", str(round((verbrauch_gesamt/one_min_phonecall)*60, 2)), "Sekunden mit dem Handy telefonieren.")
st.write("🚌", str(round(verbrauch_gesamt/bus_meter, 2)), "Meter mit dem Bus fahren.")

if verbrauch_gesamt >= 10000:
    st.write("🫧", str(round(verbrauch_gesamt/dishwasher, 5)), "mal 5 kg Wäsche waschen.")

st.divider()

st.subheader("Quellen und Literaturhinweise")
st.markdown(
    "- **Andersen**, Lisa Bondo / **Herklotz**, Markus / **Liu**, Ailin / **Goeke**, Moritz / **Juelich**, Michael / **Kern**, Christoph & **Kreuter**, Frauke (2026). \"From Awareness to Action? The Impact of CO2 Emission Feedback on Student LLM Usage\". In: *Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems (CHI EA \'26), April 13-17, 2026, Bacelona, Spain.* New York, NY, USA: ACM. DOI: 10.1145/3772363.3798840.  \n"
    "- **Jalilov**, Orkhan & **Weidensdorfer**, Tom (2025). *Einsatz generativer KI-Systeme im Unterricht*. Zenodo. DOI: 10.5281/zenodo.18242615.  \n"
    "- **Kurpicz-Briki**, Mascha (2024). *Mehr als ein Chatbot: Die Entmystifizierung der Sprachmodelle*. Cham: Springer Nature Switzerland. DOI: 10.1007/978-3-031-58545-6.  \n"
    "- **Luttrell**, Regina & **Bowman**, Nicholas David (Hrsg.) (2026). *Provoking Generative AI Futures: Merging Theory and Praxis*. Oxford: Routledge. DOI: 10.4324/9781003487623.  \n"
)

st.divider()

st.caption("Dieses Tool dient der Veranschaulichung im Rahmen von Sensibilisierungskursen zu *AI Literacy für die Geisteswissenschaften*. Es ist **nicht** als wissenschaftlich zitierbare Quelle geeignet und sollte mit Skepsis behandelt werden. Für Feedback, Literaturempfehlungen und andere Verbesserungsvorschläge bin ich dankbar.", text_alignment="justify")