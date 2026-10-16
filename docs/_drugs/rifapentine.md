---
layout: default
title: Rifapentine
parent: Evidencia Moderada (L3-L4)
nav_order: 559
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Rifapentine: nueva indicación predicha, Lepra (nivel de evidencia L3). Indicación original: Rifapentin"
---

# Rifapentine
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

# Rifapentina: De Rifapentin (texto del registro INVIMA) a Lepra

## Resumen en Una Frase

Rifapentina es un antibiótico de la familia de las rifamicinas. En Colombia su único registro sanitario (hoy cancelado) lo consigna simplemente como "Rifapentin", sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **lepra**, con **0 ensayos clínicos registrados** y **20 publicaciones**. Entre ellas hay un ensayo aleatorizado de profilaxis posexposición en contactos domiciliarios y varios estudios preclínicos.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rifapentin (texto del registro INVIMA, sin mayor detalle) |
| Nueva Indicación Predicha | Lepra |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Rifapentina inhibe la ARN polimerasa dependiente de ADN bacteriana (gen *rpoB*), el mismo blanco de la rifampicina. No se dispuso de un campo formal de mecanismo de acción, pero el análisis de reposicionamiento describe este mecanismo.

*Mycobacterium leprae*, el agente de la lepra, es sensible a las rifamicinas. La rifampicina ya es pilar del tratamiento multifármaco y de la profilaxis posexposición. Rifapentina tiene una vida media más larga y mayor potencia frente a micobacterias, lo que permite esquemas espaciados, incluso de dosis única. Esto respalda la plausibilidad mecanística de la predicción.

En la literatura hay datos preclínicos de eficacia en el modelo de almohadilla plantar de ratón y un ensayo en contactos domiciliarios con rifapentina en dosis única. No hay ensayos clínicos registrados para esta indicación, por lo que el nivel de evidencia se basa solo en publicaciones.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37195940](https://pubmed.ncbi.nlm.nih.gov/37195940/) | 2023 | ECA | N Engl J Med | Evalúa rifapentina en dosis única como profilaxis posexposición en contactos domiciliarios de pacientes con lepra, tras observarse mayor actividad bactericida que la rifampicina en modelos murinos. El resumen disponible no incluye los resultados. |
| [37585641](https://pubmed.ncbi.nlm.nih.gov/37585641/) | 2023 | Comentario | N Engl J Med | Correspondencia sobre el ensayo de rifapentina en contactos domiciliarios. |
| [37585642](https://pubmed.ncbi.nlm.nih.gov/37585642/) | 2023 | Respuesta de autores | N Engl J Med | Respuesta de los autores a la correspondencia sobre el mismo ensayo. |
| [40278757](https://pubmed.ncbi.nlm.nih.gov/40278757/) | 2025 | Revisión | Trop Med Infect Dis | Revisa eficacia, seguridad y factibilidad de la quimioprofilaxis posexposición con rifamicinas en lepra. Parte del efecto del 57% observado con rifampicina en el estudio COLEP. |
| [38440733](https://pubmed.ncbi.nlm.nih.gov/38440733/) | 2024 | Revisión | Front Immunol | Revisión sobre tratamiento, prevención y respuesta inmune en lepra. Señala que el tratamiento multifármaco no logra erradicar la enfermedad y que la resistencia a rifampicina limita su eficacia. |
| [32936818](https://pubmed.ncbi.nlm.nih.gov/32936818/) | 2020 | Preclínico | PLoS Negl Trop Dis | Compara rifampicina, rifapentina, moxifloxacino, minociclina y claritromicina como profilaxis posexposición en un modelo murino de infección subclínica. |
| [30207440](https://pubmed.ncbi.nlm.nih.gov/30207440/) | 2016 | Preclínico | Indian J Lepr | Evalúa la actividad antibacteriana de rifapentina y otros fármacos, solos y combinados, en un modelo murino de lepra resistente a rifampicina. |
| [29071280](https://pubmed.ncbi.nlm.nih.gov/29071280/) | 2017 | Simulación molecular | Mol Biol Res Commun | Analiza la resistencia cruzada de rifabutina y rifapentina con rifampicina para valorar su uso en lepra farmacorresistente. |
| [22125933](https://pubmed.ncbi.nlm.nih.gov/22125933/) | 2011 | Preclínico | Lepr Rev | Rifapentina, rifampicina, moxifloxacino y otros mostraron cierta actividad bactericida contra *M. leprae* en ratones. |
| [11201894](https://pubmed.ncbi.nlm.nih.gov/11201894/) | 2000 | Preclínico | Lepr Rev | Mide la actividad bactericida de rifapentina y moxifloxacino, frente a fármacos antilepra establecidos, en ratón. Busca un esquema mensual supervisable. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20242586 | RIFANIL-INH® Tabletas Recubiertas (Vesalius Pharma S.A.S.) | Tableta recubierta | RIFAPENTIN |

Este registro figura como **cancelado**. Actualmente no hay productos con rifapentina vigentes en Colombia según los datos compilados.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** porfiria hereditaria, enfermedad del metabolismo de porfirinas, porfiria, enfermedad hepática, enfermedad de la vesícula biliar, abuso o dependencia de sustancias, hiperbilirrubinemia (incluida la hereditaria), síndrome de Gilbert, colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones farmacológicas:** se identificaron 100 interacciones potenciales. Entre las primeras 20 listadas:
  - **Mayores:** eliglustat y naldemedina.
  - **Moderadas:** rabeprazol, hidrocortisona, dexametasona, betametasona, triamcinolona, colecalciferol, calcifediol, calcitriol, pioglitazona, glimepirida, clorpropamida, saxagliptina, linagliptina, aprepitant, metronidazol, claritromicina, dronabinol y ácido picosulfúrico.
  - Como otras rifamicinas, rifapentina puede inducir enzimas metabólicas (CYP3A4/UGT1A1) y reducir la exposición a otros fármacos.
- Las advertencias y contraindicaciones del prospecto INVIMA no estaban disponibles. Consultar el prospecto para la información de seguridad oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La plausibilidad mecanística es sólida y existe un ensayo aleatorizado de profilaxis posexposición. Sin embargo, no hay ensayos clínicos registrados, el soporte restante es mayormente preclínico, y la evidencia queda en L3. Además, el único registro sanitario local está cancelado y faltan los datos de seguridad del prospecto, por lo que no es posible avanzar con garantías.

**Para avanzar se necesita:**
- Obtener y analizar los resultados completos del ensayo de dosis única en contactos domiciliarios (NEJM 2023).
- Descargar el prospecto del INVIMA para completar advertencias y contraindicaciones, lo que bloquea el tamizaje de seguridad.
- Confirmar los datos formales de mecanismo de acción en DrugBank.
- Aclarar la situación regulatoria del registro cancelado y la disponibilidad actual de rifapentina en Colombia.
- Definir el esquema posológico y los riesgos de interacciones, en especial hepatotoxicidad y fármacos concomitantes, antes de cualquier uso en lepra.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

