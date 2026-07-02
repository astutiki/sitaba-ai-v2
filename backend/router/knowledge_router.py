"""
Knowledge Router
Menghubungkan pertanyaan pengguna ke knowledge base AI SINTA.
"""

from knowledge.disaster_impact import jawab_dampak_bencana
from knowledge.disaster_potential import jawab_potensi_bencana
from knowledge.mitigation import jawab_mitigasi
from knowledge.preparedness import jawab_kesiapsiagaan
from knowledge.evacuation import jawab_evakuasi
from knowledge.emergency_contact import jawab_kontak_darurat
from knowledge.first_aid import jawab_pertolongan_pertama
from knowledge.public_information import jawab_informasi_publik
from knowledge.faq import jawab_faq


def proses_knowledge(pertanyaan: str, intent: str):

    if intent == "DISASTER_IMPACT":
        return jawab_dampak_bencana(pertanyaan)

    if intent == "DISASTER_POTENTIAL":
        return jawab_potensi_bencana(pertanyaan)

    if intent == "MITIGATION":
        return jawab_mitigasi(pertanyaan)

    if intent == "PREPAREDNESS":
        return jawab_kesiapsiagaan(pertanyaan)

    if intent == "EVACUATION":
        return jawab_evakuasi(pertanyaan)

    if intent == "EMERGENCY_CONTACT":
        return jawab_kontak_darurat(pertanyaan)

    if intent == "FIRST_AID":
        return jawab_pertolongan_pertama(pertanyaan)

    if intent == "PUBLIC_INFORMATION":
        return jawab_informasi_publik(pertanyaan)

    if intent == "FAQ":
        return jawab_faq(pertanyaan)

    return None