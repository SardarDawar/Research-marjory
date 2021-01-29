from common.models import Setting

TEXT_ENG__NOTIF_REPLICA_UNAVAILABLE = "Currently unavailable."
TEXT_ENG__NOTIF_ALREADY_PARTICIPATED = "You have already participated in this study."
TEXT_ENG__NOTIF_PARTICIPATION_ENDED = "Your participation in this study has ended."
TEXT_ENG__NOTIF_PARTICIPATION_INCOMPLETE = "Your participation was not completed."
TEXT_ENG__NOTIF_FAILED_LOAD_SCRIPT = "Failed to load."
TEXT_ENG__NOTIF_FAILED_LOAD_STEP = "Failed to load step."

TEXT_POR__NOTIF_REPLICA_UNAVAILABLE = "Indisponível no momento."
TEXT_POR__NOTIF_ALREADY_PARTICIPATED = "Você já participou deste estudo."
TEXT_POR__NOTIF_PARTICIPATION_ENDED = "Sua participação neste estudo está completada."
TEXT_POR__NOTIF_PARTICIPATION_INCOMPLETE = "Sua participação não foi completada."
TEXT_POR__NOTIF_FAILED_LOAD_SCRIPT = "Falha na carga."
TEXT_POR__NOTIF_FAILED_LOAD_STEP = "Falha em carregar um passo."


NOTIF_REPLICA_UNAVAILABLE =         1
NOTIF_ALREADY_PARTICIPATED =        2
NOTIF_PARTICIPATION_ENDED =         3
NOTIF_PARTICIPATION_INCOMPLETE =    4
NOTIF_FAILED_LOAD_SCRIPT =          5
NOTIF_FAILED_LOAD_STEP =            6


NOTIFICATIONS_POR = {
    NOTIF_REPLICA_UNAVAILABLE : TEXT_POR__NOTIF_REPLICA_UNAVAILABLE,
    NOTIF_ALREADY_PARTICIPATED : TEXT_POR__NOTIF_ALREADY_PARTICIPATED,
    NOTIF_PARTICIPATION_ENDED : TEXT_POR__NOTIF_PARTICIPATION_ENDED,
    NOTIF_PARTICIPATION_INCOMPLETE : TEXT_POR__NOTIF_PARTICIPATION_INCOMPLETE,
    NOTIF_FAILED_LOAD_SCRIPT : TEXT_POR__NOTIF_FAILED_LOAD_SCRIPT,
    NOTIF_FAILED_LOAD_STEP : TEXT_POR__NOTIF_FAILED_LOAD_STEP,
}

NOTIFICATIONS_ENG = {
    NOTIF_REPLICA_UNAVAILABLE : TEXT_ENG__NOTIF_REPLICA_UNAVAILABLE,
    NOTIF_ALREADY_PARTICIPATED : TEXT_ENG__NOTIF_ALREADY_PARTICIPATED,
    NOTIF_PARTICIPATION_ENDED : TEXT_ENG__NOTIF_PARTICIPATION_ENDED,
    NOTIF_PARTICIPATION_INCOMPLETE : TEXT_ENG__NOTIF_PARTICIPATION_INCOMPLETE,
    NOTIF_FAILED_LOAD_SCRIPT : TEXT_ENG__NOTIF_FAILED_LOAD_SCRIPT,
    NOTIF_FAILED_LOAD_STEP : TEXT_ENG__NOTIF_FAILED_LOAD_STEP,
}

def getNotificationText(notif_id, lang):
    if lang == Setting.LANG_POR:
        return NOTIFICATIONS_POR[notif_id]
    else:
        return NOTIFICATIONS_ENG[notif_id]