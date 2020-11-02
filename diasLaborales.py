from dateutil import rrule
import datetime


def diasLaborales(fechaInicio, fechaFin, festivos=0, vacaciones=None):
    if vacaciones is None:
        vacaciones= 5, 6         # si no tienes vacaciones no trabajas sab y dom
    laborales = [dia for dia in range(7) if dia not in vacaciones]
    totalDias= rrule.rrule(rrule.DAILY, dtstart=fechaInicio, until=fechaFin,byweekday=laborales)
    return totalDias.count() - festivos
