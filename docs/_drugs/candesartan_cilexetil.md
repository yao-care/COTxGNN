---
layout: default
title: Candesartan Cilexetil
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 5
---

# Candesartan Cilexetil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Con la guía del pipeline cargada, procedo a generar el informe completo a partir del Evidence Pack.

---

# Candesartan Cilexetil: De Hipertensión Arterial a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Candesartan cilexetil es un bloqueador del receptor de angiotensina tipo 1 (ARB), ampliamente reconocido para el tratamiento de la hipertensión arterial y la insuficiencia cardíaca congestiva.
El modelo TxGNN predice que podría ser efectivo para la **Hipertensión Renovascular Maligna**, con una base mecanística directamente plausible dado su modo de acción sobre el eje renina-angiotensina.
Sin embargo, **no se encontraron ensayos clínicos ni publicaciones específicas** que respalden el uso de candesartan en esta indicación concreta, y existen advertencias de seguridad críticas que deben evaluarse antes de cualquier avance.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial / Insuficiencia cardíaca (clase ARB; sin registro activo en Colombia) |
| Nueva Indicación Predicha | Hipertensión Renovascular Maligna |
| Puntaje de Predicción TxGNN | 99.68% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia suministrado. Con base en la farmacología conocida de la clase terapéutica, candesartan cilexetil es un antagonista selectivo del receptor AT1 de angiotensina II. Al bloquear este receptor, inhibe la vasoconstricción mediada por angiotensina II, la retención de sodio y la estimulación simpática, reduciendo así la presión arterial sistémica y la carga renal.

La hipertensión renovascular maligna tiene como mecanismo fisiopatológico central la estenosis de la arteria renal → isquemia renal → liberación masiva de renina → elevación aguda de angiotensina II → vasoconstricción sistémica y renal intensa mediada por AT1. Esta cadena de eventos hace que el bloqueo del receptor AT1 por candesartan sea **directamente relevante a nivel mecanístico**. Otros ARBs de la misma clase (losartán, irbesartán) ya cuentan con evidencia de uso en hipertensión renovascular general, lo que respalda la plausibilidad de esta predicción.

No obstante, la variante **"maligna"** de la hipertensión renovascular es frecuentemente una emergencia hipertensiva con daño orgánico agudo (retinopatía, lesión renal aguda), y exige una advertencia crítica: la estenosis bilateral de arterias renales o la estenosis de arteria renal en riñón único constituyen **contraindicaciones absolutas** para los ARBs en general, incluyendo candesartan. Su uso en estos contextos puede precipitar un deterioro renal agudo severo e irreversible. La ausencia de datos clínicos específicos para candesartan en esta indicación impide avanzar más allá del estadio de hipótesis mecanística.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Candesartan cilexetil **no cuenta con registros sanitarios activos en Colombia (INVIMA)**. El estado de mercado es "no comercializado" y no se identificaron licencias aprobadas en la consulta realizada. Cualquier uso clínico futuro requeriría tramitar el registro sanitario correspondiente ante el INVIMA.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Advertencia crítica derivada del análisis mecanístico:** Los ARBs, incluyendo candesartan, están contraindicados en pacientes con estenosis bilateral de arterias renales o estenosis de arteria renal en riñón único — condiciones frecuentes en el contexto de hipertensión renovascular maligna. El uso en esta población puede desencadenar deterioro agudo de la función renal. Se requiere evaluación anatómica vascular (ej. angiografía o eco-Doppler renal) antes de considerar cualquier ARB en este escenario.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque la base mecanística de candesartan como antagonista AT1 es farmacológicamente plausible para la hipertensión renovascular maligna, la ausencia total de ensayos clínicos específicos y de literatura directa, combinada con contraindicaciones de seguridad críticas en esta población (estenosis arterial renal bilateral), hace que el perfil riesgo-beneficio sea actualmente incierto. La recomendación es mantener en estado de "pregunta de investigación" hasta obtener evidencia clínica robusta.

**Para avanzar se necesita:**
- Obtener datos completos del mecanismo de acción (MOA) desde DrugBank y la ficha técnica oficial
- Revisar advertencias y contraindicaciones del prospecto (actualmente en Data Gap)
- Identificar y analizar estudios observacionales o series de casos con ARBs (clase) en hipertensión renovascular maligna que puedan extrapolarse
- Diseñar protocolo de estudio piloto con criterios de inclusión/exclusión estrictos (excluir estenosis bilateral de arteria renal)
- Evaluar viabilidad de registro sanitario en Colombia (INVIMA) para esta indicación
- Consultar con nefrólogos y especialistas en hipertensión para validar la hipótesis clínica antes de inversión en investigación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

