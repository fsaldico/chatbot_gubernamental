# actions/actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# Ejemplo de acción para consultar el saldo SUBE integrando con una base de datos o API
class ActionConsultarSaldoSUBE(Action):
    def name(self) -> Text:
        return "action_consultar_saldo_sube"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # En un entorno real, aquí conectarías a la base de datos gubernamental de SUBE
        # numero_tarjeta = tracker.get_slot('numero_tarjeta')  # Si se solicitara
        # saldo = conector_bd_sube.consultar_saldo(numero_tarjeta)

        # Para el prototipo, simulamos una respuesta
        saldo_simulado = 450.75
        dispatcher.utter_message(text=f"Tu saldo SUBe es de ${saldo_simulado}.")

        return []

# Ejemplo de acción para solicitar un turno integrando con el sistema de turnos
class ActionSolicitarTurno(Action):
    def name(self) -> Text:
        return "action_solicitar_turno"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tipo_tramite = tracker.get_slot('tipo_tramite')

        # Simulamos la integración con el sistema de turnos
        # nuevo_turno = conector_sistema_turnos.crear_turno(tipo_tramite, tracker.sender_id)
        numero_turno_simulado = "B-284"

        dispatcher.utter_message(
            text=f"Listo. He agendado tu turno para {tipo_tramite}. Tu número de turno es {numero_turno_simulado}. Recibirás un recordatorio por SMS."
        )

        return [SlotSet("numero_turno", numero_turno_simulado)]

# Ejemplo de acción para reportar un problema
class ActionInformarProblemaCalle(Action):
    def name(self) -> Text:
        return "action_informar_problema_calle"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tipo_problema = tracker.get_slot('tipo_problema')
        ubicacion = tracker.get_slot('ubicacion')

        # Simulamos la creación de un reporte en el sistema de gestión
        # id_reporte = conector_sistema_reclamos.crear_reporte(tipo_problema, ubicacion)
        id_reporte_simulado = "RC-20241002-956"

        dispatcher.utter_message(
            text=f"Gracias por el reporte. Hemos creado una orden para atender el {tipo_problema} en {ubicacion}. Tu número de seguimiento es {id_reporte_simulado}."
        )

        return []