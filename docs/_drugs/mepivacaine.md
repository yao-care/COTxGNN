---
layout: default
title: Mepivacaine
parent: Solo Predicción del Modelo (L5)
nav_order: 428
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Mepivacaine: nueva indicación predicha, Gastroduodenitis (nivel de evidencia L5). Indicación original: Mepivacaína combinaciones"
monitor_inn: "mepivacaine"
predicted_indications: ["gastroduodenitis", "peptic ulcer disease"]
---

# Mepivacaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Mepivacaína: De Anestésico Local (Combinaciones de Mepivacaína) a Gastroduodenitis

## Resumen en Una Frase

La mepivacaína es un anestésico local de tipo amida, registrado en Colombia bajo la indicación genérica "Mepivacaína combinaciones" (producto ODONTOCAINA® 2%, solución inyectable).
El modelo TxGNN predice que podría ser efectiva para **gastroduodenitis**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Mepivacaína combinaciones |
| Nueva Indicación Predicha | Gastroduodenitis |
| Puntaje de Predicción TxGNN | 99.49% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la mepivacaína es un anestésico local de tipo amida que bloquea los canales de sodio dependientes de voltaje, y su uso está establecido para la anestesia local (en este caso, en presentación odontológica inyectable).

La relación con la gastroduodenitis es débil. De manera especulativa, un anestésico local podría aliviar el dolor de la mucosa, pero esto no está respaldado por ningún ensayo ni publicación. El bloqueo de canales de sodio no tiene un papel reconocido en la cicatrización de la mucosa gastroduodenal ni en la supresión ácida, y el uso sistémico u oral para inflamación gastroduodenal no está establecido.

Por lo tanto, el puntaje alto de TxGNN (0.995) debe interpretarse solo como una señal computacional que requiere validación, no como evidencia de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para gastroduodenitis.

*Nota: para la segunda predicción del modelo (enfermedad ulcerosa péptica), la única publicación recuperada (PMID 6890367, 1982) es un estudio en animales sobre farmacología de seguridad de la lofexidina, un fármaco distinto; no aporta evidencia sobre la mepivacaína.*

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19933337 | ODONTOCAINA® 2% | Solución inyectable | Mepivacaína combinaciones | Cancelado |

El fabricante es Productora y Comercializadora Odontológica New Stetic S.A. Actualmente no hay registros vigentes en Colombia.

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, miastenia gravis (incluida la de inicio en adultos), enfermedad de la unión neuromuscular, deficiencia de butirilcolinesterasa, enfermedad cardiovascular y enfermedad cardíaca.
- **Interacciones Farmacológicas**: se identificaron 11 interacciones.
  - Moderadas (10): morfina liposomal, lidocaína (tópica y oftálmica), benzocaína (tópica), cocaína (tópica y nasal), tetracaína (oftálmica y tópica), oxibuprocaína (oftálmica) y cinchocaína (tópica). En general corresponden a la combinación con otros anestésicos locales o depresores, con posible efecto aditivo.
  - Menores (1): hialuronidasa.

No se dispone de las advertencias y contraindicaciones del prospecto; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (L5), sin ensayos clínicos ni literatura pertinente, y no existe un vínculo mecanístico plausible entre el bloqueo de canales de sodio y la gastroduodenitis. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener los datos del mecanismo de acción (MOA) desde DrugBank
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), indispensable antes de cualquier evaluación de seguridad
- Estudios preclínicos que justifiquen un mecanismo plausible en mucosa gastroduodenal
- Definir la vía de administración requerida y su compatibilidad con la presentación inyectable disponible
- Evaluar si existe alguna presentación vigente en Colombia, dado que el único registro está cancelado
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

