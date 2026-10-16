---
layout: default
title: Theophylline
parent: Solo Predicción del Modelo (L5)
nav_order: 622
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Theophylline: nueva indicación predicha, Enfermedad trombótica (nivel de evidencia L5). Indicación original: Ambroxol"
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "obstructive lung disease", "pharyngitis", "acute laryngopharyngitis"]
---

# Theophylline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Teofilina: De Ambroxol (registro sanitario cancelado) a Enfermedad Trombótica

## Resumen en Una Frase

Teofilina figura en Colombia en un único registro sanitario, hoy cancelado, de un jarabe cuya indicación aprobada aparece como "AMBROXOL". Clínicamente es un broncodilatador usado en asma, enfisema y bronquitis crónica.
El modelo TxGNN predice como primera opción que podría ser efectiva para **enfermedad trombótica**, pero **sin ensayos clínicos** y con **18 publicaciones** recuperadas que, en su mayoría, no tratan de teofilina en trombosis.

> **Nota importante:** la indicación de mayor puntaje (enfermedad trombótica) no tiene respaldo clínico. La indicación con mayor evidencia entre las candidatas es **enfermedad pulmonar obstructiva** (rango 5), que es en realidad el área terapéutica ya conocida del fármaco. Se presenta en el análisis complementario.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ambroxol (texto del registro sanitario; corresponde a un producto con indicación registrada de forma incompleta) |
| Nueva Indicación Predicha | Enfermedad trombótica |
| Puntaje de Predicción TxGNN | 99.62% |
| Nivel de Evidencia | L4 (L5 si se considera solo ausencia de estudios reales de eficacia) |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información farmacológica conocida, la teofilina es un inhibidor no selectivo de fosfodiesterasas y antagonista de los receptores de adenosina (A1, A2A, A2B y A3), y se utiliza para la obstrucción reversible de las vías respiratorias.

Mecanísticamente, la inhibición de fosfodiesterasas podría aumentar el AMPc plaquetario y reducir la agregación. Sin embargo, el antagonismo de adenosina puede oponerse a ese efecto antiplaquetario, por lo que **la dirección del efecto es incierta**. La relación con la indicación original (respiratoria) es limitada.

La literatura recuperada para esta indicación es en gran parte ajena al tema (farmacocinética de ticlopidina, ensayos de biomarcadores, un aptasensor para detectar teofilina) y no contiene datos de eficacia de teofilina en trombosis. El alto puntaje del modelo no está respaldado por evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para enfermedad trombótica.

---

## Evidencia de Literatura

Se muestran las publicaciones más cercanas al tema (ninguna evalúa eficacia de teofilina en trombosis):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Revisión | CRC Critical Reviews in Biochemistry | Papel de prostaglandinas, tromboxano A2 y prostaciclina en la agregación plaquetaria y la aterosclerosis |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Revisión farmacocinética | Clinical Pharmacokinetics | Farmacocinética de ticlopidina (otro antiplaquetario); no trata de teofilina |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Estudio de laboratorio | General Pharmacology | Interacción de milrinona y adenosina en la inhibición de la respuesta plaquetaria humana |
| [19897460](https://pubmed.ncbi.nlm.nih.gov/19897460/) | 2010 | Estudio clínico | Heart | Isquemia miocárdica breve y reactividad plaquetaria en enfermedad coronaria |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Cohorte/laboratorio | Inflamm Bowel Dis | Agregados plaqueta-leucocito en enfermedad inflamatoria intestinal |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Estudio transversal | Rheumatology | Activación plaquetaria y de neutrófilos en enfermedad de Behçet |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Método de ensayo | Platelets | Medición de sCLEC-2 soluble como marcador de activación plaquetaria |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Método de ensayo | Br J Haematol | Radioinmunoensayo de factor plaquetario 4; la teofilina se usa solo como componente del anticoagulante de la muestra |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20005160 (cancelado) | TRIATUSIC® JARABE (LABQUIFAR LTDA.) | Jarabe | AMBROXOL |

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo (según el grafo de conocimiento, no texto de prospecto):** hipertensión, insuficiencia hepática y enfermedad hepática, epilepsia, trastornos de ansiedad y psicóticos, porfiria, enfermedad renal, enfermedad de la vesícula biliar, trombocitopenia, neutropenia y agranulocitosis, hipotiroidismo, úlcera péptica, glaucoma de ángulo abierto, diabetes y cetoacidosis diabética, hiperplasia prostática benigna, dermatitis herpetiforme.
- **Farmacología relevante:** la teofilina se une a los receptores de adenosina A1, A2A, A2B y A3, lo que explica parte de su perfil de efectos y de interacciones.
- **Otras precauciones** (de las evidencias de otras indicaciones): índice terapéutico estrecho, interacciones mediadas por CYP1A2 (por ejemplo ciprofloxacino, isoniazida) y efecto del tabaquismo sobre el aclaramiento, por lo que se requiere monitoreo de niveles plasmáticos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Análisis Complementario: Otras Indicaciones Predichas

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Recomendación | Comentario |
|---|---|---|---|---|
| Enfermedad pulmonar obstructiva | 99.48% | L1 | Proceed with Guardrails | Varios ensayos de Fase 3 completados (p. ej., NCT01599871, NCT02340520, NCT03984188, NCT00252785); confirma el uso ya conocido, no es un reposicionamiento real |
| Enfermedad de las vías respiratorias nasales (cavidad nasal) | 99.53% | L2 | Pregunta de investigación | Ensayo de Fase 2 en rinitis alérgica (NCT01132781, n=28) y estudio de provocación nasal (PMID 9648963); beneficio sobre corticoides intranasales y antihistamínicos no demostrado |
| Enfermedad traqueal | 99.49% | L3 | Pregunta de investigación | Revisiones Cochrane sobre metilxantinas para extubación en prematuros; evidencia humana indirecta |
| Laringotraqueítis | 99.51% | L5 | Hold | Solo predicción; el crup se maneja con corticoides y epinefrina |
| Faringitis | 99.46% | L4 | Hold | Sin fundamento mecanístico claro |
| Laringofaringitis aguda | 99.35% | L5 | Hold | Solo predicción |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura que respalde la teofilina en enfermedad trombótica; el puntaje de 99.62% no tiene sustento clínico y el antagonismo de adenosina podría ir en contra del efecto antiplaquetario deseado. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Estudios preclínicos o mecanísticos que aclaren el efecto de la teofilina sobre la función plaquetaria y la trombosis.
- Datos oficiales del mecanismo de acción y del prospecto (advertencias y contraindicaciones).
- Verificar la disponibilidad real del producto en Colombia, dado que no hay registros vigentes.
- Si se busca una línea con mayor sustento, priorizar enfermedad pulmonar obstructiva (con guardarrailes: monitoreo terapéutico de niveles, interacciones CYP1A2 y estado de tabaquismo) o evaluar la rinitis alérgica como pregunta de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

