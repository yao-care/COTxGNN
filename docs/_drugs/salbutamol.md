---
layout: default
title: Salbutamol
parent: Solo Predicción del Modelo (L5)
nav_order: 579
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Salbutamol: nueva indicación predicha, Conjuntivitis papilar (nivel de evidencia L5). Indicación original: SALBUTAMOL"
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
---

# Salbutamol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Salbutamol: De Broncodilatador a Conjuntivitis Papilar
{: .text-alpha }

## Resumen en Una Frase

Salbutamol es un agonista selectivo de los receptores β2-adrenérgicos, utilizado originalmente como broncodilatador para el asma y la EPOC.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis papilar**, pero hasta ahora **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SALBUTAMOL (el registro sanitario no detalla una indicación más específica; clínicamente se usa en asma y EPOC) |
| Nueva Indicación Predicha | Conjuntivitis papilar |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 10 de 12) |
| Número de Registros Sanitarios | 12 (vigentes: 10) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Salbutamol (traducción no oficial): «El sulfato de salbutamol es un agonista beta 2 -adrenérgico. Los efectos farmacológicos del sulfato de salbutamol se atribuyen a la activación de los receptores beta 2 -adrenérgicos del músculo liso de las vías respiratorias. La activación de los receptores beta 2 -adrenérgicos produce la activación de la adenilciclasa y un aumento de la concentración intracelular de 3',5'-adenosín monofosfato cíclico (AMP cíclico).» Texto original en inglés: "Albuterol sulfate is a beta 2 -adrenergic agonist. The pharmacologic effects of albuterol sulfate are attributable to activation of beta 2 -adrenergic receptors on airway smooth muscle. Activation of beta 2 -adrenergic receptors leads to the activation of adenylcyclase and to an increase in the intracellular concentration of cyclic-3', 5’-adenosine monophosphate (cyclic AMP)." ([DailyMed: Albuterol Sulfate Inhalation (albuterol sulfate) prescribing information, Amneal Pharmaceuticals NY LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e449282-ee58-4e36-b983-85c4e6f0864d), versión del 2024-12-20; consultado el 2026-11-19). Según la información farmacológica conocida, salbutamol es un agonista altamente selectivo del receptor β2-adrenérgico (ADRB2), usado en el tratamiento del asma y la EPOC, y recientemente aprobado en EE. UU. también para broncoespasmo y broncoespasmo inducido por ejercicio.

La relación con la nueva indicación es especulativa. Trabajos preclínicos sugieren que los agonistas β2 tienen cierta actividad antiinflamatoria y antialérgica en la conjuntiva (por ejemplo, reducción de la permeabilidad microvascular y estabilización de mastocitos), lo que podría ser relevante en una conjuntivitis de base inflamatoria/alérgica. Sin embargo, no se recuperaron ensayos clínicos ni literatura para esta indicación, por lo que el vínculo mecanístico no está respaldado por datos directos.

Además, la compatibilidad de vía de administración está pendiente de evaluación: la presentación registrada en Colombia es un aerosol inhalado, y una indicación ocular probablemente exigiría una formulación tópica oftálmica distinta.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19900625 | VENTILAN® OSP INHALADOR | AEROSOLES | SALBUTAMOL | Vigente |
| 19983467 | MUXOL ® JARABE NIÑOS | JARABE | SALBUTAMOL Y OTROS FARMACOS PARA ENFERMEDAD OBSTRUCTIVA DE LA VIA AER… | Vigente |
| 19983468 | MUXOL® JARABE ADULTOS | SOLUCION ORAL | SALBUTAMOL Y OTROS FARMACOS PARA ENFERMEDAD OBSTRUCTIVA DE LA VIA AER… | Vigente |
| 19988817 | NEUMOLEX JARABE | SOLUCION ORAL | SALBUTAMOL Y OTROS FARMACOS PARA ENFERMEDAD OBSTRUCTIVA DE LA VIA AER… | Vigente |
| 20011983 | SALBUTAMOL 100MCG/DOSIS | SUSPENSION PARA INHALACION | SALBUTAMOL | Vigente |

Se muestran 5 de 12 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones (relaciones del grafo de conocimiento, no del prospecto):** el grafo de conocimiento asocia salbutamol con contraindicación o precaución en: hipertensión arterial e hipertensión ocular, síndrome de QT largo (incluido el familiar), paro cardíaco súbito y enfermedad de la conducción cardíaca, isquemia miocárdica y enfermedad coronaria, epilepsia, déficit de potasio, diabetes mellitus y cetoacidosis diabética, acidosis metabólica, hipertiroidismo (enfermedad de Graves, tirotoxicosis), hiperplasia prostática benigna y obstrucción del cuello vesical, y glaucoma de ángulo cerrado.
- **Nota relevante para la indicación ocular propuesta:** la asociación con hipertensión ocular y glaucoma de ángulo cerrado exige especial cautela si se considerara cualquier uso oftálmico.
- **Señal adicional:** se identificó un reporte de caso de anafilaxia causada por el propio salbutamol.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para conjuntivitis papilar es de puntaje muy alto, pero no tiene ningún respaldo clínico ni bibliográfico (nivel L5). Además, el perfil de seguridad del grafo incluye contraindicaciones oculares relevantes.

<!-- review:begin co-lic-20261105-salbutamol-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado y el perfil de seguridad del grafo incluye contraindicaciones oculares relevantes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 12 registros sanitarios (vigentes: 10); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-salbutamol-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y revisión de la literatura preclínica sobre agonistas β2 en la conjuntiva.
- Evaluación de la compatibilidad de vía de administración (formulación oftálmica tópica) y de la similitud con la indicación original.
- Obtención y análisis del prospecto oficial (INVIMA) para completar el cribado de seguridad.
- Estudios preclínicos y, de ser favorables, un ensayo clínico exploratorio en conjuntivitis alérgica o papilar.
- Aclarar la situación regulatoria, dado que no existen registros vigentes en Colombia.

---

### Nota sobre otras indicaciones predichas

Entre las demás predicciones, la **enfermedad pulmonar obstructiva** muestra el mayor respaldo (nivel L1, incluido un ensayo de Fase 3 con 1118 participantes), pero coincide con el uso ya establecido del fármaco, por lo que es una confirmación y no un reposicionamiento. La **anafilaxia** (L4) cuenta con un ensayo de Fase 3 terminado prematuramente con solo 24 participantes, sin conclusiones fiables de eficacia.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Albuterol Sulfate Inhalation (albuterol sulfate) prescribing information, Amneal Pharmaceuticals NY LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e449282-ee58-4e36-b983-85c4e6f0864d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

