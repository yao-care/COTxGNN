---
layout: default
title: Aztreonam
parent: Solo Predicción del Modelo (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
monitor_inn: "AZTREONAM"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-11-24
description: "Aztreonam: nueva indicación predicha, hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). Indicación original: AZTREONAM"
---

# Aztreonam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Aztreonam: antibiótico monobactámico → hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Aztreonam es un antibiótico monobactámico que actúa sobre bacterias gramnegativas aerobias.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia (hyperamylasemia)**,
pero actualmente no hay ensayos clínicos ni publicaciones que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | AZTREONAM |
| Nueva Indicación Predicha | hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0,9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es razonable esta predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Aztreonam (traducción no oficial): «Aztreonam es un agente bactericida que actúa mediante la inhibición de la síntesis de la pared celular bacteriana. Aztreonam tiene actividad en presencia de algunas betalactamasas, tanto penicilinasas como cefalosporinasas, de bacterias gramnegativas y grampositivas.» Texto original en inglés: "Aztreonam is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Aztreonam has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6), versión del 2024-06-03; consultado el 2026-11-19). Según la información conocida, aztreonam es un antibiótico monobactámico que inhibe la síntesis de la pared celular bacteriana al unirse a la proteína fijadora de penicilina 3 (PBP3) de bacterias gramnegativas aerobias.

La hiperamilasemia, en cambio, es un hallazgo de laboratorio (elevación de la amilasa en sangre) y no una enfermedad infecciosa. No se identifica un vínculo mecanístico plausible entre la acción antibacteriana de aztreonam y esta condición.

Por ello, el puntaje alto del modelo debe interpretarse con cautela: es una señal computacional sin respaldo biológico ni clínico, y no una evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19982144 | AZTREONAM 1G POLVO PARA RECONSTITUIR A SOLUCIÓN INYECTABLE | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | AZTREONAM | Vigente |
| 20163741 | AZBIOS® 1G POLVO PARA RECONSTITUIR A SOLUCION INYECTABLE | POLVO ESTERIL PARA RECONSTITUIR A SOLUCION INYECTABLE | AZTREONAM | Vigente |
| 20271484 | AZTREONAM 1GPOLVO ESTERIL PARA RECONSTITUIR A SOLUCIÓN INYECTABLE | POLVO ESTERIL PARA RECONSTITUIR A SOLUCION INYECTABLE | AZTREONAM | Vigente |

Se muestran los 3 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 27 interacciones en total. Las de nivel moderado incluyen ácido picosulfúrico, dicumarol y warfarina (en el caso de los anticoagulantes, conviene vigilar la coagulación). Otras interacciones registradas, de gravedad no clasificada, incluyen vancomicina, amikacina, anfotericina B, tacrolimus, heparina, morfina, fluconazol, metronidazol y varios inhibidores de la bomba de protones (omeprazol, pantoprazol, lansoprazol).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que estudie aztreonam en hiperamilasemia, y el mecanismo antibacteriano no explica un posible efecto sobre esta alteración de laboratorio. El puntaje alto parece un artefacto del modelo.

**Para avanzar se necesita:**
- Una hipótesis biológica que vincule a aztreonam con la hiperamilasemia
- Estudios preclínicos o clínicos que evalúen directamente esta indicación
- Datos de seguridad del prospecto (advertencias y contraindicaciones)

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

