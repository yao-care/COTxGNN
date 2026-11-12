---
layout: default
title: Primaquine
parent: Solo Predicción del Modelo (L5)
nav_order: 534
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-12
monitor_inn: "primaquine"
predicted_indications: ["myiasis", "furuncular myiasis", "wound myiasis", "creeping myiasis", "toxoplasmosis", "nocardiosis", "pneumocystosis"]
description: "Primaquine: nueva indicación predicha, Miasis (myiasis) (nivel de evidencia L5). Indicación original: PRIMAQUINA"
---

# Primaquine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Primaquine: Miasis (myiasis)
{: .text-alpha }

## Resumen en Una Frase

La primaquina es un antimalárico del grupo de las 8-aminoquinolinas, comercializado en Colombia como tabletas de 15 mg. El texto de su registro sanitario solo indica el nombre del producto, sin detallar la indicación.
El modelo TxGNN predice que podría ser efectiva para **miasis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PRIMAQUINA |
| Nueva Indicación Predicha | Miasis (myiasis) |
| Puntaje de Predicción TxGNN | 0.9976 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, la primaquina es una 8-aminoquinolina activa contra las formas hepáticas latentes (hipnozoítos) de *Plasmodium vivax* y *P. ovale*, y contra los gametocitos maduros de *P. falciparum*. Se cree que actúa mediante metabolitos reactivos que generan estrés oxidativo.

La miasis es una infestación por larvas de moscas (dípteros). Es un problema distinto de la malaria, que es una infección por protozoos. **No se identifica un vínculo mecanístico plausible** entre el efecto de la primaquina sobre *Plasmodium* y la eliminación de larvas de mosca. El puntaje alto (0.9976) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

La miasis se trata con extracción mecánica de las larvas, desbridamiento de las heridas y, cuando es necesario, ivermectina. Los subtipos de miasis (furunculosa, de heridas, migratoria) comparten puntajes casi idénticos del modelo TxGNN (aprendizaje profundo) (0.9973), lo que puede reflejar similitudes aprendidas entre enfermedades relacionadas y no evidencia independiente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19943341 | PRIMAQUINA TABLETAS 15 MG (FAES FARMA COLOMBIA S.A.S.) | Tableta | PRIMAQUINA (el registro no detalla la indicación) |

---

## Consideraciones de Seguridad

- **Contraindicaciones asociadas en el grafo de conocimiento** (relaciones fármaco-enfermedad de PrimeKG, no texto de prospecto): neutropenia, agranulocitosis, deficiencia de G6PD, anemia hemolítica, metahemoglobinemia por deficiencia de metahemoglobina reductasa, enfermedad por almacenamiento de glucógeno, cistinuria, galactosemia y deficiencia de piruvato deshidrogenasa E3.
- **Interacciones farmacológicas**: se registran **278 interacciones** en total. Entre las principales, de las 20 listadas:
  - **Mayor**: dolasetrón.
  - **Moderada**: famotidina, alosetrón, loperamida, bisacodilo, claritromicina, levofloxacino, ondansetrón, granisetrón, palonosetrón, lactulosa, lactitol, glicerina, aceite de ricino, citrato de magnesio, ácido picosulfúrico, sulfato de sodio y polietilenglicol.
  - **Menor**: metronidazol.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para miasis no tiene ensayos clínicos ni literatura que la respalden (nivel L5), y no existe un mecanismo biológico plausible. Además, el tratamiento estándar ya es eficaz.

<!-- review:begin co-lic-20261105-primaquine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el tratamiento estándar ya es eficaz y la primaquina no tiene registro sanitario vigente en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-primaquine-1 -->

**Observación adicional:** entre las demás predicciones del modelo, **malaria** (uso original, con múltiples ensayos de Fase 3) y **neumocistosis** (combinación clindamicina-primaquina como alternativa de segunda línea) cuentan con evidencia clínica real y nivel L1. Ambas se clasifican como "Proceed with Guardrails". Si se busca una vía de reposicionamiento con sustento, la neumocistosis sería un candidato más razonable que la miasis.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que justifiquen un efecto sobre larvas de dípteros, o estudios preclínicos que lo demuestren.
- Estudios in vitro o in vivo de actividad larvicida de la primaquina.
- Obtener y analizar el prospecto oficial del INVIMA para completar el perfil de seguridad.
- Verificar la disponibilidad comercial en Colombia.
- Plan de tamizaje de G6PD y monitoreo hematológico en caso de cualquier uso futuro.

<!-- review:begin co-lic-20261105-primaquine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Verificar la disponibilidad comercial en Colombia, dado que el único registro está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-primaquine-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y la primaquina no tiene registro sanitario vigente en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que el único registro está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

