---
layout: default
title: Imipenem
parent: Solo Predicción del Modelo (L5)
nav_order: 337
evidence_level: L5
indication_count: 9
monitor_inn: "IMIPENEM"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "eosinophilia-myalgia syndrome"]
last_modified_at: 2026-11-25
description: "Imipenem: nueva indicación predicha, esclerodermia difusa (diffuse scleroderma) (nivel de evidencia L5). Indicación original: IMIPENEM Y CILASTATINA"
---

# Imipenem
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Imipenem: antibiótico carbapenémico → esclerodermia difusa (diffuse scleroderma)
{: .text-alpha }

## Resumen en Una Frase

Imipenem es un antibiótico carbapenémico de amplio espectro, usado contra infecciones bacterianas.
El modelo TxGNN lo propone para **esclerodermia difusa (diffuse scleroderma)** con un puntaje de 0,9999. Hasta ahora no hay **ningún ensayo clínico ni publicación** que respalde esta dirección, por lo que se trata solo de una señal del modelo, sin evidencia real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IMIPENEM Y CILASTATINA |
| Nueva Indicación Predicha | esclerodermia difusa (diffuse scleroderma) |
| Puntaje de Predicción TxGNN | 0,9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 5 de 5) |
| Número de Registros Sanitarios | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Imipenem es (traducción no oficial): «Inhibidor de las proteínas bacterianas de unión a penicilina». Texto original en inglés: "Bacterial penicillin-binding protein inhibitor" ([ChEMBL CHEMBL43708 (imipenem): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL43708), CC BY-SA 3.0; consultado el 2026-11-19). Por conocimiento general, imipenem es un carbapenémico que inhibe la síntesis de la pared celular bacteriana.

La esclerodermia difusa es una enfermedad autoinmune con fibrosis de la piel y de órganos internos. No tiene un componente infeccioso bacteriano que un antibiótico pueda tratar, y no se identificó un vínculo mecanístico plausible entre ambos.

El puntaje alto es un resultado del modelo, no una prueba de eficacia. Sin ensayos clínicos ni literatura que lo sustenten, no debe interpretarse como indicio de beneficio clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19982795 | IMIPENEM Y CILASTATINA1G. | POLVO ESTERIL PARA RECONSTITUIR A SOLUCION INYECTABLE | IMIPENEM Y CILASTATINA | Vigente |
| 20072860 | IMIPENEM 500 MG CILASTATINA 500 MG | POLVO ESTERIL PARA RECONSTITUIR A SOLUCION INYECTABLE | IMIPENEM Y CILASTATINA | Vigente |
| 20212212 | RECARBRIO® | POLVO PARA SOLUCIÓN INYECTABLE | IMIPENEM. CILASTATINA . RELEBACTAM | Vigente |
| 20256282 | IMIPENEM+CILASTATINA 500+500 MG POLVO PARA RECONSTITUIR | POLVO ESTERIL PARA RECONSTITUIR A SOLUCION INYECTABLE | IMIPENEM Y CILASTATINA | Vigente |
| 20165470 | IMCIBIOS® | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | IMIPENEM Y CILASTATINA | Vigente |

Se muestran los 5 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

## Consideraciones de Seguridad

**Interacciones farmacológicas** (15 interacciones registradas):

| Gravedad | Fármacos |
|------|------|
| Mayor | Bupropión, iohexol, iopamidol |
| Moderada | Polietilenglicol (3350 con electrolitos), dicumarol, warfarina, lindano, aminofilina, difilina, oxtrifilina, teofilina, ciclosporina, etinilestradiol, ácido micofenólico, pemetrexed |

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni publicaciones que la respalden y carece de un vínculo mecanístico plausible. Por ello el nivel de evidencia es L5 y no hay base para avanzar.

**Para avanzar se necesita:**
- Estudios preclínicos o mecanísticos que muestren un efecto de imipenem en procesos inflamatorios o fibróticos relevantes para la esclerodermia.
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto.
- Evidencia clínica directa en esclerodermia difusa antes de reconsiderar la decisión.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL43708 (imipenem): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL43708) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

