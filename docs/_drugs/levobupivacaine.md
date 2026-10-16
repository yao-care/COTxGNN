---
layout: default
title: Levobupivacaine
parent: Solo Predicción del Modelo (L5)
nav_order: 396
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Levobupivacaine: nueva indicación predicha, Gastroduodenitis (nivel de evidencia L5). Indicación original: Bupivacaína"
---

# Levobupivacaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Levobupivacaína: De Bupivacaína (anestésico local) a Gastroduodenitis

## Resumen en Una Frase

La levobupivacaína es un anestésico local de acción prolongada; en Colombia su único registro sanitario (BUPINEST® 0.75 % solución inyectable) figura con la indicación "bupivacaína" y se encuentra cancelado.
El modelo TxGNN predice que podría ser efectiva para **gastroduodenitis**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: la predicción se apoya solo en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Bupivacaína (anestésico local, según el registro INVIMA) |
| Nueva Indicación Predicha | Gastroduodenitis |
| Puntaje de Predicción TxGNN | 99.09% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general (no proveniente de los datos), la levobupivacaína es un anestésico local de tipo amida y de acción prolongada que bloquea los canales de sodio dependientes de voltaje, impidiendo la conducción del impulso nervioso.

Un vínculo plausible, pero no verificado, sería una acción analgésica o antinociceptiva local sobre las fibras aferentes viscerales de la mucosa gastroduodenal. También se han descrito efectos antiinflamatorios de los anestésicos locales, pero no hay datos que los relacionen con la gastroduodenitis.

Existe además una barrera probable de vía de administración: la levobupivacaína se usa normalmente por infiltración, epidural o bloqueo nervioso, y no está establecida su administración tópica o sistémica al tracto digestivo superior. El puntaje alto podría reflejar similitud en el grafo con otros anestésicos locales o bloqueadores de canales de sodio, y no una relación terapéutica real. La compatibilidad de vías de administración está pendiente de evaluar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19902579 | BUPINEST® 0.75 % SIMPLE INYECTABLE | Solución inyectable | Bupivacaína | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no provienen del prospecto): enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, miastenia gravis (incluida la de inicio en adultos), enfermedad de la unión neuromuscular, deficiencia de butirilcolinesterasa, enfermedad cardiovascular y cardiopatía.
- **Interacciones Farmacológicas**: se identificaron 62 interacciones en total. Entre las listadas:
  - *Moderadas*: aprepitant, cimetidina, claritromicina, ácido obeticólico, miconazol, clotrimazol, cobicistat, deferasirox, ticlopidina, fostamatinib, tiabendazol, primaquina, y los anestésicos tópicos lidocaína (tópica y oftálmica), benzocaína y cocaína.
  - *Menores*: dexametasona, omeprazol, hialuronidasa, albendazol.

Consultar el prospecto para información sobre advertencias y contraindicaciones de la etiqueta, ya que no se dispone de ella en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en un puntaje computacional alto (99.09%), sin ensayos clínicos ni literatura (nivel L5). Además, el único registro sanitario en Colombia está cancelado y la vía de administración habitual no es compatible de forma evidente con la gastroduodenitis.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente sin datos.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida de literatura preclínica y clínica sobre anestésicos locales en gastroduodenitis o dolor visceral gastroduodenal.
- Evaluar la compatibilidad de vías de administración y la viabilidad de una formulación o vía adecuada para el tracto digestivo superior.
- Confirmar la situación regulatoria: el registro está cancelado, por lo que no hay producto vigente en Colombia.
- Analizar las contraindicaciones del grafo (hepáticas, renales, cardiovasculares y neuromusculares) frente a la población objetivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

